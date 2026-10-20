# BluetoothHCIExtendedInquiryResult

**Framework**: IOBluetooth  
**Kind**: struct  
**Role**: Structure

**Availability**:
- macOS

## Declaration

```swift
struct BluetoothHCIExtendedInquiryResult
```

```c
struct BluetoothHCIExtendedInquiryResult;
```

## Topics

### Initializers
- [init()](./bluetoothhciextendedinquiryresult/init%28%29.md)
- [init(numberOfReponses: UInt8, deviceAddress: BluetoothDeviceAddress, pageScanRepetitionMode: BluetoothPageScanRepetitionMode, reserved: UInt8, classOfDevice: BluetoothClassOfDevice, clockOffset: BluetoothClockOffset, RSSIValue: BluetoothHCIRSSIValue, extendedInquiryResponse: BluetoothHCIExtendedInquiryResponse)](./bluetoothhciextendedinquiryresult/init%28numberofreponses,deviceaddress,pagescanrepetitionmode,reserved,classofdevice,clockoffset,rssivalue,extendedinquiryresponse%29.md)
### Instance Properties
- [var RSSIValue: BluetoothHCIRSSIValue](./bluetoothhciextendedinquiryresult/rssivalue.md)
- [var classOfDevice: BluetoothClassOfDevice](./bluetoothhciextendedinquiryresult/classofdevice.md)
- [var clockOffset: BluetoothClockOffset](./bluetoothhciextendedinquiryresult/clockoffset.md)
- [var deviceAddress: BluetoothDeviceAddress](./bluetoothhciextendedinquiryresult/deviceaddress.md)
- [var extendedInquiryResponse: BluetoothHCIExtendedInquiryResponse](./bluetoothhciextendedinquiryresult/extendedinquiryresponse.md)
- [var numberOfReponses: UInt8](./bluetoothhciextendedinquiryresult/numberofreponses.md)
- [var pageScanRepetitionMode: BluetoothPageScanRepetitionMode](./bluetoothhciextendedinquiryresult/pagescanrepetitionmode.md)
- [var reserved: UInt8](./bluetoothhciextendedinquiryresult/reserved.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/bluetoothhciextendedinquiryresult)*