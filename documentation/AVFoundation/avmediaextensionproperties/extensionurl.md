# extensionURL

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The file URL of the Media Extension bundle.

**Availability**:
- macOS 15.0+

## Declaration

```swift
var extensionURL: URL { get }
```

```objc
@property (nonatomic, readonly) NSURL * extensionURL;
```

## See Also

### Inspecting the extension
- [var extensionName: String](./extensionname.md)
  The name of the Media Extension.
- [var containingBundleName: String](./containingbundlename.md)
  The name of the containing app bundle.
- [var extensionIdentifier: String](./extensionidentifier.md)
- [var containingBundleURL: URL](./containingbundleurl.md)
  The file URL of the host application for the Media Extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediaextensionproperties/extensionurl)*