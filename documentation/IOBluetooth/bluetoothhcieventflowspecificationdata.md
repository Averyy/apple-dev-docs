# BluetoothHCIEventFlowSpecificationData

**Framework**: IOBluetooth  
**Kind**: struct

**Availability**:
- macOS ?+

## Declaration

```swift
struct BluetoothHCIEventFlowSpecificationData
```

## Topics

### Initializers
- [init()](bluetoothhcieventflowspecificationdata/init.md)
- [init(connectionHandle: BluetoothConnectionHandle, flags: UInt8, flowDirection: UInt8, serviceType: UInt8, tokenRate: UInt32, tokenBucketSize: UInt32, peakBandwidth: UInt32, accessLatency: UInt32)](bluetoothhcieventflowspecificationdata/init(connectionhandle:flags:flowdirection:servicetype:tokenrate:tokenbucketsize:peakbandwidth:accesslatency:).md)
### Instance Properties
- [var accessLatency: UInt32](bluetoothhcieventflowspecificationdata/accesslatency.md)
- [var connectionHandle: BluetoothConnectionHandle](bluetoothhcieventflowspecificationdata/connectionhandle.md)
- [var flags: UInt8](bluetoothhcieventflowspecificationdata/flags.md)
- [var flowDirection: UInt8](bluetoothhcieventflowspecificationdata/flowdirection.md)
- [var peakBandwidth: UInt32](bluetoothhcieventflowspecificationdata/peakbandwidth.md)
- [var serviceType: UInt8](bluetoothhcieventflowspecificationdata/servicetype.md)
- [var tokenBucketSize: UInt32](bluetoothhcieventflowspecificationdata/tokenbucketsize.md)
- [var tokenRate: UInt32](bluetoothhcieventflowspecificationdata/tokenrate.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/bluetoothhcieventflowspecificationdata)*