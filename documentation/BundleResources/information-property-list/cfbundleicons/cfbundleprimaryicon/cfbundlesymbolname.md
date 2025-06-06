# CFBundleSymbolName

**Framework**: Bundle Resources  
**Kind**: typealias

The name of the symbol to show in the action sheet, and in Finder’s sidebar on macOS.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

#### Discussion

The system associates the given symbol with your application. The system displays the symbol in the following locations:

- The action sheet displayed by an Action extension
- The Finder sidebar icons for file provider domains (macOS only)

To use a symbol from SF Symbols as the icon, set the value of `CFBundleSymbolName` to the symbol’s name. For example, to use the `flame.fill` symbol, configure the `Info.plist` entry as follows:

![Screenshot showing the Icon files portion of an Info.plist file containing a primary icon entry with CFBundleSymbolName inside of that. The value of CFBundleSymbolName is a string containing the value “flame.fill”.](https://docs-assets.developer.apple.com/published/e4d78c51f9e1de416e600af1a7f130c5/media-3922506%402x.png)

The resulting item shown on the action sheet looks like this:

![A screenshot of an action sheet entry showing an icon using the flame.fill SF symbol. ](https://docs-assets.developer.apple.com/published/f41a44e4f9c9c0a0c795419e053c51d5/media-3922500%402x.png)

In the Finder sidebar, it looks like this:

![A screenshot of Finder, showing the flame.fill SF Symbol in the sidebar.](https://docs-assets.developer.apple.com/published/8e0e0619fbcd52ede58c91e91651f10a/media-3922503%402x.png)

To create a custom symbol for your app, see [`Creating custom symbol images for your app`](https://developer.apple.com/documentation/UIKit/creating-custom-symbol-images-for-your-app).


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/cfbundleicons/cfbundleprimaryicon/cfbundlesymbolname)*