# LPError

**Framework**: Link Presentation  
**Kind**: struct

An error returned by the LinkPresentation framework.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
struct LPError
```

## Topics

### Error details
- [var errorCode: Int](lperror/errorcode.md)
  A code for the error.
- [var errorUserInfo: [String : Any]](lperror/erroruserinfo.md)
### Error domain
- [static var errorDomain: String](lperror/errordomain.md)
  The domain for the error.
- [let LPErrorDomain: String](lperrordomain.md)
  The domain for Link Presentation errors.
### Error codes
- [static var metadataFetchCancelled: LPError.Code](lperror/metadatafetchcancelled.md)
  An error indicating that the metadata fetch was canceled by the client.
- [static var metadataFetchFailed: LPError.Code](lperror/metadatafetchfailed.md)
  An error indicating that a metadata fetch failed.
- [static var metadataFetchTimedOut: LPError.Code](lperror/metadatafetchtimedout.md)
  An error indicating that the metadata fetch took longer than allowed.
- [static var unknown: LPError.Code](lperror/unknown.md)
- [LPError.Code](lperror/code.md)
  Possible error values that can be returned from LinkPresentation APIs.
### Type Properties
- [static var metadataFetchNotAllowed: LPError.Code](lperror/metadatafetchnotallowed.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [LPError.Code](lperror/code.md)
  Possible error values that can be returned from LinkPresentation APIs.
- [let LPErrorDomain: String](lperrordomain.md)
  The domain for Link Presentation errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/linkpresentation/lperror)*