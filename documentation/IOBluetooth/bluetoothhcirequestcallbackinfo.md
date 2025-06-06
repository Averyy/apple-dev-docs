# BluetoothHCIRequestCallbackInfo

**Framework**: IOBluetooth  
**Kind**: struct

**Availability**:
- macOS ?+

## Declaration

```swift
struct BluetoothHCIRequestCallbackInfo
```

## Topics

### Initializers
- [init()](bluetoothhcirequestcallbackinfo/init.md)
- [init(userCallback: mach_vm_address_t, userRefCon: mach_vm_address_t, internalRefCon: mach_vm_address_t, asyncIDRefCon: mach_vm_address_t, reserved: mach_vm_address_t)](bluetoothhcirequestcallbackinfo/init(usercallback:userrefcon:internalrefcon:asyncidrefcon:reserved:).md)
### Instance Properties
- [var asyncIDRefCon: mach_vm_address_t](bluetoothhcirequestcallbackinfo/asyncidrefcon.md)
- [var internalRefCon: mach_vm_address_t](bluetoothhcirequestcallbackinfo/internalrefcon.md)
- [var reserved: mach_vm_address_t](bluetoothhcirequestcallbackinfo/reserved.md)
- [var userCallback: mach_vm_address_t](bluetoothhcirequestcallbackinfo/usercallback.md)
- [var userRefCon: mach_vm_address_t](bluetoothhcirequestcallbackinfo/userrefcon.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct BluetoothAFHHostChannelClassification](bluetoothafhhostchannelclassification.md)
- [struct BluetoothAFHResults](bluetoothafhresults.md)
- [struct BluetoothAMPCommandRejectReason](bluetoothampcommandrejectreason.md)
- [struct BluetoothAMPCreatePhysicalLinkResponseStatus](bluetoothampcreatephysicallinkresponsestatus.md)
- [struct BluetoothAMPDisconnectPhysicalLinkResponseStatus](bluetoothampdisconnectphysicallinkresponsestatus.md)
- [struct BluetoothAMPDiscoverResponseControllerStatus](bluetoothampdiscoverresponsecontrollerstatus.md)
- [struct BluetoothAMPGetAssocResponseStatus](bluetoothampgetassocresponsestatus.md)
- [struct BluetoothAMPGetInfoResponseStatus](bluetoothampgetinforesponsestatus.md)
- [struct BluetoothAMPManagerCode](bluetoothampmanagercode.md)
- [struct BluetoothAuthenticationRequirementsValues](bluetoothauthenticationrequirementsvalues.md)
- [struct BluetoothCompanyIdentifers](bluetoothcompanyidentifers.md)
- [struct BluetoothDeviceAddress](bluetoothdeviceaddress.md)
- [struct BluetoothEnhancedSynchronousConnectionInfo](bluetoothenhancedsynchronousconnectioninfo.md)
- [struct BluetoothEventFilterCondition](bluetootheventfiltercondition.md)
- [struct BluetoothFeatureBits](bluetoothfeaturebits.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/bluetoothhcirequestcallbackinfo)*