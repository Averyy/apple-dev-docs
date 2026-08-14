# BAAppExtensionInfo

**Framework**: Background Assets  
**Kind**: class

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 18.4+
- visionOS 2.4+

## Declaration

```swift
class BAAppExtensionInfo
```

## Topics

### Getting the size of the remaining downloads
- [var restrictedEssentialDownloadSizeRemaining: Int?](baappextensioninfo/restrictedessentialdownloadsizeremaining-5r8v0.md)
- [var restrictedDownloadSizeRemaining: Int?](baappextensioninfo/restricteddownloadsizeremaining-4hea4.md)
### Initializers
- [init?(coder: NSCoder)](baappextensioninfo/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func downloads(for: BAContentRequest, manifestURL: URL, extensionInfo: BAAppExtensionInfo) -> Set<BADownload>](badownloaderextension-qwaw/downloads(for:manifesturl:extensioninfo:).md)
- [enum BAContentRequest](bacontentrequest.md)
  A type that indicates the purpose of a content download request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/baappextensioninfo)*