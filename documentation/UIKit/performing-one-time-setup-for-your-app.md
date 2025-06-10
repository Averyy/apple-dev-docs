# Performing one-time setup for your app

**Framework**: UIKit

Ensure proper configuration of your app environment.

#### Overview

When the user launches your app for the first time, you might want to prepare your app environment by performing some one-time tasks. For example, you might want to:

- Download required data from your server.
- Copy document templates or modifiable data files from your app bundle to a writable directory.
- Configure default preferences for the user.
- Set up user accounts or gather other required data.

Perform any one-time tasks in your app delegate’s [`application(_:willFinishLaunchingWithOptions:)`](uiapplicationdelegate/application(_:willfinishlaunchingwithoptions:).md) or [`application(_:didFinishLaunchingWithOptions:)`](uiapplicationdelegate/application(_:didfinishlaunchingwithoptions:).md) method. Never block the app’s main thread for tasks that don’t require user input. Instead, start tasks asynchronously using a dispatch queue, and let them run in the background while your app finishes launching. For tasks that require user input, make all changes to your user interface in the [`application(_:didFinishLaunchingWithOptions:)`](uiapplicationdelegate/application(_:didfinishlaunchingwithoptions:).md) method.

##### Install Files in the Proper Locations

Your app has its own container directory for storing files, and you should always place app-specific files in the `~/Library` subdirectory. Specifically, store your files in the following `~/Library` subdirectories:

- `~/Library/Application Support/` — Store app-specific files that you want backed up with the user’s other content. (You can create custom subdirectories here as needed.) Use this directory for data files, configuration files, document templates, and so on.
- `~/Library/Caches/` — Store temporary data files that can be easily regenerated or downloaded.

To obtain a URL for one of the directories in your app’s container, use the [`urls(for:in:)`](https://developer.apple.com/documentation/Foundation/FileManager/urls(for:in:)) method of [`FileManager`](https://developer.apple.com/documentation/Foundation/FileManager).

```swift
let appSupportURL = FileManager.default.urls(for: 
      .applicationSupportDirectory, in: .userDomainMask)

let cachesURL = FileManager.default.urls(for: 
      .cachesDirectory, in: .userDomainMask)
```

Place any temporary files in your app’s `tmp/` directory. Temporary files might include compressed files that you intend to delete once their contents have been extracted and installed elsewhere. Retrieve the URL for your app’s temporary directory using the [`temporaryDirectory`](https://developer.apple.com/documentation/Foundation/FileManager/temporaryDirectory) method of [`FileManager`](https://developer.apple.com/documentation/Foundation/FileManager).

## See Also

- [About the app launch sequence](about-the-app-launch-sequence.md)
  Learn the order in which the system executes your code at app launch time.
- [Preserving your app’s UI across launches](preserving-your-app-s-ui-across-launches.md)
  Return your app to its previous state after the system terminates it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/performing-one-time-setup-for-your-app)*