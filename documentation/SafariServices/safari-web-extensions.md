# Safari web extensions

**Framework**: Safari Services

Create web extensions that work in Safari and other browsers.

#### Overview

A Safari web extension adds custom functionality to Safari using JavaScript APIs and common file formats from extensions for Google Chrome, Mozilla Firefox, and Microsoft Edge browsers. While [`Safari app extensions`](safari-app-extensions.md) are useful for sharing code between your native macOS app and Safari, you build Safari web extensions primarily on JavaScript, HTML, and CSS, and can repackage them to work in other browsers. You can also use Safari web extensions in [`Mac web apps`](https://developer.apple.comhttps://support.apple.com/en-us/104996).

> ❗ **Important**:  You implement a Safari web extension as a macOS, visionOS, or iOS app extension to provide a safe and secure distribution and usage model. You can distribute a Safari web extension with a Mac app, a visionOS app, an iOS app, or a Mac app created using [`Mac Catalyst`](https://developer.apple.com/documentation/UIKit/mac-catalyst). Use [`Xcode`](https://developer.apple.comhttps://developer.apple.com/xcode/) to package your extension for testing and distribution, and join the [`Apple Developer Program`](https://developer.apple.comhttps://developer.apple.com/programs/) to distribute Safari web extensions. For more information, see [`Distributing your Safari web extension`](distributing-your-safari-web-extension.md).

To get started with creating a Safari web extension, use one of the following options:

- Package your existing extension into a Safari web extension, so you can use it in Safari in macOS, visionOS, and iOS and distribute it. Xcode includes a command-line tool to simplify this process.
- Build a new Safari web extension in Xcode using the built-in template. You can then repackage the extension files for deployment in other browsers.
- Temporarily install your web extension in Safari for testing without packaging it or setting up an Xcode project. For more information, see [`Temporarily install a web extension folder in macOS Safari`](running-your-safari-web-extension#Temporarily-install-a-web-extension-folder-in-macOS-Safari.md).

Learn more about the capabilities of web extensions and the APIs you use to build them in Mozilla’s [`Browser Extensions`](https://developer.apple.comhttps://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions) documentation.

Safari web extensions are available in macOS with Safari 14 and later, visionOS 1 and later, and iOS 15 and later. Safari web extensions are available in Mac web apps in macOS 15 and later.

## Topics

### New extensions
- [Creating a Safari web extension](creating-a-safari-web-extension.md)
  Build a Safari web extension in Xcode.
- [Modernizing Safari Web Extensions](modernizing-safari-web-extensions.md)
  Learn about enhancements to Safari Web Extensions.
- [Developing a Safari Web Extension](developing-a-safari-web-extension.md)
  Customize and enhance web pages by building a Safari web extension.
### Extension conversions and packaging
- [Packaging a web extension for Safari](packaging-a-web-extension-for-safari.md)
  Package your existing extension as a Safari web extension using Xcode’s command-line tool.
- [Packaging and distributing Safari Web Extensions with App Store Connect](packaging-and-distributing-safari-web-extensions-with-app-store-connect.md)
  Upload and distribute Safari Web Extensions without using a Mac or Xcode.
- [Converting a Safari app extension to a Safari web extension](converting-a-safari-app-extension-to-a-safari-web-extension.md)
  Unify your web extensions and simplify development by sharing code with a Safari web extension.
### Extension updates
- [Updating a Safari web extension](updating-a-safari-web-extension.md)
  Add new features and fix bugs in your Safari web extension using Xcode tools.
- [Managing Safari web extension permissions](managing-safari-web-extension-permissions.md)
  Respect user privacy by setting appropriate permissions for your Safari web extension.
- [Previewing Metadata using Open Graph](previewing-metadata-using-open-graph.md)
  Build a Safari Extension that displays metadata using Open Graph.
### Checking extension state
- [class SFSafariExtensionManager](sfsafariextensionmanager.md)
  A class that your app uses to find out the current state of a Safari extension.
- [class SFSafariExtensionState](sfsafariextensionstate.md)
  The state of a Safari extension.
### Messaging
- [Messaging between the app and JavaScript in a Safari web extension](messaging-between-the-app-and-javascript-in-a-safari-web-extension.md)
  Communicate about events and share data between the containing app and JavaScript by using native messaging and app groups.
- [let SFExtensionMessageKey: String](sfextensionmessagekey.md)
  A string the system uses as a key in a user info dictionary to identify a message.
- [let SFExtensionProfileKey: String](sfextensionprofilekey.md)
  A string the system uses as a key in a user info dictionary to identify a profile identifier.
- [Messaging a Web Extension’s Native App](messaging-a-web-extension-s-native-app.md)
  Communicate between your Safari web extension and its containing app.
- [Messaging between a webpage and your Safari web extension](messaging-between-a-webpage-and-your-safari-web-extension.md)
  Configure your extension to enable messaging from webpages, and then update your extension to handle messages.
### Blocking content
- [Blocking content with your Safari web extension](blocking-content-with-your-safari-web-extension.md)
  Build content blocking with declarative net request into your Safari web extension.
- [Adopting Declarative Content Blocking in Safari Web Extensions](adopting-declarative-content-blocking-in-safari-web-extensions.md)
  Block web content with your web extension using the declarative net request API.
### Adding Web Inspector tools
- [Adding a web development tool to Safari Web Inspector](adding-a-web-development-tool-to-safari-web-inspector.md)
  Expand the built-in Safari Web Inspector to include your custom tool, augmenting developers’ options for inspecting, testing, and debugging webpages.
- [Creating Safari Web Inspector extensions](creating-safari-web-inspector-extensions.md)
  Learn how to make custom Safari Web Inspector extensions.
### Extension improvements
- [Optimizing your web extension for Safari](optimizing-your-web-extension-for-safari.md)
  Support Dark Mode, reduce memory and power usage, and ensure feature compatibility to improve your web extension experience in Safari and web apps.
- [Adopting New Safari Web Extension APIs](adopting-new-safari-web-extension-apis.md)
  Improve your web extension in Safari with a non-persistent background page and new tab-override customization.
- [Syncing Safari web extensions across devices and platforms](syncing-safari-web-extensions-across-devices-and-platforms.md)
  Let users install your extension on one device and then use and manage the extension on all their other iOS and macOS devices.
- [Assessing your Safari web extension’s browser compatibility](assessing-your-safari-web-extension-s-browser-compatibility.md)
  Review your Safari web extension implementation plan, manifest keys, and JavaScript API usage for compatibility with other browsers.
- [Troubleshooting your Safari web extension](troubleshooting-your-safari-web-extension.md)
  Use developer resources to investigate and resolve common problems with Safari web extensions.
### Installation and distribution
- [Running your Safari web extension](running-your-safari-web-extension.md)
  Install and update your extension in Safari as you make changes in development.
- [Distributing your Safari web extension](distributing-your-safari-web-extension.md)
  Get feedback on your extension from beta testers, then share your extension with customers in the App Store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/safari-web-extensions)*