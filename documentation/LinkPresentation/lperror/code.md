# LPError.Code

**Framework**: Link Presentation  
**Kind**: enum

Possible error values that can be returned from LinkPresentation APIs.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
enum Code
```

## Topics

### Error cases
- [LPError.Code.metadataFetchCancelled](lperror/code/metadatafetchcancelled.md)
  An error indicating that the metadata fetch was canceled by the client.
- [LPError.Code.metadataFetchFailed](lperror/code/metadatafetchfailed.md)
  An error indicating that a metadata fetch failed.
- [LPError.Code.metadataFetchTimedOut](lperror/code/metadatafetchtimedout.md)
  An error indicating that the metadata fetch took longer than allowed.
- [LPError.Code.unknown](lperror/code/unknown.md)
  An unknown error.
### Enumeration Cases
- [LPError.Code.metadataFetchNotAllowed](lperror/code/metadatafetchnotallowed.md)
  An error indicating that the metadata fetch was not allowed due to system policies.
### Initializers
- [init?(rawValue: Int)](lperror/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct LPError](lperror.md)
  An error returned by the LinkPresentation framework.
- [let LPErrorDomain: String](lperrordomain.md)
  The domain for Link Presentation errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/linkpresentation/lperror/code)*