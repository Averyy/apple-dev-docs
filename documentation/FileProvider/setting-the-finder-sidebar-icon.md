# Setting the Finder Sidebar Icon

**Framework**: File Provider

Specify a standard or custom symbol as a sidebar icon.

#### Overview

To set the sidebar icon for your File Provider extension, set the [`CFBundleSymbolName`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleIcons/CFBundlePrimaryIcon/CFBundleSymbolName) key in the File Provider extension’s `Info.plist` file. The key takes the name of one of the SF Symbols. For the complete list of available symbols, see [`SF Symbols 3`](https://developer.apple.comhttps://developer.apple.com/sf-symbols/).

This image shows setting the sidebar icon to the `cloud.bolt.fill` symbol in the Plist editor.

![A screenshot of the File Provider extension’s Info.plist file. The Plist editor shows an Icon file (iOS 5) key that contains a Primary Icon key, which also contains the SF Symbol name key. ](https://docs-assets.developer.apple.com/published/bb6b976038df19008cb0692faf373041/media-3908721%402x.png)

Alternatively, you can open the `Info.plist` file as source code and edit the XML directly.

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleIcons</key>
    <dict>
        <key>CFBundlePrimaryIcon</key>
        <dict>
            <key>CFBundleSymbolName</key>
            <string>cloud.bolt.fill</string>
        </dict>
    </dict>
    <key>NSExtension</key>
    <dict>
        <key>NSExtensionFileProviderDocumentGroup</key>
        <string>group.com.examples.My-File-Provider-App</string>
        <key>NSExtensionFileProviderSupportsEnumeration</key>
        <true/>
        <key>NSExtensionPointIdentifier</key>
        <string>com.apple.fileprovider-nonui</string>
        <key>NSExtensionPrincipalClass</key>
        <string>$(PRODUCT_MODULE_NAME).FileProviderExtension</string>
    </dict>
</dict>
</plist>
```

To create a custom symbol for your app, see [`Creating custom symbol images for your app`](https://developer.apple.com/documentation/UIKit/creating-custom-symbol-images-for-your-app). To see a sample code project that uses a custom symbol, see [`Synchronizing files using file provider extensions`](synchronizing-files-using-file-provider-extensions.md).

## See Also

- [Synchronizing the File Provider Extension](synchronizing-the-file-provider-extension.md)
  Keep the local and remote copies of your File Provider extension’s content in sync.
- [Synchronizing files using file provider extensions](synchronizing-files-using-file-provider-extensions.md)
  Make remote files available in macOS and iOS, and synchronize their states by using file provider extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/setting-the-finder-sidebar-icon)*