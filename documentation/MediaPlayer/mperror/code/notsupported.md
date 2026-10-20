# MPError.Code.notSupported

**Framework**: Media Player  
**Kind**: case  
**Role**: Case

An error that indicates the requested operation failed because the system doesn’t support it.

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
case notSupported
```

```c
MPErrorNotSupported
```

#### Discussion

An example of this is trying to add a media item to a smart playlist.

## See Also

### Error codes
- [MPError.Code.cancelled](./cancelled.md)
  An error that indicates the system canceled the requested operation before it completed.
- [MPError.Code.cloudServiceCapabilityMissing](./cloudservicecapabilitymissing.md)
  An error that indicates the operation can’t complete because iCloud services aren’t enabled.
- [MPError.Code.networkConnectionFailed](./networkconnectionfailed.md)
  An error that indicates the operation failed because the device can’t connect to the network.
- [MPError.Code.notFound](./notfound.md)
  An error that indicates the operation failed because the system can’t find the requested identifier in the current storefront.
- [MPError.Code.permissionDenied](./permissiondenied.md)
  An error that indicates the operation can’t complete because the user doesn’t have permission to execute the operation.
- [MPError.Code.requestTimedOut](./requesttimedout.md)
  An error that indicates the requested operation timed out.
- [MPError.Code.unknown](./unknown.md)
  An error that indicates the requested operation can’t complete due to an unknown error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mperror/code/notsupported)*