# Ingesting an alternative distribution package

**Framework**: MarketplaceKit

Process an available app version from App Store Connect and store it for download from your server.

#### Overview

When an app passes Notarization, App Store Connect makes it available for storage on the back end of your web server. The app format that App Store Connect provides is an , which contains everything a device needs to install the available app. App Store Connect sends newly available apps that an alternative marketplace app distributes to your web server automatically through your notifications webhook; see [`Processing alternative app marketplace notifications`](processing-alternative-marketplace-notifications.md). For your apps that install from your website, you need to download your alternative distribution package from App Store Connect manually.

In either case, to prepare the package for installation on devices, process, or , the package to a specific format, and serve its contents from specific relative locations that the operating system expects.

![A diagram that shows the flow of the ingesting an alternative distribution package. When there’s a new version of an app available, App Store Connect sends a notification to your server’s notifications webhook, your primary back end retrieves the package metadata using  the app distribution package ID from the notification. Your primary back end then downloads the package zip from the content delivery network and saves the manifest and signature to your database or large file storage. Your primary back end registers the variant and delta info, then stores it. For each variant and delta of the app distribution package, your back end retrieves the asset URL by ID from App Store Connect, then downloads the asset from the content delivery network and stores the asset in your database.](https://docs-assets.developer.apple.com/published/557844addd2e5197953a26fbafeac2b2/ingesting-an-alternative-distribution-package-1%402x.png)

#### Receive New Package Version Notification

If the developer of an app that your marketplace distributes enables notifications in App Store Connect, your webhook receives the `AlternativeDistributionPackageVersionAvailable` notification when a new version of that app is available. For information about enabling notifications, see [`Manage distribution on an alternative app marketplace`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/distributing-apps-in-the-european-union/manage-distribution-on-an-alternative-app-marketplace).

When your webhoook receives `AlternativeDistributionPackageVersionAvailable`, check the notification’s `attributes` object for the app ID and version. For example:

```json
{
  "data": {
    "type": "AlternativeDistributionPackageVersionAvailable",
    "version": 1,
    "id": "543c3939-2db6-4fbc-9672-fb0ec5687624",
    "timestamp": "2023-11-27T10:40:37.246-08:00",
    "attributes": {
      "marketplaceAppId": "3839839",
      "appId": "1111",
      "alternativeDistributionPackageId": "f826eb7a-fa2b-420f-a780-356106195663",
      "alternativeDistributionPackageVersionId": "6B29FC40-CA47-1067-B31D-00DD010662DA",
      "alternativeDistributionPackageVersionNum": "1",
      "eventTimestamp": "2023-11-27T18:40:32.143-00:00"
    }
  }
}
```

In the POST body, the alternative distribution package version ID refers to the specific available alternative distribution package. To begin retrieving actual app data from App Store Connect, pass `alternativeDistributionPackageVersionId` as the `id` path parameter to the `alternativeDistributionPackageVersions/{id}` endpoint, as follows:

```None
GET https://api.appstoreconnect.apple.com/v1/alternativeDistributionPackageVersions/6B29FC40-CA47-1067-B31D-00DD010662DA
```

For more information about the `alternativeDistributionPackageVersions/{id}` endpoint, see [`Read information for an alternative distribution package version`](https://developer.apple.com/documentation/AppStoreConnectAPI/GET-v1-alternativeDistributionPackageVersions-_id_).

Example response:

```json
{
  "data": [
    {
      "type": "alternativeDistributionPackageVersions",
      "id": "d1663e24-4360-4f7f-a661-8e616e3b3c3b",
      "attributes": {
        "url": "<Apple_CDN_base_URL>/alternative-distribution-package.zip?accessKey=<access_key>",
        "urlExpirationDate": "2024-03-29T21:09:21-07:00",
        "version": "1",
        "state": "COMPLETED"
        }, ...
```

In the response, navigate to the `data.attributes.url`, which downloads `alternative-distribution-package.zip`. Inside the `zip` file is a manifest and a signature:

| File | Description |
| --- | --- |
| `manifest.json` | Instructions you use to assemble the alternative distribution package. |
| `signature` | A signature that the device’s operating system uses to verify the package contents. |

> 💡 **Tip**: Save the `alternativeDistributionPackageId` in case you want to query App Store Connect for all alternative distribution package versions outside of a normal `AlternativeDistributionPackageVersionAvailable` notification. For more information, see [`Read alternative distribution package information`](https://developer.apple.com/documentation/AppStoreConnectAPI/GET-v1-alternativeDistributionPackages-_id_).

For more information on alternative distribution package workflows, see [`Alternative Distribution Packages`](https://developer.apple.com/documentation/AppStoreConnectAPI/alternative-distribution-packages).

#### Process the Manifest File

The manifest file contains links to assets that you download to compose a complete alternative distribution package. The individual assets represent unique variations and portions of an app, as required to install it on the variety of Apple devices that the app supports.

An example manifest follows:

```json
{
  "distributionPackageRevision": 1,
  "appleItemId": "10738181399",
  "bundleId": "com.megabytemart.backyardbirds",
  "shortVersionString": "1.5",
  "bundleVersion": "1",
  "appleVersionId": "2000013060",
  "platforms": [
    "ios"
  ],
  "minimumSystemVersions": {
    "ios": "17.2"
  },
  "requiredDeviceCapabilities": [
    "arm64"
  ],
  "appInstallDeterminants": [],
  "variants": [
    {
      "publicId": "219750db-80c2-4c75-aecc-fa67835f384d",
      "assetPath": "variant/219750db-80c2-4c75-aecc-fa67835f384d.ipa",
      "installTargets": [
        {
          "device": "iPhone14,5",
          "os": "17.4"
        },
        {
          "device": "iPhone13,4",
          "os": "17.4"
        }, 
          ...
        }
      ],
      "variantDetails": {
        "compressedSize": 183335,
        "uncompressedSize": 375808,
        "hashes": [
          {
            "algorithm": "sha256",
            "chunkSize": 183335,
            "encryptedChunkDigests": [
              "ecc9df4860bd98b17dd8eae7f6b7aa6371fb51911ad13578da2293409366e53c"
            ]
          }
        ]
      }
    }
  ],
  "deltas": [
    {
      "publicId": "ffbc52b6-f76b-4d51-9eff-5388bc6b7572",
      "assetPath": "delta/ffbc52b6-f76b-4d51-9eff-5388bc6b7572.ipa",
      "sourceVariant": {
        "installTargets": [
          {
            "device": "iPhone14,5",
            "os": "17.4"
          },
          {
            "device": "iPhone13,4",
            "os": "17.4"
          },
            ...
          }
        ],
        "appleVersionId": "2000011760",
        "version": "1.1"
      },
      "targetVariantAssetPath": "variant/219750db-80c2-4c75-aecc-fa67835f384d.ipa",
      "deltaDetails": {
        "compressedSize": 26668,
        "uncompressedSize": 82944,
        "hashes": [
          {
            "algorithm": "sha256",
            "chunkSize": 26668,
            "encryptedChunkDigests": [
              "3eb8f4ea27196289933047e0971d03e910436781f42da896e666a8306ecf3e0f"
            ]
          }
        ]
      }
    }
  ]
}
```

When the operating system installs an app on a device, it accesses your server at different subfolders off the base URL you provide in the download link depending on the needs of the requesting device. When your endpoint processes the alternative distribution package, you ingest and organize the contents that the manifest references according to two categories:

#### Download App Variants

The variants reside at the top of the manifest. The first variant in the example has a `publicId` of `219750db-80c2-4c75-aecc-fa67835f384d`. To download the variant, provide the `publicId` as the `id` path parameter of the `alternativeDistributionPackageVariants` endpoint, as follows:

```None
GET https://api.appstoreconnect.apple.com/alternativeDistributionPackageVariants/219750db-80c2-4c75-aecc-fa67835f384d
```

For more information about the `alternativeDistributionPackageVariants` endpoint, see [`Read information for an alternative distribution package variants`](https://developer.apple.com/documentation/AppStoreConnectAPI/GET-v1-alternativeDistributionPackageVariants-_id_).

Example response:

```json
{
  "data": {
    "type": "alternativeDistributionPackageVariants",
    "id": "219750db-80c2-4c75-aecc-fa67835f384d",
    "attributes": {
      "url": "<Apple_CDN_base_URL>/pre-thinned11331259484252926706.thinned.signed.dpkg.ipa?accessKey=<accesskey>",
      "urlExpirationDate": "2024-03-29T21:57:24-07:00",
      "alternativeDistributionKeyBlob": "<key_blob_base64_encoded_string>"
    }, ...
```

In the response, navigate to the `data.attributes.url`, which refers to an installable app in an encrypted form for the particular class of supported devices that Apple assigns this variant. The example `data.attributes.url` downloads the variant named `pre-thinned11331259484252926706.thinned.signed.dpkg.ipa`.

> **Note**: Although an app that resides on App Store Connect might contain binaries for multiple platforms, the alternative distribution package sent to the marketplace only contains variants for the platforms that MarketplaceKit supports in the target region (see [`Participating in alternative distribution for specific regions`](participating-in-alternative-distribution-for-specific-regions.md) for the device-support specifics). For example, a specific alternative distribution package contains variants for each supported device; it doesn’t contain watch variants.

The `alternativeDistributionKeyBlob` () has a unique value for each variant. The [`App License Delivery SDK`](https://developer.apple.com/documentation/AppLicenseDeliverySDK) requires the key blob during licensing requests. Store the key blob so your licensing service can use it to decrypt the license request payload coming from a device as required to generate an app license for the variant.

#### Download App Deltas

If someone already has a prior version of the app installed, the system selects an encrypted partial app bundle (a delta) to install rather than a variant. The deltas reside at the bottom of the manifest. The first delta in the example has a `publicId` of `ffbc52b6-f76b-4d51-9eff-5388bc6b7572`. To download the first delta, provide the `publicId` as the `id` path parameter of the `alternativeDistributionPackageDeltas` endpoint, as follows:

```None
GET https://api.appstoreconnect.apple.com/alternativeDistributionPackageDeltas/ffbc52b6-f76b-4d51-9eff-5388bc6b7572
```

For more information about the `alternativeDistributionPackageDeltas` endpoint, see [`Read information for alternative distribution package deltas`](https://developer.apple.com/documentation/AppStoreConnectAPI/GET-v1-alternativeDistributionPackageDeltas-_id_).

Example response:

```json
{
  "data": {
    "type": "alternativeDistributionPackageDeltas",
    "id": "ffbc52b6-f76b-4d51-9eff-5388bc6b7572",
    "attributes": {
      "url": "<Apple_CDN_base_URL>/mzpse.7668245576990498917.ipa?accessKey=<access_key>",
      "urlExpirationDate": "2024-03-29T21:25:47-07:00",
      "alternativeDistributionKeyBlob": "<key_blob_base64_encoded_string>"
    }, ...
```

> ❗ **Important**: When App Store Connect sends a new app version notification, it sends an app distribution package that includes the variants first, followed by another for deltas, if any are available for the app. Deltas arrive an unspecified amount of time after the app’s variants. You don’t need to wait for deltas to arrive before serving the new app to devices. Rather, App Store Connect sends variants first to expedite the app’s availability for customers.

#### Store the App Data at an Expected Path

Assemble all of the downloaded alternative distribution package assets into a folder structure, as follows:

```None
delta/
manifest.json
signature
variant/
```

You can serve the base URL of this file structure from any URL scheme you choose. When the device’s operating system attempts to download the app, it accesses the contents of this folder according to the `alternativeDistributionPackage` parameter that you provide to either:

- [`MarketplaceKitURIScheme`](marketplacekiturischeme.md) URLs, when serving your app marketplace
- The [`InstallMetadata`](installmetadata.md) initializer [`init(account:appleItemID:alternativeDistributionPackage:isUpdate:)`](installmetadata/init(account:appleitemid:alternativedistributionpackage:isupdate:).md), when serving apps that reside on your marketplace

Store the variants and deltas according to their `assetPath` in the manifest. For example, the following `assetPath` tells you how to name a specific variant and where to store it off the base URL:

```None
"assetPath": "variant/219750db-80c2-4c75-aecc-fa67835f384d.ipa",
```

When the device’s operating system attempts to download an app, it first reads the manifest to discover the contents of the alternative distribution package, then the operating system reads the signature to validate the variant or delta it chooses to install.

#### Validate the Assembled App Data

You can use the `dist_package_tool` utility on macOS 14.4 and later to verify the integrity of the alternative distribution packages you assemble. After downloading and assembling a complete alternative distribution package, you can validate it with the command:

```zsh
dist_package_tool validate <package-path> -v
```

This utility verifies the signature in the manifest and that the folders contain the correct assets that the manifest references.

The `-v` option provides verbose output. The following example represents the output of a valid alternative distribution package:

```None
Validating package: file:///Users/<name>/476476a1-6246-4782-98f1-9ca3819827ad/
Package has a valid signature.
All resources are present and valid.
```

If the alternative distribution package is incomplete, the output can identify problems. For example:

```None
Package contained added files.
    Added file: .DS_Store
Package contained missing files.
    Missing file: variant/7e11a118-ab90-4a52-9ca1-31362f5d108e.ipa
```

The tool’s return value indicates success or failure, so you can branch conditional logic using it in a script.

## See Also

- [Processing alternative app marketplace notifications](processing-alternative-marketplace-notifications.md)
  Manage the addition and removal of apps available on your alternative marketplace.
- [Installing your app from your website](installing-your-app-from-your-website.md)
  Manage the installation of an app that you develop and distribute through your website.
- [Installing apps from an alternative marketplace](installing-apps-from-an-alternative-marketplace.md)
  Manage the installation of apps that developers distribute from your marketplace app.
- [Supplying an install verification token](supplying-an-install-verification-token.md)
  Support the installation of alternative distribution apps by creating signed JSON web tokens.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/ingesting-an-alternative-distribution-package)*