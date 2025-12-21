# Downloading Apple-hosted asset packs

**Framework**: Background Assets

Configure your project and write the code to download asset packs hosted by Apple.

#### Overview

Let Apple host your app’s assets for you with your Apple Developer Program membership. Apple-Hosted Background Assets hosts up to 200GB of compressed assets and is available for apps on TestFlight or the App Store that use the Managed Background Assets features on all platforms except watchOS. You can use the service to host many different types of assets — such as texture files, machine learning models, Metal shader libraries, and videos — and update them independent of your app build. Background Assets provides a default implementation of a downloader extension that manages asset pack downloads, background updates, compression, and more on people’s systems that you can customize in your downloader extension code.

To create asset packs with a manifest file that the system manages, see [`Creating managed asset packs`](creating-managed-asset-packs.md). To test your asset packs before uploading them to App Store Connect, see [`Testing asset packs locally`](testing-asset-packs-locally.md).

##### Configure Your Project for Apple Hosted Background Assets

To use Apple-Hosted Background Assets, add a downloader extension target to your project, configure the App Groups capability for both the app and the extension targets, and add some Background Assets information property list keys.

Background Assets uses your app’s downloader extension to schedule downloads when your app isn’t running. Add a downloader extension that is preconfigured for Managed Background Assets to your Xcode project from a template. Choose New > Target and, in the sheet that appears, choose the Background Download template under Application Extension, and click Next. In the dialog, enter a target name, choose Apple-Hosted, Managed as the extension type, and click Finish. In the next dialog, click Activate to use the extension scheme Xcode creates.

Your app and your downloader extension target need to share an app group, which Background Assets uses to facilitate coordination between the two. Add each of the two targets to a shared app group in the Signing & Capabilities tab of the target editor in Xcode.

In the project editor, select the app target and click the Info tab. Then, add the following keys to the information property list file:

For apps that use Apple-Hosted Background Assets, omit all other Background Assets information property list keys from your project.

##### Customize Downloads

The default system implementation supports automatic downloads, background updates, compression, and more that you can customize. The system calls the [`shouldDownload(_:)`](manageddownloaderextension/shoulddownload(_:).md) method each time it downloads a new asset pack based on its download policy. Optionally, use this method to filter downloads at runtime.

![A screenshot of the project editor showing the download extension code created from the template. The source editor shows the default ](https://docs-assets.developer.apple.com/published/8a8fbc3013759ff2f111baa729d95af3/downloading-asset-packs-downloader-extension%402x.png)

If you don’t need to customize the download behavior for your asset packs beyond the download policies that you configure in the manifest files, remove the [`shouldDownload(_:)`](manageddownloaderextension/shoulddownload(_:).md) method implementation from your downloader-extension structure. Otherwise, if your asset packs have specific compatibility requirements, provide a custom implementation for the [`shouldDownload(_:)`](manageddownloaderextension/shoulddownload(_:).md) method.

##### Download Asset Packs From Your App

An instance of the [`AssetPack`](assetpack.md) structure represents an individual asset pack that’s available for download from the server, including metadata, such as its identifier that you set in the manifest file. To obtain an [`AssetPack`](assetpack.md) instance, call the [`assetPack(withID:)`](assetpackmanager/assetpack(withid:).md) method on the shared asset-pack manager:

```swift
let assetPack = try await AssetPackManager.shared.assetPack(withID: "Tutorial")
```

To ensure that the system downloads an asset pack, pass it to the [`ensureLocalAvailability(of:)`](assetpackmanager/ensurelocalavailability(of:).md) method:

```swift
try await AssetPackManager.shared.ensureLocalAvailability(of: assetPack)
```

If the system previously downloaded the asset pack, the [`ensureLocalAvailability(of:)`](assetpackmanager/ensurelocalavailability(of:).md) method returns quickly without downloading it again. For an asset pack with an essential or a prefetch download policy, the system may finish downloading the asset pack before you call this method. To download an asset pack with an on-demand download policy, this method initiates the download and waits for it to finish before returning. If this method returns without throwing an error, the asset pack is available to access locally.

> **Note**: Even for an asset pack with an essential download policy, network dropouts or other uncommon issues can prevent the system from downloading it until you call the [`ensureLocalAvailability(of:)`](assetpackmanager/ensurelocalavailability(of:).md) method.

##### Show Download Progress

When downloading asset packs in the foreground, display a progress indicator.

In Swift, you can await status updates on the asynchronous sequence that the [`statusUpdates(forAssetPackWithID:)`](assetpackmanager/statusupdates(forassetpackwithid:).md) method returns:

```swift
let statusUpdates = AssetPackManager.shared.statusUpdates(forAssetPackWithID: "Tutorial")
for await statusUpdate in statusUpdates {
	switch statusUpdate {
	case began(let assetPack): // …
	case paused(let assetPack): // …
	case downloading(let assetPack, let progress): // …
	case finished(let assetPack): // …
	case failed(let assetPack, let error): // …
	}
}
```

In Objective-C, you can create a class that conforms to the [`BAManagedAssetPackDownloadDelegate`](bamanagedassetpackdownloaddelegate.md) protocol:

```objc
@interface ManagedAssetPackDownloadDelegate : NSObject <BAManagedAssetPackDownloadDelegate>

@end

@implementation ManagedAssetPackDownloadDelegate

- (void)downloadOfAssetPackBegan:(BAAssetPack*)assetPack { /* … */ }

- (void)downloadOfAssetPackPaused:(BAAssetPack*)assetPack { /* … */ }

- (void)downloadOfAssetPack:(BAAssetPack*)assetPack hasProgress:(NSProgress*)progress { /* … */ }

- (void)downloadOfAssetPackFinished:(BAAssetPack*)assetPack { /* … */ }

- (void)downloadOfAssetPack:(BAAssetPack*)assetPack failedWithError:(NSError*)error { /* … */ }

@end
```

Then, set the shared asset-pack manager’s [`delegate`](baassetpackmanager/delegate.md) property to an instance of that class.

```objc
ManagedAssetPackDownloadDelegate* delegate = [[ManagedAssetPackDownloadDelegate alloc] init];
[[BAAssetPackManager sharedManager] setDelegate:delegate];
```

To cancel a download, call the [`cancel()`](https://developer.apple.com/documentation/Foundation/Progress/cancel()) method on any of the [`Progress`](https://developer.apple.com/documentation/Foundation/Progress) objects that you receive in the download status updates:

```swift
switch statusUpdate {
case downloading(let assetPack, let progress) where assetPack.id == "Tutorial":
    progress.cancel()
default: // …
}
```

##### Load Files in a Downloaded Asset Pack

To read the contents of an asset pack, call the [`contents(at:searchingInAssetPackWithID:options:)`](assetpackmanager/contents(at:searchinginassetpackwithid:options:).md) method on the shared asset-pack manager, passing a relative path from the root of the source repository — the folder where you ran the packaging tool command — to the file that you want to read:

```swift
let videoData = try AssetPackManager.shared.contents(at: "Videos/Introduction.m4v")
```

The system automatically merges all of your asset packs into a shared namespace, effectively reconstructing your asset root folder as if it were pasted on a person’s device. This way, you can access individual files without needing to know which asset pack they reside in.

By default, the [`contents(at:searchingInAssetPackWithID:options:)`](assetpackmanager/contents(at:searchinginassetpackwithid:options:).md) method returns a memory-mapped [`Data`](https://developer.apple.com/documentation/Foundation/Data) instance, which is suitable even for large asset files that take up a lot of space in memory. If you need low-level access to the file descriptor — for example, to read a file into memory procedurally — then you can use the [`descriptor(for:searchingInAssetPackWithID:)`](assetpackmanager/descriptor(for:searchinginassetpackwithid:).md) method instead:

```swift
let videoDescriptor = try AssetPackManager.shared.descriptor(for: "Videos/Introduction.m4v")
defer {
	do {
		try videoDescriptor.close()
	} catch {
		print("The file descriptor couldn’t be closed: \(error)")
	}
}
```

> ❗ **Important**: It’s your responsibility to close the file descriptor when you’re done using it.

The system tracks which asset packs you download and automatically keeps them up to date in the background. However, the system won’t automatically remove your asset packs while your app is installed. Therefore, when you are done with an asset pack, call the [`remove(assetPackWithID:)`](assetpackmanager/remove(assetpackwithid:).md) method on the shared asset-pack manager to free up storage space on the device. For example, remove the tutorial asset pack when a person finishes playing the tutorial:

```swift
try await AssetPackManager.shared.remove(assetPackWithID: "Tutorial")
```

To redownload an asset pack, call the [`ensureLocalAvailability(of:)`](assetpackmanager/ensurelocalavailability(of:).md) method again.

## See Also

- [Creating managed asset packs](creating-managed-asset-packs.md)
  Create managed asset packs, choose download options, and upload Apple-hosted asset packs  to App Store Connect.
- [Testing asset packs locally](testing-asset-packs-locally.md)
  Test your system-managed asset packs using a mock server on your Mac.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/downloading-apple-hosted-asset-packs)*