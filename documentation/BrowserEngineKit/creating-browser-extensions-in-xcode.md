# Creating browser extensions in Xcode

**Framework**: BrowserEngineKit

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

To act as a person’s web browser, your app requires the default-browser entitlement (see [`Preparing your app to be the default web browser`](https://developer.apple.com/documentation/Xcode/preparing-your-app-to-be-the-default-browser)), and the [`Web Browser Engine Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.web-browser-engine.host) that enables your app to separate core tasks of an alternative browser engine into dedicated extensions.

> **Note**:  Apps that aren’t browsers that use an alternative browser engine for in-app browsing need to add the [`Embedded Browser Engine Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.embedded-web-browser-engine) and [`Embedded Browser Engine Association Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.embedded-web-browser-engine.engine-association) rather than the default-browser entitlement and [`Web Browser Engine Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.web-browser-engine.host). In addition, an app that isn’t a browser needs to include: - The alternative browser engine in its own executable or as a dynamic library
- The [`BEEmbeddedWebBrowserEngine`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/BEEmbeddedWebBrowserEngine) and [`BEEmbeddedWebBrowserEngineVersion`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/BEEmbeddedWebBrowserEngineVersion) keys in its target properties
- `embedded-web-browser-engine` in its [`UIRequiredDeviceCapabilities`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIRequiredDeviceCapabilities) target property The embedded alternative browser only needs to use the `arm64` instruction set (not `arm64e`). It can’t include any web browser extensions or use just-in-time (JIT) compilation.

Each of your browser app’s extensions need to add the the following entitlements with a value of `true`:

To use the extension entitlements, compile your host app and extensions with the `arm64e` instruction set.

In Japan, browser apps are required to enable hardware memory tagging (see [`Enable Hardware Memory Tagging`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.hardened-process.checked-allocations)). To protect your users, Apple also strongly recommends that browser apps enable memory tagging in the European Union.

In addition, you can optionally add the following entitlements:

- To allow JIT compilation of website scripts, your content extension uses the [`Allow execution of JIT-compiled code entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.cs.allow-jit) entitlement with a value of `true`, and [`Extended Virtual Addressing Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.kernel.extended-virtual-addressing) with a value of `true`. For more information, see [`Protecting code compiled just in time`](protecting-code-compiled-just-in-time.md). You can’t give this entitlement to your browser app, rendering extension, or networking extension.
- To transfer memory attribution between extensions, your content extension uses the `com.apple.developer.memory.transfer_accept` entitlement, and your rendering extension uses the [`com.apple.developer.memory.transfer_send`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.memory.transfer_send) entitlement, both with the browser apps’ bundle identifier as the value. For more information, see [`Attributing memory to a content extension`](attributing-memory-to-a-content-extension.md).
- To restrict access to the system notification service in your web content extension, add the `com.apple.developer.web-browser-engine.restrict.notifyd` entitlement with the value `true`. For more information, see [`Limiting resource access in web content extensions`](limiting-resource-access-in-content-extensions.md).

For more information on adding entitlements to targets in Xcode, see [`Entitlements`](https://developer.apple.com/documentation/BundleResources/Entitlements).

> ❗ **Important**:  App Store Connect won’t accept your app if your non-browser app includes any of the entitlements for web browsers and their extensions described in this section, or you use the entitlements on other web browser components or with different values than those listed here. You must use all of the entitlements listed here only for the purposes described, for the relevant components of your browser app.

##### Target Devices with Required Capabilities

Add the string `web-browser-engine` to the [`UIRequiredDeviceCapabilities`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIRequiredDeviceCapabilities) array in your target’s properties, to ensure that people can only download your app on devices that support browser apps with alternative browser engines. If your browser app only supports the `arm64e` instruction set, also add `arm64e` to [`UIRequiredDeviceCapabilities`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIRequiredDeviceCapabilities).

For more information, see [`Required Device Capabilities`](https://developer.apple.comhttps://developer.apple.com/support/required-device-capabilities/).

##### Test Your Web Browser

Development of a web browser that uses an alternative browser engine can occur anywhere in the world. Xcode allows running development or Ad-Hoc signed builds of the app on Simulator but device support varies by region:

## See Also

- [Extension lifecycle](extension-lifecycle.md)
  Launch, communicate with, and invalidate browser extensions.
- [Extension resources](extension-resources.md)
  Control access to files and memory in browser extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/creating-browser-extensions-in-xcode)*