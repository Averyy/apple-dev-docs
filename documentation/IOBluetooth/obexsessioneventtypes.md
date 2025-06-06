# OBEXSessionEventTypes

**Framework**: IOBluetooth  
**Kind**: struct

Type identifiers for OBEX sessions.

**Availability**:
- macOS ?+

## Declaration

```swift
struct OBEXSessionEventTypes
```

#### Overview

When a new session event occurs, your selector (or C callback) will be given an OBEXSessionEvent pointer, and in it will be a ‘type’ field with one of the following types in it. Based on that type, you can then read the corresponding field in the union to get out interesting data for that event type. For example, if the type of an event is a ‘kOBEXSessionEventTypeConnectCommandResponseReceived’, you should look in the ‘OBEXConnectCommandResponseData’ part of the structure’s union to find more information pased to you in the event. Note that some you will never see, depending on the type of session you are using - a client or server. If you are a client (most likely case), you will never see the “Command” events, but instead you will only receive the “CommandResponse” events since you will be the issuer oft he commands, not the receiver of them. Both types of sessions will receive error type events.

## Topics

### Constants
- [var kOBEXSessionEventTypeAbortCommandReceived: OBEXSessionEventTypes](kobexsessioneventtypeabortcommandreceived.md)
- [var kOBEXSessionEventTypeAbortCommandResponseReceived: OBEXSessionEventTypes](kobexsessioneventtypeabortcommandresponsereceived.md)
- [var kOBEXSessionEventTypeConnectCommandReceived: OBEXSessionEventTypes](kobexsessioneventtypeconnectcommandreceived.md)
- [var kOBEXSessionEventTypeConnectCommandResponseReceived: OBEXSessionEventTypes](kobexsessioneventtypeconnectcommandresponsereceived.md)
- [var kOBEXSessionEventTypeDisconnectCommandReceived: OBEXSessionEventTypes](kobexsessioneventtypedisconnectcommandreceived.md)
- [var kOBEXSessionEventTypeDisconnectCommandResponseReceived: OBEXSessionEventTypes](kobexsessioneventtypedisconnectcommandresponsereceived.md)
- [var kOBEXSessionEventTypeError: OBEXSessionEventTypes](kobexsessioneventtypeerror.md)
- [var kOBEXSessionEventTypeGetCommandReceived: OBEXSessionEventTypes](kobexsessioneventtypegetcommandreceived.md)
- [var kOBEXSessionEventTypeGetCommandResponseReceived: OBEXSessionEventTypes](kobexsessioneventtypegetcommandresponsereceived.md)
- [var kOBEXSessionEventTypePutCommandReceived: OBEXSessionEventTypes](kobexsessioneventtypeputcommandreceived.md)
- [var kOBEXSessionEventTypePutCommandResponseReceived: OBEXSessionEventTypes](kobexsessioneventtypeputcommandresponsereceived.md)
- [var kOBEXSessionEventTypeSetPathCommandReceived: OBEXSessionEventTypes](kobexsessioneventtypesetpathcommandreceived.md)
- [var kOBEXSessionEventTypeSetPathCommandResponseReceived: OBEXSessionEventTypes](kobexsessioneventtypesetpathcommandresponsereceived.md)
### Initializers
- [init(UInt32)](obexsessioneventtypes/init(_:).md)
- [init(rawValue: UInt32)](obexsessioneventtypes/init(rawvalue:).md)
### Instance Properties
- [var rawValue: UInt32](obexsessioneventtypes/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [typealias BluetoothAFHMode](bluetoothafhmode.md)
- [typealias BluetoothAirMode](bluetoothairmode.md)
- [typealias BluetoothAllowRoleSwitch](bluetoothallowroleswitch.md)
- [typealias BluetoothAuthenticationRequirements](bluetoothauthenticationrequirements.md)
- [struct BluetoothAuthenticationRequirementsValues](bluetoothauthenticationrequirementsvalues.md)
- [typealias BluetoothClassOfDevice](bluetoothclassofdevice.md)
- [typealias BluetoothClockOffset](bluetoothclockoffset.md)
- [struct BluetoothCompanyIdentifers](bluetoothcompanyidentifers.md)
- [typealias BluetoothConnectionHandle](bluetoothconnectionhandle.md)
- [typealias BluetoothDeviceClassMajor](bluetoothdeviceclassmajor.md)
- [typealias BluetoothDeviceClassMinor](bluetoothdeviceclassminor.md)
- [typealias BluetoothDeviceName](bluetoothdevicename.md)
- [typealias BluetoothEncryptionEnable](bluetoothencryptionenable.md)
- [struct BluetoothFeatureBits](bluetoothfeaturebits.md)
- [typealias BluetoothHCIACLDataByteCount](bluetoothhciacldatabytecount.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexsessioneventtypes)*