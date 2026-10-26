# BAAppExtensionInfo

**Framework**: Background Assets  
**Kind**: class  
**Role**: Class

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

```objc
@interface BAAppExtensionInfo : NSObject
```

## Topics

### Getting the size of the remaining downloads
- [var restrictedEssentialDownloadSizeRemaining: Int?](./baappextensioninfo/restrictedessentialdownloadsizeremaining-5r8v0.md)
- [var restrictedDownloadSizeRemaining: Int?](./baappextensioninfo/restricteddownloadsizeremaining-4hea4.md)
- [restrictedEssentialDownloadSizeRemaining](./baappextensioninfo/restrictedessentialdownloadsizeremaining-76av8.md)
- [restrictedDownloadSizeRemaining](./baappextensioninfo/restricteddownloadsizeremaining-9itic.md)
### Initializers
- [init?(coder: NSCoder)](./baappextensioninfo/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Checking for asset updates
- [func downloads(for: BAContentRequest, manifestURL: URL, extensionInfo: BAAppExtensionInfo) -> Set<BADownload>](./badownloaderextension-qwaw/downloads%28for,manifesturl,extensioninfo%29.md)
- [enum BAContentRequest](./bacontentrequest.md)
  A type that indicates the purpose of a content download request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/baappextensioninfo)*