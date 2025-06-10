# CBError

**Framework**: Core Bluetooth  
**Kind**: struct

An error that Core Bluetooth returns during Bluetooth transactions.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
struct CBError
```

## Topics

### Error Codes
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
- [static var connectionLimitReached: CBError.Code](cberror-swift.struct/connectionlimitreached.md)
  The device already has the maximum number of connections.
- [static var operationNotSupported: CBError.Code](cberror-swift.struct/operationnotsupported.md)
  The operation isn’t supported.
- [static var unknownDevice: CBError.Code](cberror-swift.struct/unknowndevice.md)
  The device is unknown.
- [static var unkownDevice: CBError.Code](cberror-swift.struct/unkowndevice.md)
  A misspelled version of the unknown device error code.
### Type Properties
- [static var encryptionTimedOut: CBError.Code](cberror-swift.struct/encryptiontimedout.md)
- [static var leGattExceededBackgroundNotificationLimit: CBError.Code](cberror-swift.struct/legattexceededbackgroundnotificationlimit.md)
- [static var leGattNearBackgroundNotificationLimit: CBError.Code](cberror-swift.struct/legattnearbackgroundnotificationlimit.md)
- [static var peerRemovedPairingInformation: CBError.Code](cberror-swift.struct/peerremovedpairinginformation.md)
- [static var tooManyLEPairedDevices: CBError.Code](cberror-swift.struct/toomanylepaireddevices.md)
- [static var errorDomain: String](cberror-swift.struct/errordomain.md)
### Enumerations
- [CBError.Code](cberror-swift.struct/code.md)
  The codes for errors that Core Bluetooth returns during Bluetooth transactions.

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let CBErrorDomain: String](cberrordomain.md)
  The domain for Core Bluetooth errors.
- [CBError.Code](cberror-swift.struct/code.md)
  The codes for errors that Core Bluetooth returns during Bluetooth transactions.
- [struct CBATTError](cbatterror-swift.struct.md)
  An error that Core Bluetooth returns while using Attribute Protocol (ATT).
- [let CBATTErrorDomain: String](cbatterrordomain.md)
  The domain for Core Bluetooth ATT errors.
- [CBATTError.Code](cbatterror-swift.struct/code.md)
  The possible errors returned by a GATT server (a remote peripheral) during Bluetooth low energy ATT transactions.
- [struct CBATTError](cbatterror-swift.struct.md)
  An error that Core Bluetooth returns while using Attribute Protocol (ATT).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cberror-swift.struct)*