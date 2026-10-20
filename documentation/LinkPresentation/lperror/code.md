# LPError.Code

**Framework**: Link Presentation  
**Kind**: enum  
**Role**: Enumeration

Possible error values that can be returned from LinkPresentation APIs.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
enum Code
```

```c
enum LPErrorCode : NSInteger;
```

## Topics

### Error cases
- [LPError.Code.metadataFetchCancelled](./code/metadatafetchcancelled.md)
  An error indicating that the metadata fetch was canceled by the client.
- [LPError.Code.metadataFetchFailed](./code/metadatafetchfailed.md)
  An error indicating that a metadata fetch failed.
- [LPError.Code.metadataFetchTimedOut](./code/metadatafetchtimedout.md)
  An error indicating that the metadata fetch took longer than allowed.
- [LPError.Code.unknown](./code/unknown.md)
  An unknown error.
### Enumeration Cases
- [LPError.Code.metadataFetchNotAllowed](./code/metadatafetchnotallowed.md)
  An error indicating that the metadata fetch was not allowed due to system policies.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Errors
- [struct LPError](../lperror.md)
  An error returned by the LinkPresentation framework.
- [let LPErrorDomain: String](../lperrordomain.md)
  The domain for Link Presentation errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/linkpresentation/lperror/code)*