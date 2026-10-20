# extensionName

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The name of the Media Extension.

**Availability**:
- macOS 15.0+

## Declaration

```swift
var extensionName: String { get }
```

```objc
@property (nonatomic, readonly) NSString * extensionName;
```

#### Discussion

This value corresponds to the extension’s [`CFBundleDisplayName`](../../BundleResources/information-property-list/cfbundledisplayname.md).

## See Also

### Inspecting the extension
- [var containingBundleName: String](./containingbundlename.md)
  The name of the containing app bundle.
- [var extensionIdentifier: String](./extensionidentifier.md)
- [var extensionURL: URL](./extensionurl.md)
  The file URL of the Media Extension bundle.
- [var containingBundleURL: URL](./containingbundleurl.md)
  The file URL of the host application for the Media Extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediaextensionproperties/extensionname)*