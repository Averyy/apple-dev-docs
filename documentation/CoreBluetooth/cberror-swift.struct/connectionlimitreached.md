# connectionLimitReached

**Framework**: Core Bluetooth  
**Kind**: property

The device already has the maximum number of connections.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var connectionLimitReached: CBError.Code { get }
```

## See Also

- [static var unknown: CBError.Code](cberror-swift.struct/unknown.md)
  An unknown error occurred.
- [static var invalidParameters: CBError.Code](cberror-swift.struct/invalidparameters.md)
  The specified parameters are invalid.
- [static var invalidHandle: CBError.Code](cberror-swift.struct/invalidhandle.md)
  The specified attribute handle is invalid.
- [static var notConnected: CBError.Code](cberror-swift.struct/notconnected.md)
  The device isn’t currently connected.
- [static var outOfSpace: CBError.Code](cberror-swift.struct/outofspace.md)
  The device has run out of space to complete the intended operation.
- [static var operationCancelled: CBError.Code](cberror-swift.struct/operationcancelled.md)
  The error represents a canceled operation.
- [static var connectionTimeout: CBError.Code](cberror-swift.struct/connectiontimeout.md)
  The connection timed out.
- [static var peripheralDisconnected: CBError.Code](cberror-swift.struct/peripheraldisconnected.md)
  The peripheral disconnected.
- [static var uuidNotAllowed: CBError.Code](cberror-swift.struct/uuidnotallowed.md)
  The specified UUID isn’t permitted.
- [static var alreadyAdvertising: CBError.Code](cberror-swift.struct/alreadyadvertising.md)
  The peripheral is already advertising.
- [static var connectionFailed: CBError.Code](cberror-swift.struct/connectionfailed.md)
  The connection failed.
- [static var operationNotSupported: CBError.Code](cberror-swift.struct/operationnotsupported.md)
  The operation isn’t supported.
- [static var unknownDevice: CBError.Code](cberror-swift.struct/unknowndevice.md)
  The device is unknown.
- [static var unkownDevice: CBError.Code](cberror-swift.struct/unkowndevice.md)
  A misspelled version of the unknown device error code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cberror-swift.struct/connectionlimitreached)*