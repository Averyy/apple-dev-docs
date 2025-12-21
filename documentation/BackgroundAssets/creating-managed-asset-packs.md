# Creating managed asset packs

**Framework**: Background Assets

Create managed asset packs, choose download options, and upload Apple-hosted asset packs  to App Store Connect.

#### Overview

Before you can use Managed Background Assets, you need to create asset packs with a manifest file that specifies a download policy and provides other details. Then Managed Background Assets can automatically manage downloads, updates, compression, and more for your assets.

If you use Apple-Hosted Background Assets, you upload the asset packs to App Store Connect and update them there along with your app builds. Apple-Hosted Background Assets can host up to 200GB of compressed assets and is available for apps distributed through the App Store on all platforms except watchOS.

To add an Apple-Hosted Background Assets downloader extension to your app, see [`Downloading Apple-hosted asset packs`](downloading-apple-hosted-asset-packs.md). To test your asset packs before uploading them to App Store Connect, see [`Testing asset packs locally`](testing-asset-packs-locally.md).

##### Identify Asset Packs and Choose Download Policies

Group assets that you want to download together into asset packs. For example, create an asset pack that contains the textures, sound effects, and GPU shaders for a tutorial in your game. You can also include CPU and GPU executables in an asset pack, but not macOS executables.

Decide on a download policy for each asset pack, which the system uses to manage the assets on a device:

For example, choose `essential` for the tutorial asset pack so that people can run the tutorial immediately after installing your game without delay.

For limits on asset packs hosted by Apple, see [`Apple-hosted asset pack size limits`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/reference/apple-hosted-asset-pack-size-limits) in App Store Connect Help.

##### Create a Manifest File

Add a manifest file to your asset pack that specifies a download policy and other details. Create a JSON manifest file that contains information about your asset pack. After you install Xcode, run this `xcrun` command in Terminal to generate a manifest template:

```sh
xcrun ba-package template -o Manifest.json
```

Then, enter the information about your asset pack in the manifest file following the instructions in the comments:

1. Set the `assetPackID` key to an identifier that you use in your code to access the asset pack.
2. Set the `downloadPolicy` key to an object with a single key that’s either `essential`, `prefetch`, or `onDemand`. - For `essential` and `prefetch`, set the nested `installationEventTypes` key to an array of `firstInstallation`, `subsequentUpdate`, or both.
- For `onDemand`, leave the value as an empty object.
3. Add the paths to the files and folders that you want to include in the asset pack as file-selector objects in the `fileSelectors` array. Use the `file` key for individual assets and the `directory` key for folders that contain assets. All nested folders are also included.
4. Specify the platforms on which you want to make the asset pack available in the `platforms` array.

> ❗ **Important**: The paths that you include in the manifest file must be relative to the directory where you run the packaging tool command.

This example shows a manifest file for downloading assets for a game’s tutorial. The first time  people install this game, the system downloads the tutorial’s assets, and later, when people update the game, the system doesn’t download the tutorial’s assets again.

```json
{
    "assetPackID": "Tutorial",
    "downloadPolicy": {
        "essential": {
            "installationEventTypes": [
                "firstInstallation"
            ]
        }
    },
    "fileSelectors": [
        {
            "file": "Videos/Introduction.m4v"
        },
        // …
    ],
    "platforms": [ /* … */ ]
}
```

##### Archive Asset Packs

Next, use the packaging tool command to compress the assets, along with the manifest file, into an archive. Set the current directory in Terminal to the root of your source repository and pass the manifest file to the packaging tool command:

```sh
cd ~/Documents/The\ Coast/
xcrun ba-package Manifest.json -o Tutorial.aar
```

##### Manage Asset Packs in App Store Connect

For Apple-hosted asset packs, upload your asset packs — independent of your app builds — to App Store Connect using the  [`Transporter`](https://developer.apple.comhttps://apps.apple.com/us/app/transporter/id1450874784) app, the `altool` command-line tool, iTMSTransporter, or the [`App Store Connect API`](https://developer.apple.com/documentation/AppStoreConnectAPI). Later, when you want to test your app using TestFlight with external testers or to distribute it on the App Store, you can submit your asset packs for review.

For more information about managing your asset packs in App Store Connect, see [`Overview of Apple-hosted asset packs`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-asset-packs/overview-of-apple-hosted-asset-packs) in App Store Connect Help. To use web services, see [`Uploading and versioning Apple hosted background assets`](https://developer.apple.com/documentation/AppStoreConnectAPI/managing-apple-hosted-background-assets).

## See Also

- [Downloading Apple-hosted asset packs](downloading-apple-hosted-asset-packs.md)
  Configure your project and write the code to download asset packs hosted by Apple.
- [Testing asset packs locally](testing-asset-packs-locally.md)
  Test your system-managed asset packs using a mock server on your Mac.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/creating-managed-asset-packs)*