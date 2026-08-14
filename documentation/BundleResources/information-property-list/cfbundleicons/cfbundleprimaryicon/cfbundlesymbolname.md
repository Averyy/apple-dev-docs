# CFBundleSymbolName

**Framework**: Bundle Resources  
**Kind**: typealias

The name of the symbol to show in the action sheet, and in Finder’s sidebar on macOS.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+



**Type**: string

#### Discussion

The system associates the given symbol with your application. The system displays the symbol in the following locations:

- The action sheet displayed by an Action extension
- The Finder sidebar icons for file provider domains (macOS only)

To use a symbol from SF Symbols as the icon, set the value of `CFBundleSymbolName` to the symbol’s name. For example, to use the `flame.fill` symbol, configure the `Info.plist` entry as follows:

![Screenshot showing the Icon files portion of an Info.plist file containing a primary icon entry with CFBundleSymbolName inside of that. The value of CFBundleSymbolName is a string containing the value “flame.fill”.](/images/com.apple.bundleresources/media-3922506@2x.png)

The resulting item shown on the action sheet looks like this:

![A screenshot of an action sheet entry showing an icon using the flame.fill SF symbol. ](/images/com.apple.bundleresources/media-3922500@2x.png)

In the Finder sidebar, it looks like this:

![A screenshot of Finder, showing the flame.fill SF Symbol in the sidebar.](/images/com.apple.bundleresources/media-3922503@2x.png)

To create a custom symbol for your app, see [`Creating custom symbol images for your app`](https://developer.apple.com/documentation/uikit/creating-custom-symbol-images-for-your-app).


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/cfbundleicons/cfbundleprimaryicon/cfbundlesymbolname)*