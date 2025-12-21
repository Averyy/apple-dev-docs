# extensionName

**Framework**: AVFoundation  
**Kind**: property

The name of the Media Extension.

**Availability**:
- macOS 15.0+

## Declaration

```swift
var extensionName: String { get }
```

#### Discussion

This value corresponds to the extension’s [`CFBundleDisplayName`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleDisplayName).

## See Also

- [var containingBundleName: String](avmediaextensionproperties/containingbundlename.md)
  The name of the containing app bundle.
- [var extensionIdentifier: String](avmediaextensionproperties/extensionidentifier.md)
- [var extensionURL: URL](avmediaextensionproperties/extensionurl.md)
  The file URL of the Media Extension bundle.
- [var containingBundleURL: URL](avmediaextensionproperties/containingbundleurl.md)
  The file URL of the host application for the Media Extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediaextensionproperties/extensionname)*