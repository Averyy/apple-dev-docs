# CBError.Code

**Framework**: Core Bluetooth  
**Kind**: enum

The codes for errors that Core Bluetooth returns during Bluetooth transactions.

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
enum Code
```

## Topics

### Error Codes
- [CBError.Code.unknown](cberror-swift.struct/code/unknown.md)
  An unknown error occurred.
- [CBError.Code.invalidParameters](cberror-swift.struct/code/invalidparameters.md)
  The specified parameters are invalid.
- [CBError.Code.invalidHandle](cberror-swift.struct/code/invalidhandle.md)
  The specified attribute handle is invalid.
- [CBError.Code.notConnected](cberror-swift.struct/code/notconnected.md)
  The device isn’t currently connected.
- [CBError.Code.outOfSpace](cberror-swift.struct/code/outofspace.md)
  The device has run out of space to complete the intended operation.
- [CBError.Code.operationCancelled](cberror-swift.struct/code/operationcancelled.md)
  The error represents a canceled operation.
- [CBError.Code.connectionTimeout](cberror-swift.struct/code/connectiontimeout.md)
  The connection timed out.
- [CBError.Code.peripheralDisconnected](cberror-swift.struct/code/peripheraldisconnected.md)
  The peripheral disconnected.
- [CBError.Code.uuidNotAllowed](cberror-swift.struct/code/uuidnotallowed.md)
  The specified UUID isn’t permitted.
- [CBError.Code.alreadyAdvertising](cberror-swift.struct/code/alreadyadvertising.md)
  The peripheral is already advertising.
- [CBError.Code.connectionFailed](cberror-swift.struct/code/connectionfailed.md)
  The connection failed.
- [CBError.Code.connectionLimitReached](cberror-swift.struct/code/connectionlimitreached.md)
  The device already has the maximum number of connections.
- [CBError.Code.operationNotSupported](cberror-swift.struct/code/operationnotsupported.md)
  The operation isn’t supported.
- [static var unknownDevice: CBError.Code](cberror-swift.struct/code/unknowndevice.md)
  The device is unknown.
- [CBError.Code.unkownDevice](cberror-swift.struct/code/unkowndevice.md)
  A misspelled version of the unknown device error code.
### Enumeration Cases
- [CBError.Code.encryptionTimedOut](cberror-swift.struct/code/encryptiontimedout.md)
- [CBError.Code.leGattExceededBackgroundNotificationLimit](cberror-swift.struct/code/legattexceededbackgroundnotificationlimit.md)
- [CBError.Code.leGattNearBackgroundNotificationLimit](cberror-swift.struct/code/legattnearbackgroundnotificationlimit.md)
- [CBError.Code.peerRemovedPairingInformation](cberror-swift.struct/code/peerremovedpairinginformation.md)
- [CBError.Code.tooManyLEPairedDevices](cberror-swift.struct/code/toomanylepaireddevices.md)
### Initializers
- [init?(rawValue: Int)](cberror-swift.struct/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct CBError](cberror-swift.struct.md)
  An error that Core Bluetooth returns during Bluetooth transactions.
- [let CBErrorDomain: String](cberrordomain.md)
  The domain for Core Bluetooth errors.
- [struct CBATTError](cbatterror-swift.struct.md)
  An error that Core Bluetooth returns while using Attribute Protocol (ATT).
- [let CBATTErrorDomain: String](cbatterrordomain.md)
  The domain for Core Bluetooth ATT errors.
- [CBATTError.Code](cbatterror-swift.struct/code.md)
  The possible errors returned by a GATT server (a remote peripheral) during Bluetooth low energy ATT transactions.
- [struct CBATTError](cbatterror-swift.struct.md)
  An error that Core Bluetooth returns while using Attribute Protocol (ATT).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cberror-swift.struct/code)*