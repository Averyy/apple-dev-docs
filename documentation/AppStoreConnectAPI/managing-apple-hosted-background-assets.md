# Uploading and versioning Apple hosted background assets

**Framework**: App Store Connect API

Manage background assets for your App store apps.

#### Overview

Use the Background assets API to manage content that Apple hosts, so people can download that content outside your main app bundle, for apps distributed through the App Store. You can also update additional content without creating a new app version.

#### Create an Asset Pack Record

Once you create your asset pack, you can start configuring your Apple hosted background assets. Begin by using [`Create asset pack record`](post-v1-backgroundassets.md).

In the request body, add the name of the asset pack as the `assetPackIdentifier` and add your app’s Apple ID In the relationships section.

This sample payload shows the structure of a [`Create asset pack record`](post-v1-backgroundassets.md) request:

```json
{
  "data": {
    "type": "backgroundAssets",
    "attributes": {
      "assetPackIdentifier": "Tutorial"
    },
    "relationships": {
      "app": {
        "data": {
          "type": "apps",
          "id": "123456789"
        }
      }
    }
  }
}
```

This call’s response returns a UUID to your asset pack, which you can use in later API calls.

#### Create an Asset Pack Version Record

Next, you create a new version for your asset pack by using [`Create asset pack version record`](post-v1-backgroundassetversions.md). In the relationships section, use the ID of the asset pack that the previous API response returned.

> **Note**: This operation automatically increases the version number based on existing versions.

```json
{
  "data": {
    "type": "backgroundAssetVersions",
    "relationships": {
      "backgroundAsset": {
        "data": {
          "type": "backgroundAssets",
          "id": "1930fc63-0466-4a4a-bcfd-e0a3cc7a341a"
        }
      }
    }
  }
}
```

#### Upload an Asset Pack Archive

This process is similar to uploading screenshots or app previews. First, you use [`Create a reservation for an asset pack upload`](post-v1-backgroundassetuploadfiles.md) with a payload like this, where you use the UUID from the response when using [`Create asset pack version record`](post-v1-backgroundassetversions.md):

```json
{
  "data": {
    "type": "backgroundAssetUploadFiles",
    "attributes": {
      "assetType": "ASSET",
      "fileName": "Tutorial.aar",
      "fileSize": 59587
    },
    "relationships": {
      "backgroundAssetVersion": {
        "data": {
          "type": "backgroundAssetVersions",
          "id": "5934fd14-5123-gbgb-9090-01a2GYhg213z"
        }
      }
    }
  }
}
```

You can optionally upload the asset manifest, to check its validity, by using [`Create a reservation for an asset pack upload`](post-v1-backgroundassetuploadfiles.md) before you upload your full asset pack. The system checks the validity of your manifest and returns an error, if there is an issue. Use a payload like this to verify your manifest:

```json
{
  "data": {
    "type": "backgroundAssetUploadFiles",
    "attributes": {
      "assetType": "MANIFEST",
      "fileName": "Manifest.json",
      "fileSize": 9675
    },
    "relationships": {
      "backgroundAssetVersion": {
        "data": {
          "type": "backgroundAssetVersions",
          "id": "5934fd14-5123-gbgb-9090-01a2GYhg213z"
        }
      }
    }
  }
}
```

Then, you upload the file with `PUT` request or requests, as necessary, which are included in the response of [`Create a reservation for an asset pack upload`](post-v1-backgroundassetuploadfiles.md).

#### Commit Your Asset Pack to Begin Processing

When you successfully upload your archive, you use [`Commit an uploaded asset pack to a background asset version`](patch-v1-backgroundassetuploadfiles-_id_.md) to commit the upload. After this call, your upload starts processing. Use a payload like this including the upload file ID:

```json
{
  "data": {
    "type": "backgroundAssetUploadFiles",
    "id": "string",
    "attributes": {
      "uploaded": true
    }
  }
}
```

#### Test Your Asset Pack

When the asset pack version is successfully processed by the App Store, you see an Internal Beta Release resource created with the “Ready for testing” state in App Store Connect. This means the new version is ready for use in your app builds in internal TestFlight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/managing-apple-hosted-background-assets)*