# BAContentRequest

**Framework**: Background Assets  
**Kind**: enum

A type that indicates the purpose of a content download request.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 18.4+
- visionOS 2.4+

## Declaration

```swift
enum BAContentRequest
```

## Topics

### Content request types
- [BAContentRequest.install](bacontentrequest/install.md)
  A content request resulting from the installation of the app.
- [BAContentRequest.periodic](bacontentrequest/periodic.md)
  A content request resulting from a system request for updated content within the app.
- [BAContentRequest.update](bacontentrequest/update.md)
  A content request resulting from an update of the app.
- [BAContentRequest.languageChange](bacontentrequest/languagechange.md)
  A content request resulting from someone changing the app’s preferred language.
### Initializers
- [init?(rawValue: Int)](bacontentrequest/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func downloads(for: BAContentRequest, manifestURL: URL, extensionInfo: BAAppExtensionInfo) -> Set<BADownload>](badownloaderextension-qwaw/downloads(for:manifesturl:extensioninfo:).md)
- [class BAAppExtensionInfo](baappextensioninfo.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/bacontentrequest)*