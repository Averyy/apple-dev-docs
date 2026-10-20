# connectionTimeout

**Framework**: Core Bluetooth  
**Kind**: property  
**Role**: Type Property

The connection timed out.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var connectionTimeout: CBError.Code { get }
```

## See Also

### Error Codes
- [static var unknown: CBError.Code](./unknown.md)
  An unknown error occurred.
- [static var invalidParameters: CBError.Code](./invalidparameters.md)
  The specified parameters are invalid.
- [static var invalidHandle: CBError.Code](./invalidhandle.md)
  The specified attribute handle is invalid.
- [static var notConnected: CBError.Code](./notconnected.md)
  The device isn’t currently connected.
- [static var outOfSpace: CBError.Code](./outofspace.md)
  The device has run out of space to complete the intended operation.
- [static var operationCancelled: CBError.Code](./operationcancelled.md)
  The error represents a canceled operation.
- [static var peripheralDisconnected: CBError.Code](./peripheraldisconnected.md)
  The peripheral disconnected.
- [static var uuidNotAllowed: CBError.Code](./uuidnotallowed.md)
  The specified UUID isn’t permitted.
- [static var alreadyAdvertising: CBError.Code](./alreadyadvertising.md)
  The peripheral is already advertising.
- [static var connectionFailed: CBError.Code](./connectionfailed.md)
  The connection failed.
- [static var connectionLimitReached: CBError.Code](./connectionlimitreached.md)
  The device already has the maximum number of connections.
- [static var operationNotSupported: CBError.Code](./operationnotsupported.md)
  The operation isn’t supported.
- [static var unknownDevice: CBError.Code](./unknowndevice.md)
  The device is unknown.
- [static var unkownDevice: CBError.Code](./unkowndevice.md)
  A misspelled version of the unknown device error code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cberror-swift.struct/connectiontimeout)*