# Packaging a web extension for Safari

**Framework**: Safari Services

Package your existing extension as a Safari web extension using Xcode’s command-line tool.

#### Overview

If you create a web extension that works in a browser other than Safari, you can deploy it in Safari by using the Safari web extension packager. The packager:

- Creates an Xcode project
- Configures the Xcode project with a macOS app or iOS app that installs the extension in Safari
- Configures a Safari web extension with your extension files in the Xcode project

Safari web extension packager is available as a command line tool which you can use alongside Xcode on a Mac, or as a web-based tool available in App Store Connect. To learn more about using the web-based tool, see [`Packaging and distributing Safari Web Extensions with App Store Connect`](packaging-and-distributing-safari-web-extensions-with-app-store-connect.md).

##### Run the Packager

To run the packager, open the Terminal app and run the `xcrun` command with the `safari-web-extension-packager` option, providing the path for your existing extension files.

```other
xcrun safari-web-extension-packager /path/to/extension
```

> **Note**: This tool used to be named `safari-web-extension-converter`.

If the packager needs more information, it asks you interactively, or you can provide the following command-line options:

> ❗ **Important**:  By default, the packager creates a reference in the Xcode project to the resources in the path you provide. As a result, changes you make to the original extension update your packaged Safari web extension and vice versa. If you prefer to keep your original and packaged extensions separate, use the `--copy-resources` option to make a copy of the original files.

New Xcode projects require you to select either the Swift or Objective-C language for native development. For your Safari web extension, you may not need to make any native customizations at all because your extension uses the JavaScript, HTML, and CSS you provide. If you are unsure of which language to use, select Swift.

If the packager runs interactively, it asks you to confirm your selections and gives you the opportunity to update them.

##### Review the Manifest Warnings

The packager generates and opens your new Xcode project. The packager reports any manifest keys that the current version of Safari doesn’t support.

```other
Warning: The following keys in your manifest.json are not supported by your 
current version of Safari. If these are critical to your extension, you 
should review your code to see if you need to make changes to support Safari:
downloads
offline_enabled

```

Review any reported exceptions, and see [`Assessing your Safari web extension’s browser compatibility`](assessing-your-safari-web-extension-s-browser-compatibility.md) for details on how to resolve them.

##### Build and Run Your Converted Safari Web Extension

To see your converted extension in Safari, follow the instructions in [`Running your Safari web extension`](running-your-safari-web-extension.md).

##### Add Ios to Your Existing Xcode Project

If you have an existing Xcode project with a macOS Safari web extension, and you want to add support for iOS to it, use the packager with the `--rebuild-project` option.

```other
xcrun safari-web-extension-packager --rebuild-project /path/to/myExtension/myExtension.xcodeproj
```

Provide the path to your current extension’s Xcode project file (including the `xcodeproj` file extension). The packager creates a new Xcode project with both macOS and iOS extensions from your existing project, and prints manifest warnings.

## See Also

- [Packaging and distributing Safari Web Extensions with App Store Connect](packaging-and-distributing-safari-web-extensions-with-app-store-connect.md)
  Upload and distribute Safari Web Extensions without using a Mac or Xcode.
- [Converting a Safari app extension to a Safari web extension](converting-a-safari-app-extension-to-a-safari-web-extension.md)
  Unify your web extensions and simplify development by sharing code with a Safari web extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/packaging-a-web-extension-for-safari)*