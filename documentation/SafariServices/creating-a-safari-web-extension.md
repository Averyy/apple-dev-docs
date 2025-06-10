# Creating a Safari web extension

**Framework**: Safari Services

Build a Safari web extension in Xcode.

#### Overview

To create a Safari web extension, you create an Xcode project using the Safari Extension App template. The project includes the Safari web extension as a macOS or iOS app extension that users can download from the App Store and install in Safari. The Xcode project includes default web extension files, such as the manifest, script files for a content page and background page, files for the toolbar pop-up menu, and folders for images and internationalization.

##### Create and Configure the Xcode Project

To create a new project in Xcode:

1. In Xcode, choose File > New > Project.
2. Select Multiplatform for your extension to work in both iOS and macOS, or select either the iOS or macOS platform for your extension to work for just that platform.
3. In the Application section, click the Safari Extension App template.
4. Click Next.

Xcode then displays the “Choose options for your new project” dialog, as in the following figure:

![A screenshot of the Choose options for your new project dialog in Xcode. The Product Name field is empty. The Team dropdown says Add account. The Organization Identifier is com.examples. The Bundle Identifier is com.examples.ProductName. The selected Type is Safari Web Extension. The selected Language is Swift. Include Tests is unchecked. The Next button is disabled.](https://docs-assets.developer.apple.com/published/7325ba512a450f94f1ab7bf1316d88b1/media-3744497%402x.png)

Provide information in the dialog for Xcode to configure your project:

1. In the Product Name field, enter a name for your extension. Xcode adds the name you enter here to the end of the extension’s bundle identifier.
2. From the Team pop-up menu, select your Apple Developer team profile. If you don’t have an account, you can update this information later in the project settings.
3. In the Organization Identifier field, enter a reverse DNS identifier for yourself or your organization (for example, com.example-organization). Xcode combines the organization identifier with the product name to construct the bundle identifier, which uniquely identifies your app in the App Store.
4. If you’re working in macOS, click the Type pop-up menu and select Safari Web Extension, if necessary.
5. Specify the Language as either Swift or Objective-C for code in the macOS app container for the web extension, or for messaging between the macOS app and the web extension.
6. If your Safari web extension relies solely on JavaScript, deselect the Include Tests checkbox. Select Include Tests if you include Swift or Objective-C code for messaging between the iOS or macOS app and the web extension, and you want to build unit tests or UI tests with XCTest.
7. Click Next and save the Xcode project to your Mac.

> **Note**:  XCTest doesn’t support unit tests for the JavaScript APIs that Safari web extensions use, or UI tests in Safari. Use XCTest if you build features in the iOS or macOS app container using Swift or Objective-C.

##### Review the Generated Web Extension Files and Folders

Xcode generates the project, provides default versions of the files you need to create your Safari web extension, and organizes them into the groups and folders illustrated in the following figure:

![A screenshot of the Xcode Project navigator showing the HelloWorld Extension group expanded, and the Resources group inside it expanded. The Resources group contains a _locales folder, an images folder, and the manifest.json, background.js, content.js, popup.html, popup.css, and popup.js files.](https://docs-assets.developer.apple.com/published/c0e10acaa64fce201a958108d9847e5d/media-3744500%402x.png)

The project contains default versions of web extension files in the Resources group:

> 💡 **Tip**:  To use your web extension in other browsers, repackage the files in the Resources group. The other files in the Xcode project are for the iOS or macOS app the system needs to use your web extension in Safari.

See [`Running your Safari web extension`](running-your-safari-web-extension.md) to try out your web extension in Safari.

##### Replace the Default Icons and Toolbar Icons

Xcode provides default icons and toolbar icons for your Safari web extension in the Resources > images folder. Safari uses the icon images in Preferences > Extensions to display in the list of icons that the user can select to see more detail about your extension. Safari uses the toolbar icon images when your extension has a pop-up webpage that the user can access from Safari’s toolbar.

Replace the default icons with icon images customized for your web extension. Use a PNG format, and provide 48-, 64-, 96-, 128-, 256-, and 512-pixel sizes.

Replace the toolbar icons with a toolbar image customized for your web extension. Use a PNG format, and provide 16-, 19-, 32-, and 38-pixel sizes.

Before you distribute your Safari web extension, create icons for the iOS and macOS apps that contain your extension, and add them to the AppIcon entries in the Assets.xcassets files for each platform. Your app icons should relate visually to your extension icon and toolbar icon. For more information about creating your app icons and detailed requirements, see [`Human Interface Guidelines > App icons`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/macos/icons-and-images/app-icon/).

## See Also

- [Modernizing Safari Web Extensions](modernizing-safari-web-extensions.md)
  Learn about enhancements to Safari Web Extensions.
- [Developing a Safari Web Extension](developing-a-safari-web-extension.md)
  Customize and enhance web pages by building a Safari web extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/creating-a-safari-web-extension)*