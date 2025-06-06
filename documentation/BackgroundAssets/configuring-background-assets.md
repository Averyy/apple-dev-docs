# Configuring your Background Assets project

**Framework**: Background Assets

Edit your app and extension targets in your Xcode project to use Background Assets.

#### Overview

Before you can use the Background Assets framework, you need to add an extension target to your project, configure the App Groups capability for both the app and extension target, and add some Background Asset keys to the app’s information property list. Then the system notifies your extension when system events occur so that it can initiate downloads.

##### Add an App Extension to Your Project

Add an extension target to your new or existing Xcode project. Choose New > Target and, in the sheet that appears, choose the Background Download template under Application Extension, and click Next. In the next dialog that appears, click Activate to use the extension scheme Xcode creates.

If you don’t have an Xcode project for your app, first create one from an Application template under the platform you support, such as iOS or macOS. For more information, see [`Creating an Xcode project for an app`](https://developer.apple.com/documentation/Xcode/creating-an-xcode-project-for-an-app).

##### Add the App Groups Capability

Add your app and extension targets to the same app group so that they can communicate and share data.

Add the App Groups capability to both your app and extension target. For macOS apps, also add the App Sandbox capability to both targets. For more information, see [`Adding capabilities to your app`](https://developer.apple.com/documentation/Xcode/adding-capabilities-to-your-app).

Then, add both targets to the same app group. In the project editor, select the app target, and then add a unique ID for the group under App Groups on the Signing & Capabilities pane. Xcode automatically selects the new group ID. Select the extension target, then go to App Groups, click Refresh, and select the same group ID.

The app and extension are now in the same app group and can share the asset files. For more information on configuring app groups, and additional steps for macOS apps, see [`Configuring app groups`](https://developer.apple.com/documentation/Xcode/configuring-app-groups).

##### Add Required Information Property List Keys

Configure Background Assets for your app target by setting information property list keys. In the project editor, select the app target and click the Info tab. Then, add the following keys to the information property list file:

For more examples of these information property list keys, see the [`Downloading essential assets in the background`](downloading-essential-assets-in-the-background.md) sample code project. For more information on editing the information property list file, see [`Managing Your App’s Information Property List`](https://developer.apple.com/documentation/BundleResources/managing-your-app-s-information-property-list).

## See Also

- [BAManifestURL](../BundleResources/Information-Property-List/BAManifestURL.md)
  The location URL of the app’s manifest file that contains the names and sizes of assets.
- [BAInitialDownloadRestrictions](../BundleResources/Information-Property-List/BAInitialDownloadRestrictions.md)
  The restrictions that apply to the set of assets that download immediately after app installation.
- [BAEssentialMaxInstallSize](../BundleResources/Information-Property-List/BAEssentialMaxInstallSize.md)
  The combined, maximum size of the essential assets that the system downloads before it launches your app in bytes.
- [BAMaxInstallSize](../BundleResources/Information-Property-List/BAMaxInstallSize.md)
  The combined, maximum size, in bytes, of the non-essential assets that download immediately after app installation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/configuring-background-assets)*