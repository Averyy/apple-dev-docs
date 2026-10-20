# CBError.Code

**Framework**: Core Bluetooth  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum CBError : NSInteger;
```

## Topics

### Error Codes
- [CBError.Code.unknown](./code/unknown.md)
  An unknown error occurred.
- [CBError.Code.invalidParameters](./code/invalidparameters.md)
  The specified parameters are invalid.
- [CBError.Code.invalidHandle](./code/invalidhandle.md)
  The specified attribute handle is invalid.
- [CBError.Code.notConnected](./code/notconnected.md)
  The device isn’t currently connected.
- [CBError.Code.outOfSpace](./code/outofspace.md)
  The device has run out of space to complete the intended operation.
- [CBError.Code.operationCancelled](./code/operationcancelled.md)
  The error represents a canceled operation.
- [CBError.Code.connectionTimeout](./code/connectiontimeout.md)
  The connection timed out.
- [CBError.Code.peripheralDisconnected](./code/peripheraldisconnected.md)
  The peripheral disconnected.
- [CBError.Code.uuidNotAllowed](./code/uuidnotallowed.md)
  The specified UUID isn’t permitted.
- [CBError.Code.alreadyAdvertising](./code/alreadyadvertising.md)
  The peripheral is already advertising.
- [CBError.Code.connectionFailed](./code/connectionfailed.md)
  The connection failed.
- [CBError.Code.connectionLimitReached](./code/connectionlimitreached.md)
  The device already has the maximum number of connections.
- [CBError.Code.operationNotSupported](./code/operationnotsupported.md)
  The operation isn’t supported.
- [static var unknownDevice: CBError.Code](./code/unknowndevice.md)
  The device is unknown.
- [CBError.Code.unkownDevice](./code/unkowndevice.md)
  A misspelled version of the unknown device error code.
### Enumeration Cases
- [CBError.Code.channelSoundingConfigurationFailed](./code/channelsoundingconfigurationfailed.md)
- [CBError.Code.channelSoundingProcedureFailed](./code/channelsoundingprocedurefailed.md)
- [CBError.Code.encryptionTimedOut](./code/encryptiontimedout.md)
- [CBError.Code.leGattExceededBackgroundNotificationLimit](./code/legattexceededbackgroundnotificationlimit.md)
- [CBError.Code.leGattNearBackgroundNotificationLimit](./code/legattnearbackgroundnotificationlimit.md)
- [CBError.Code.peerRemovedPairingInformation](./code/peerremovedpairinginformation.md)
- [CBError.Code.tooManyLEPairedDevices](./code/toomanylepaireddevices.md)
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
- [struct CBError](../cberror-swift.struct.md)
  An error that Core Bluetooth returns during Bluetooth transactions.
- [let CBErrorDomain: String](../cberrordomain.md)
  The domain for Core Bluetooth errors.
- [struct CBATTError](../cbatterror-swift.struct.md)
  An error that Core Bluetooth returns while using Attribute Protocol (ATT).
- [let CBATTErrorDomain: String](../cbatterrordomain.md)
  The domain for Core Bluetooth ATT errors.
- [CBATTError.Code](../cbatterror-swift.struct/code.md)
  The possible errors returned by a GATT server (a remote peripheral) during Bluetooth low energy ATT transactions.
- [struct CBATTError](../cbatterror-swift.struct.md)
  An error that Core Bluetooth returns while using Attribute Protocol (ATT).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cberror-swift.struct/code)*