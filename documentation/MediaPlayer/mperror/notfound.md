# notFound

**Framework**: Media Player  
**Kind**: property  
**Role**: Type Property

The operation fails because the system can’t find the requested identifier in the current storefront.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- macOS 10.14.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
static var notFound: MPError.Code { get }
```

## See Also

### Error code constants
- [static var cancelled: MPError.Code](./cancelled.md)
  The system cancels the requested operation before it completes.
- [static var cloudServiceCapabilityMissing: MPError.Code](./cloudservicecapabilitymissing.md)
  The operation can’t complete because iCloud services aren’t in an enabled state.
- [static var unknown: MPError.Code](./unknown.md)
  The requested operation can’t complete due to an unknown error.
- [static var networkConnectionFailed: MPError.Code](./networkconnectionfailed.md)
  The operation fails because the device can’t connect to the network.
- [static var notSupported: MPError.Code](./notsupported.md)
  The requested operation fails because the system doesn’t support it.
- [static var permissionDenied: MPError.Code](./permissiondenied.md)
  The operation can’t complete because the user doesn’t have permission for the request.
- [static var requestTimedOut: MPError.Code](./requesttimedout.md)
  The requested operation times out.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mperror/notfound)*