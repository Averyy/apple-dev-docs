# BluetoothHCIEventSynchronousConnectionChangedResults

**Framework**: IOBluetooth  
**Kind**: struct  
**Role**: Structure

**Availability**:
- macOS

## Declaration

```swift
struct BluetoothHCIEventSynchronousConnectionChangedResults
```

```c
struct BluetoothHCIEventSynchronousConnectionChangedResults;
```

## Topics

### Initializers
- [init()](./bluetoothhcieventsynchronousconnectionchangedresults/init%28%29.md)
- [init(connectionHandle: BluetoothConnectionHandle, transmissionInterval: UInt8, retransmissionWindow: UInt8, receivePacketLength: UInt16, transmitPacketLength: UInt16)](./bluetoothhcieventsynchronousconnectionchangedresults/init%28connectionhandle,transmissioninterval,retransmissionwindow,receivepacketlength,transmitpacketlength%29.md)
### Instance Properties
- [var connectionHandle: BluetoothConnectionHandle](./bluetoothhcieventsynchronousconnectionchangedresults/connectionhandle.md)
- [var receivePacketLength: UInt16](./bluetoothhcieventsynchronousconnectionchangedresults/receivepacketlength.md)
- [var retransmissionWindow: UInt8](./bluetoothhcieventsynchronousconnectionchangedresults/retransmissionwindow.md)
- [var transmissionInterval: UInt8](./bluetoothhcieventsynchronousconnectionchangedresults/transmissioninterval.md)
- [var transmitPacketLength: UInt16](./bluetoothhcieventsynchronousconnectionchangedresults/transmitpacketlength.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/bluetoothhcieventsynchronousconnectionchangedresults)*