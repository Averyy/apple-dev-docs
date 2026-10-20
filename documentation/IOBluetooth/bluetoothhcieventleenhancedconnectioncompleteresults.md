# BluetoothHCIEventLEEnhancedConnectionCompleteResults

**Framework**: IOBluetooth  
**Kind**: struct  
**Role**: Structure

**Availability**:
- macOS

## Declaration

```swift
struct BluetoothHCIEventLEEnhancedConnectionCompleteResults
```

```c
struct BluetoothHCIEventLEEnhancedConnectionCompleteResults;
```

## Topics

### Initializers
- [init()](./bluetoothhcieventleenhancedconnectioncompleteresults/init%28%29.md)
- [init(connectionHandle: BluetoothConnectionHandle, role: UInt8, peerAddressType: UInt8, peerAddress: BluetoothDeviceAddress, localResolvablePrivateAddress: BluetoothDeviceAddress, peerResolvablePrivateAddress: BluetoothDeviceAddress, connInterval: UInt16, connLatency: UInt16, supervisionTimeout: UInt16, masterClockAccuracy: UInt8)](./bluetoothhcieventleenhancedconnectioncompleteresults/init%28connectionhandle,role,peeraddresstype,peeraddress,localresolvableprivateaddress,peerresolvableprivateaddress,conninterval,connlatency,supervisiontimeout,masterclockaccuracy%29.md)
### Instance Properties
- [var connInterval: UInt16](./bluetoothhcieventleenhancedconnectioncompleteresults/conninterval.md)
- [var connLatency: UInt16](./bluetoothhcieventleenhancedconnectioncompleteresults/connlatency.md)
- [var connectionHandle: BluetoothConnectionHandle](./bluetoothhcieventleenhancedconnectioncompleteresults/connectionhandle.md)
- [var localResolvablePrivateAddress: BluetoothDeviceAddress](./bluetoothhcieventleenhancedconnectioncompleteresults/localresolvableprivateaddress.md)
- [var masterClockAccuracy: UInt8](./bluetoothhcieventleenhancedconnectioncompleteresults/masterclockaccuracy.md)
- [var peerAddress: BluetoothDeviceAddress](./bluetoothhcieventleenhancedconnectioncompleteresults/peeraddress.md)
- [var peerAddressType: UInt8](./bluetoothhcieventleenhancedconnectioncompleteresults/peeraddresstype.md)
- [var peerResolvablePrivateAddress: BluetoothDeviceAddress](./bluetoothhcieventleenhancedconnectioncompleteresults/peerresolvableprivateaddress.md)
- [var role: UInt8](./bluetoothhcieventleenhancedconnectioncompleteresults/role.md)
- [var supervisionTimeout: UInt16](./bluetoothhcieventleenhancedconnectioncompleteresults/supervisiontimeout.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Structures
- [struct BluetoothAFHHostChannelClassification](./bluetoothafhhostchannelclassification.md)
- [struct BluetoothAFHResults](./bluetoothafhresults.md)
- [struct BluetoothAMPCommandRejectReason](./bluetoothampcommandrejectreason.md)
- [struct BluetoothAMPCreatePhysicalLinkResponseStatus](./bluetoothampcreatephysicallinkresponsestatus.md)
- [struct BluetoothAMPDisconnectPhysicalLinkResponseStatus](./bluetoothampdisconnectphysicallinkresponsestatus.md)
- [struct BluetoothAMPDiscoverResponseControllerStatus](./bluetoothampdiscoverresponsecontrollerstatus.md)
- [struct BluetoothAMPGetAssocResponseStatus](./bluetoothampgetassocresponsestatus.md)
- [struct BluetoothAMPGetInfoResponseStatus](./bluetoothampgetinforesponsestatus.md)
- [struct BluetoothAMPManagerCode](./bluetoothampmanagercode.md)
- [struct BluetoothAuthenticationRequirementsValues](./bluetoothauthenticationrequirementsvalues.md)
- [struct BluetoothCompanyIdentifers](./bluetoothcompanyidentifers.md)
- [struct BluetoothDeviceAddress](./bluetoothdeviceaddress.md)
- [struct BluetoothEnhancedSynchronousConnectionInfo](./bluetoothenhancedsynchronousconnectioninfo.md)
- [struct BluetoothEventFilterCondition](./bluetootheventfiltercondition.md)
- [struct BluetoothFeatureBits](./bluetoothfeaturebits.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/bluetoothhcieventleenhancedconnectioncompleteresults)*