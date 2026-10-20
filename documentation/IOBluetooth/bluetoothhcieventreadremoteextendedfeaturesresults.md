# BluetoothHCIEventReadRemoteExtendedFeaturesResults

**Framework**: IOBluetooth  
**Kind**: struct  
**Role**: Structure

**Availability**:
- macOS

## Declaration

```swift
struct BluetoothHCIEventReadRemoteExtendedFeaturesResults
```

```c
struct BluetoothHCIEventReadRemoteExtendedFeaturesResults;
```

## Topics

### Initializers
- [init()](./bluetoothhcieventreadremoteextendedfeaturesresults/init%28%29.md)
- [init(error: BluetoothHCIStatus, connectionHandle: BluetoothConnectionHandle, page: BluetoothHCIPageNumber, maxPage: BluetoothHCIPageNumber, lmpFeatures: BluetoothHCISupportedFeatures)](./bluetoothhcieventreadremoteextendedfeaturesresults/init%28error,connectionhandle,page,maxpage,lmpfeatures%29.md)
### Instance Properties
- [var connectionHandle: BluetoothConnectionHandle](./bluetoothhcieventreadremoteextendedfeaturesresults/connectionhandle.md)
- [var error: BluetoothHCIStatus](./bluetoothhcieventreadremoteextendedfeaturesresults/error.md)
- [var lmpFeatures: BluetoothHCISupportedFeatures](./bluetoothhcieventreadremoteextendedfeaturesresults/lmpfeatures.md)
- [var maxPage: BluetoothHCIPageNumber](./bluetoothhcieventreadremoteextendedfeaturesresults/maxpage.md)
- [var page: BluetoothHCIPageNumber](./bluetoothhcieventreadremoteextendedfeaturesresults/page.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/bluetoothhcieventreadremoteextendedfeaturesresults)*