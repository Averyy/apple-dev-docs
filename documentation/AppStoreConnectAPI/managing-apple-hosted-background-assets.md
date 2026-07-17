# Uploading and versioning Apple hosted background assets

**Framework**: App Store Connect API

Manage background assets for your App store apps.

#### Overview

Use the Background assets API to manage content that Apple hosts, so people can download that content outside your main app bundle, for apps distributed through the App Store. You can also update additional content without creating a new app version.

#### Create an Asset Pack Record

Once you create your asset pack, you can start configuring your Apple hosted background assets. Begin by using [`Create Asset Pack Record`](post-v1-backgroundassets.md).

In the request body, add the name of the asset pack as the `assetPackIdentifier` and add your app’s Apple ID In the relationships section.

This sample payload shows the structure of a [`Create Asset Pack Record`](post-v1-backgroundassets.md) request:

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

Next, you create a new version for your asset pack by using [`Create Asset Pack Version Record`](post-v1-backgroundassetversions.md). In the relationships section, use the ID of the asset pack that the previous API response returned.

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

This process is similar to uploading screenshots or app previews. First, you use [`Create a Reservation for an Asset Pack Upload`](post-v1-backgroundassetuploadfiles.md) with a payload like this, where you use the UUID from the response when using [`Create Asset Pack Version Record`](post-v1-backgroundassetversions.md):

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

You can optionally upload the asset manifest, to check its validity, by using [`Create a Reservation for an Asset Pack Upload`](post-v1-backgroundassetuploadfiles.md) before you upload your full asset pack. The system checks the validity of your manifest and returns an error, if there is an issue. Use a payload like this to verify your manifest:

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

Then, you upload the file with `PUT` request or requests, as necessary, which are included in the response of [`Create a Reservation for an Asset Pack Upload`](post-v1-backgroundassetuploadfiles.md).

#### Commit Your Asset Pack to Begin Processing

When you successfully upload your archive, you use [`Commit an Uploaded Asset Pack to a Background Asset Version`](patch-v1-backgroundassetuploadfiles-_id_.md) to commit the upload. After this call, your upload starts processing. Use a payload like this including the upload file ID:

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

After successful upload and internal testing, to test your asset pack version with a wider audience via external TestFlight, submit it to beta-asset pack review using [`Submit an app for beta review`](post-v1-betaappreviewsubmissions.md) or in App Store Connect.

#### Submit Your Asset Pack

When you are ready to publish the asset pack version to the App Store, you can submit it to review using [`Create a Review Submission`](post-v1-reviewsubmissions.md). You can submit the asset pack version by itself, with other asset packs, and as an app build with all files.

In this example, when the review submission state is `APPROVED`, version `1` of the asset pack is available to any version of your app live on the App Store.

#### Update and Version Your Asset Packs

Once you have live app versions and asset packs for TestFlight and the App Store, you can also  update either the app binary or the asset pack content.

- **Update app binary**: To update the app binary without changing any asset pack content, the new app binary needs to continue to work with the existing available asset packs. When you upload the new app build and it becomes ready for internal testing, it can download the internal testing versions of the existing asset pack. Similarly, when you submit the build for external TestFlight or the App Store, it continues to work with the asset pack versions that are live for external TestFlight and the App Store, respectively.
- **Update asset pack**: To switch out some contents in the Tutorial asset pack, you can upload a new version for the same asset pack. The system assigns a higher version number; in this case it is version 2. When the system processes version 2, it replaces version 1 for internal testing, but version 1 is still live for external TestFlight and the App Store. If you are satisfied with version 2, you can submit to review to replace version 1 in external TestFlight and the App Store. As a result, the devices downloads version 2 instead of version 1 when someone requests the tutorial asset pack and when the system updates the asset pack in the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/managing-apple-hosted-background-assets)*