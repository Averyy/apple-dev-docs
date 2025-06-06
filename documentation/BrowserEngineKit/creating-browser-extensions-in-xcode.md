# Creating browser extensions in Xcode

**Framework**: Browserenginekit

Configure your Xcode project to support your alternative browser engine.

#### Overview

Deliver your web browser as a browser app and a collection of extensions, described in [`Designing your browser architecture`](designing-your-browser-architecture.md). Create a separate target in your Xcode project for each of the three kinds of extension: web content extension, rendering extension, and networking extension.

##### Create Your Xcode Project

Create a new Xcode project for your browser app and extensions:

1. In Xcode, choose File > New Project.
2. Select the iOS App template, and click Next.
3. Give your project a name, and click Next.
4. Choose a location to save your project, and click Create.

##### Create Extension Targets in Xcode

Open your Xcode project, and follow these steps for each of the three extension types:

1. Select your Xcode project in the Project Navigator.
2. Click the Add (+) button at the bottom of the targets list.
3. Select the iOS Generic Extension template, and click Next.
4. Give the extension a name, and ensure your browser app is chosen for the Embed in Application setting.
5. Click Finish, then cancel the request to activate the extension target’s scheme.
6. Select the new target in the Project Editor.
7. Switch to the Info tab.
8. Expand the disclosure triangle next to `EXAppExtensionAttributes`.
9. Edit the value for `EXExtensionPointIdentifier`, and enter the appropriate value from the list based on the extension type:

##### Build for Pointer Authentication

Browser apps that include alternative browser engines must use the `arm64e` instruction set for all executables, including the extensions, in order to use the operating system’s pointer-authentication protection on devices that support it. Build your browser app as a universal binary that also supports the `arm64` instruction set to target iPad models that support alternative browser engines and don’t support `arm64e` instructions.

> ❗ **Important**:  You can develop and test your alternative browser engine using the `arm64` instruction set. To distribute your browser that includes an alternative browser engine, you need to support the `arm64e` instruction set.

To configure your Xcode targets to use the `arm64e` instruction set:

1. Select the Xcode project in the Project Navigator.
2. Select your target.
3. Open the Build Settings Tab.
4. Click the disclosure button to the left of the Architectures build setting.
5. Click the Add (+) button that appears when you move the mouse pointer over the Debug build configuration.
6. Change the SDK in the new row from “Any SDK” to “iOS”.
7. Enter the value `arm64e` for the build setting for the iOS SDK.
8. Repeat steps 5-7 for the Release build configuration.
9. Repeat steps 2-8 for each target in your browser app project.

Alternatively, if you use Xcode configuration files to manage build settings for your targets, add this line to your configuration file:

```other
ARCHS[sdk=iphoneos*]=arm64e
```

> ❗ **Important**:  Don’t build your target with the `arm64e` instruction set for Simulator destinations. Simulator for iPhone doesn’t support `arm64e` instructions.

If your Xcode workspace includes Swift Packages as dependencies for your targets, use workspace settings to build the packages using the `arm64e` instruction set. In Terminal, run these commands:

```zsh
% plutil -create xml1 MyWorkspace.xcworkspace/xcshareddata/WorkspaceSettings.xcsettings
% plutil -insert iOSPackagesShouldBuildARM64e -bool YES MyWorkspace.xcworkspace/xcshareddata/WorkspaceSettings.xcsettings
```

##### Adopt the Correct Entitlements

To act as a person’s web browser, your app uses the [`com.apple.developer.web-browser`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.web-browser) entitlement. For more information, see [`Preparing your app to be the default web browser`](https://developer.apple.com/documentation/Xcode/preparing-your-app-to-be-the-default-browser).

Additionally, to manage extensions for an alternative browser engine, your app declares the `com.apple.developer.web-browser-engine.host` entitlement with the value `true`.

> **Note**:  For a non-browser app that uses an alternative browser engine for in-app web browsing, add the `com.apple.developer.embedded-web-browser-engine` entitlement with the value `true`, instead of `com.apple.developer.web-browser`. Your non-browser app includes the alternative web browser engine in its own executable or as a dynamic library, uses only the `arm64` instruction set (not `arm64e`), and doesn’t include any web browser extensions. The alternative web browser engine in a non-browser app can’t use just-in-time (JIT) compilation. Add the following keys and values to your non-browser app’s `Info.plist` file: Add the value `embedded-web-browser-engine` to the `UIRequiredDeviceCapabilities` array in your app’s `Info.plist` file.

Each of your browser app’s extensions must use the appropriate entitlement from this list:

In each case, set the value for the entitlement to `true`. To use these entitlements, your host app and its extensions must be compiled for the `arm64e` instruction set, described in the “Build for pointer authentication” section, above.

For more information on adding entitlements to targets in Xcode, see [`Entitlements`](https://developer.apple.com/documentation/BundleResources/Entitlements).

Optionally, you may add the following entitlements:

- To allow just-in-time (JIT) compilation of web site scripts, your content extension uses the `com.apple.developer.cs.allow-jit` entitlement with the `true` value, and [`Extended Virtual Addressing Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.kernel.extended-virtual-addressing) with the `true` value. For more information, see [`Protecting code compiled just in time`](protecting-code-compiled-just-in-time.md). You can’t give this entitlement to your browser app, rendering extension, or networking extension.
- To transfer memory attribution between extensions, your content extension uses the `com.apple.developer.memory.transfer_accept` entitlement and your rendering extension uses the `com.apple.developer.memory.transfer_send` entitlement, both with the browser apps’ bundle identifier as the value. For more information, see [`Attributing memory to a content extension`](attributing-memory-to-a-content-extension.md).
- To restrict access to the system notification service in your web content extension, add the `com.apple.developer.web-browser-engine.restrict.notifyd` entitlement with the value `true`. For more information, see [`Limiting resource access in web content extensions`](limiting-resource-access-in-content-extensions.md)

> ❗ **Important**:  App Store Connect won’t accept your app if your non-browser app includes any of the entitlements for web browsers and their extensions described in this section, or you use the entitlements on other web browser components or with different values than those listed here. You must use all of the entitlements listed here only for the purposes described, for the relevant components of your browser app.

##### Target Devices with Required Capabilities

Add the string `web-browser-engine` to the `UIRequiredDeviceCapabilities` array in your app’s `Info.plist` file, to ensure that people can only download your app on devices that support browser apps with alternative browser engines. If your browser app only supports the `arm64e` instruction set, also add the string `arm64e` to the `UIRequiredDeviceCapabilities` array. For more information, see [`Required Device Capabilities`](https://developer.apple.comhttps://developer.apple.com/support/required-device-capabilities/).

##### Test Your Web Browser

Development of a web browser that uses an alternative browser engine can occur anywhere in the world. Xcode allows running development-signed or Ad-Hoc signed builds of the app on Simulator and all supported physical devices (iPhone and iPad).

## See Also

- [Extension lifecycle](extension-lifecycle.md)
  Launch, communicate with, and invalidate browser extensions.
- [Extension resources](extension-resources.md)
  Control access to files and memory in browser extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/creating-browser-extensions-in-xcode)*