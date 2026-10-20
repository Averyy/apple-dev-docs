# AVMediaExtensionProperties

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

An object that describes a Media Extension.

**Availability**:
- macOS 15.0+

## Declaration

```swift
class AVMediaExtensionProperties
```

```objc
@interface AVMediaExtensionProperties : NSObject
```

## Topics

### Inspecting the extension
- [var extensionName: String](./avmediaextensionproperties/extensionname.md)
  The name of the Media Extension.
- [var containingBundleName: String](./avmediaextensionproperties/containingbundlename.md)
  The name of the containing app bundle.
- [var extensionIdentifier: String](./avmediaextensionproperties/extensionidentifier.md)
- [var extensionURL: URL](./avmediaextensionproperties/extensionurl.md)
  The file URL of the Media Extension bundle.
- [var containingBundleURL: URL](./avmediaextensionproperties/containingbundleurl.md)
  The file URL of the host application for the Media Extension.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Accessing Media Extension properties
- [var mediaExtensionProperties: AVMediaExtensionProperties?](./avurlasset/mediaextensionproperties.md)
  The properties of the media extension format reader that decodes the asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediaextensionproperties)*