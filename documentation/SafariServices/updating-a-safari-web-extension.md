# Updating a Safari web extension

**Framework**: Safari Services

Add new features and fix bugs in your Safari web extension using Xcode tools.

#### Overview

Update your Safari web extension by editing the generated files in your Xcode project to fix bugs, or by adding new source files to create new features.

If you prefer to use another editor for your source files, or if you want to preserve your existing development workflow for your converted web extension, edit your source files in an external source editor and use Xcode to update your extension in Safari.

Add new features with web extension APIs that work across browsers. For more information, see Mozilla’s [`Browser Extensions`](https://developer.apple.comhttps://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions) documentation. For more information about web extension API compatibility in Safari, see [`Assessing your Safari web extension’s browser compatibility`](assessing-your-safari-web-extension-s-browser-compatibility.md).

##### Share Your Extension in Safari in Ios

Safari supports web extensions in iOS 15 and later. To update your existing Xcode project with a macOS Safari web extension to support iOS, use the converter tool with the `--rebuild-project` option. For more information, see [`Add iOS to your existing Xcode project`](converting-a-web-extension-for-safari#Add-iOS-to-your-existing-Xcode-project.md).

##### Edit Existing Files in Xcode

While Xcode is primarily for native development, it has built-in support for editing web source-code documents, including HTML, CSS, JavaScript, and JSON. In the Xcode Project navigator, select and edit the files you want to customize.

For more information, see [`Editing source files in Xcode`](https://developer.apple.com/documentation/Xcode/creating-organizing-and-editing-source-files).

##### Edit Existing Files in an External Editor

If you have an existing development workflow for your web extension, you can use another source editor for your HTML, CSS, and JavaScript extension files in the Resources group. Your changes are visible in Xcode when you save changes to your files.

To see and test your web extension changes in Safari, you need Xcode to build and package your extension updates in the macOS containing app, or to build and deploy your iOS containing app to a simulator or device:

- For macOS, build and package your extension from Xcode by choosing Product > Build from the menu.
- For iOS, build and deploy your extension from Xcode by choosing Product > Run from the menu.

For more information, see [`Running your Safari web extension`](running-your-safari-web-extension.md).

If your alternative source editor supports custom build commands, configure it to use `xcodebuild` from the command line to build your extension’s macOS app container.

```other
xcodebuild -scheme HelloWorld\ \(macOS\) build
```

Run the `xcodebuild` command from the top directory of your Xcode project, and replace the `-scheme` parameter with the name of your Xcode project.

##### Add New Files to Your Safari Web Extension

Add new sources files for new features or to refactor existing features. To add a new source file to your web extension:

1. In the Xcode Project navigator, select the Resources folder.
2. Choose File > New > File, or Control-click the folder and choose New File.

Xcode presents a list of templates for new source files. To add a new HTML, CSS, JavaScript, or JSON file:

1. Select the iOS or macOS platform option from the top list of platform choices.
2. Scroll down to the Other section and select the Empty option. Click Next.
3. Name the file using the appropriate file extension for the file type you’re creating, and then click Create.

To add an existing source file or image file from another directory, see the section titled “Add Existing Source Files to Your Project” in [`Editing source files in Xcode`](https://developer.apple.com/documentation/Xcode/creating-organizing-and-editing-source-files).

> ❗ **Important**:  When you add new files, make sure that you add the files to the correct target. A Safari web extension has two targets per platform: an app for that platform, and the Safari web extension for that platform. If you want your files included in your Safari web extension, add them to both extension targets.

## See Also

- [Managing Safari web extension permissions](managing-safari-web-extension-permissions.md)
  Respect user privacy by setting appropriate permissions for your Safari web extension.
- [Previewing Metadata using Open Graph](previewing-metadata-using-open-graph.md)
  Build a Safari Extension that displays metadata using Open Graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/updating-a-safari-web-extension)*