# Converting a Safari app extension to a Safari web extension

**Framework**: Safari Services

Unify your web extensions and simplify development by sharing code with a Safari web extension.

#### Overview

Safari 14 and later in macOS and Safari 15 and later in iOS include support for Safari web extensions, which support the same JavaScript APIs that other browsers use in their extensions. If you have an extension for other browsers and a Safari app extension that offer the same features, you can replace your Safari app extension with a Safari web extension and share code.

> **Note**:  You must use the same developer account to create the Safari web extension that you used to create the Safari app extension.

To convert your Safari app extension to a Safari web extension:

- Add new Safari web extension target(s) for macOS, iOS, or both to your project. Update the target(s) to include the icons, assets, and files you need from your Safari app extension. Link code and assets that you want to use from your extension for other browsers in your new Safari web extension target. See [`Updating a Safari web extension`](updating-a-safari-web-extension.md) for more information.
- Update the JavaScript APIs from your Safari app extension that are specific to Safari to use the Safari web extensions JavaScript APIs. For more information, see [`Assessing your Safari web extension’s browser compatibility`](assessing-your-safari-web-extension-s-browser-compatibility.md).
- Update your `Info.plist` file to migrate your users (see details below).

##### Migrate Your Users to Your Safari Web Extension

To replace your Safari app extension with a Safari web extension, you just need to update your `Info.plist` file to migrate your users from one to the other.

Add the `SFSafariAppExtensionBundleIdentifiersToReplace` key to the `NSExtension` element inside your Safari web extension’s `Info.plist` file. Then specify the Safari app extensions that you want to replace when your Safari web extension loads. The value for this key is an array of strings, each of which is the bundle identifier for a Safari app extension that you want to replace.

When your app installs, the Safari web extension installs with it, and Safari removes the Safari app extensions you specified in the `Info.plist` file. If any of the Safari app extensions are in the enabled state when the installation occurs, Safari also enables the Safari web extension.

## See Also

- [Converting a web extension for Safari](converting-a-web-extension-for-safari.md)
  Convert your existing extension to a Safari web extension using Xcode’s command-line tool.
- [Packaging and distributing Safari Web Extensions with App Store Connect](packaging-and-distributing-safari-web-extensions-with-app-store-connect.md)
  Upload and distribute Safari Web Extensions without using a Mac or Xcode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/converting-a-safari-app-extension-to-a-safari-web-extension)*