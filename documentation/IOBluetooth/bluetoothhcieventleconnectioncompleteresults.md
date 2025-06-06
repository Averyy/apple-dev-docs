# BluetoothHCIEventLEConnectionCompleteResults

**Framework**: IOBluetooth  
**Kind**: struct

**Availability**:
- macOS ?+

## Declaration

```swift
struct BluetoothHCIEventLEConnectionCompleteResults
```

## Topics

### Initializers
- [init()](bluetoothhcieventleconnectioncompleteresults/init.md)
- [init(connectionHandle: BluetoothConnectionHandle, role: UInt8, peerAddressType: UInt8, peerAddress: BluetoothDeviceAddress, connInterval: UInt16, connLatency: UInt16, supervisionTimeout: UInt16, masterClockAccuracy: UInt8)](bluetoothhcieventleconnectioncompleteresults/init(connectionhandle:role:peeraddresstype:peeraddress:conninterval:connlatency:supervisiontimeout:masterclockaccuracy:).md)
### Instance Properties
- [var connInterval: UInt16](bluetoothhcieventleconnectioncompleteresults/conninterval.md)
- [var connLatency: UInt16](bluetoothhcieventleconnectioncompleteresults/connlatency.md)
- [var connectionHandle: BluetoothConnectionHandle](bluetoothhcieventleconnectioncompleteresults/connectionhandle.md)
- [var masterClockAccuracy: UInt8](bluetoothhcieventleconnectioncompleteresults/masterclockaccuracy.md)
- [var peerAddress: BluetoothDeviceAddress](bluetoothhcieventleconnectioncompleteresults/peeraddress.md)
- [var peerAddressType: UInt8](bluetoothhcieventleconnectioncompleteresults/peeraddresstype.md)
- [var role: UInt8](bluetoothhcieventleconnectioncompleteresults/role.md)
- [var supervisionTimeout: UInt16](bluetoothhcieventleconnectioncompleteresults/supervisiontimeout.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/bluetoothhcieventleconnectioncompleteresults)*