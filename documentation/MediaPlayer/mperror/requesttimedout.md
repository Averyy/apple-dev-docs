# requestTimedOut

**Framework**: Media Player  
**Kind**: property

The requested operation times out.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- macOS 10.14.2+
- tvOS 10.3+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
static var requestTimedOut: MPError.Code { get }
```

## See Also

- [static var cancelled: MPError.Code](mperror/cancelled.md)
  The system cancels the requested operation before it completes.
- [static var cloudServiceCapabilityMissing: MPError.Code](mperror/cloudservicecapabilitymissing.md)
  The operation can’t complete because iCloud services aren’t in an enabled state.
- [static var unknown: MPError.Code](mperror/unknown.md)
  The requested operation can’t complete due to an unknown error.
- [static var networkConnectionFailed: MPError.Code](mperror/networkconnectionfailed.md)
  The operation fails because the device can’t connect to the network.
- [static var notFound: MPError.Code](mperror/notfound.md)
  The operation fails because the system can’t find the requested identifier in the current storefront.
- [static var notSupported: MPError.Code](mperror/notsupported.md)
  The requested operation fails because the system doesn’t support it.
- [static var permissionDenied: MPError.Code](mperror/permissiondenied.md)
  The operation can’t complete because the user doesn’t have permission for the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mperror/requesttimedout)*