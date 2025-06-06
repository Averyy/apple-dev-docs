# IOBluetoothDeviceSearchAttributes

**Framework**: IOBluetooth  
**Kind**: struct

Structure used to search for particular devices.

**Availability**:
- macOS ?+

## Declaration

```swift
struct IOBluetoothDeviceSearchAttributes
```

#### Overview

You can search for general device classes and service classes, or you can search for a specific device address or name. If you pass NULL as the attribute structure, you will get ALL devices in the vicinity found during a search. Note that passing a zeroed out block of attributes is NOT equivalent to passing in NULL!

## Topics

### Initializers
- [init()](iobluetoothdevicesearchattributes/init.md)
- [init(options: IOBluetoothDeviceSearchOptions, maxResults: IOItemCount, deviceAttributeCount: IOItemCount, attributeList: UnsafeMutablePointer<IOBluetoothDeviceSearchDeviceAttributes>!)](iobluetoothdevicesearchattributes/init(options:maxresults:deviceattributecount:attributelist:).md)
### Instance Properties
- [var attributeList: UnsafeMutablePointer<IOBluetoothDeviceSearchDeviceAttributes>!](iobluetoothdevicesearchattributes/attributelist.md)
- [var deviceAttributeCount: IOItemCount](iobluetoothdevicesearchattributes/deviceattributecount.md)
- [var maxResults: IOItemCount](iobluetoothdevicesearchattributes/maxresults.md)
- [var options: IOBluetoothDeviceSearchOptions](iobluetoothdevicesearchattributes/options.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevicesearchattributes)*