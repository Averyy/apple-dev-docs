# OBEXOpCodeSessionValues

**Framework**: IOBluetooth  
**Kind**: struct  
**Role**: Structure

Operation OpCode values for sessions. From the OBEX 1.3 specification.

**Availability**:
- macOS

## Declaration

```swift
struct OBEXOpCodeSessionValues
```

```c
enum OBEXOpCodeSessionValues : unsigned int;
```

## Topics

### Constants
- [var kOBEXOpCodeCloseSession: OBEXOpCodeSessionValues](./kobexopcodeclosesession.md)
- [var kOBEXOpCodeCreateSession: OBEXOpCodeSessionValues](./kobexopcodecreatesession.md)
- [var kOBEXOpCodeResumeSession: OBEXOpCodeSessionValues](./kobexopcoderesumesession.md)
- [var kOBEXOpCodeSetTimeout: OBEXOpCodeSessionValues](./kobexopcodesettimeout.md)
- [var kOBEXOpCodeSuspendSession: OBEXOpCodeSessionValues](./kobexopcodesuspendsession.md)
### Initializers
- [init(UInt32)](./obexopcodesessionvalues/init%28_%29.md)
- [init(rawValue: UInt32)](./obexopcodesessionvalues/init%28rawvalue%29.md)
### Instance Properties
- [var rawValue: UInt32](./obexopcodesessionvalues/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Data Types
- [typealias BluetoothAFHMode](./bluetoothafhmode.md)
- [typealias BluetoothAirMode](./bluetoothairmode.md)
- [typealias BluetoothAllowRoleSwitch](./bluetoothallowroleswitch.md)
- [typealias BluetoothAuthenticationRequirements](./bluetoothauthenticationrequirements.md)
- [struct BluetoothAuthenticationRequirementsValues](./bluetoothauthenticationrequirementsvalues.md)
- [typealias BluetoothClassOfDevice](./bluetoothclassofdevice.md)
- [typealias BluetoothClockOffset](./bluetoothclockoffset.md)
- [struct BluetoothCompanyIdentifers](./bluetoothcompanyidentifers.md)
- [typealias BluetoothConnectionHandle](./bluetoothconnectionhandle.md)
- [typealias BluetoothDeviceClassMajor](./bluetoothdeviceclassmajor.md)
- [typealias BluetoothDeviceClassMinor](./bluetoothdeviceclassminor.md)
- [typealias BluetoothDeviceName](./bluetoothdevicename.md)
- [typealias BluetoothEncryptionEnable](./bluetoothencryptionenable.md)
- [struct BluetoothFeatureBits](./bluetoothfeaturebits.md)
- [typealias BluetoothHCIACLDataByteCount](./bluetoothhciacldatabytecount.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexopcodesessionvalues)*