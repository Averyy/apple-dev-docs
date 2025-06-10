# IOUserNetworkEthernet

**Framework**: NetworkingDriverKit  
**Kind**: class

The object you use to manage the setup, configuration, and teardown of your networking driver.

**Availability**:
- DriverKit ?+

## Declaration

```swift
class IOUserNetworkEthernet;
```

#### Overview

Subclass `IOUserNetworkEthernet` and override the methods you need to implement your driver’s behavior. Your subclass manages your driver’s overall life cycle, and facilitates communication between the hardware and the rest of the system. Use the [`Start`](https://developer.apple.com/documentation/DriverKit/IOService/Start) method to establish a link to your hardware and to create the data structures needed to manage incoming and outgoing data packets. Use the [`Stop`](https://developer.apple.com/documentation/DriverKit/IOService/Stop) method to clean up the data structures you create in your [`Start`](https://developer.apple.com/documentation/DriverKit/IOService/Start) method.

Override other methods of this class, and of the [`IOService`](https://developer.apple.com/documentation/DriverKit/IOService) parent class, as needed to enable your interface and implement other network-related behaviors. For example, you might want to override the inherited [`setPowerState`](https://developer.apple.com/documentation/kernel/ioservice/1532866-setpowerstate) method to respond to power-level changes.

##### Specify the Drivers Personality Information

When you subclass `IOUserNetworkEthernet`, update the `IOKitPersonalities` key of your driver extension’s `Info.plist` file with information to match your driver to appropriate hardware. For this class, always include the keys and values in the following table.

| Key | Discussion |
| --- | --- |
| `IOClass` | The value [`IOUserNetworkEthernet`](iousernetworkethernet.md). |
| `IOProviderClass` | The provider class information. For USB-based network interfaces, specify [`IOUSBHostInterface`](https://developer.apple.com/documentation/USBDriverKit/IOUSBHostInterface). |
| `IOUserClass` | The name of your custom subclass. |
| [`CFBundleIdentifier`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleIdentifier) | The bundle identifier of your driver. |
| `CFBundleIdentifierKernel` | The value `com.apple.iokit.IOSkywalkFamily`. |

You may add other keys to assist with the matching process. For example, you might include the `bInterfaceClass`, `bInterfaceProtocol`, and `bInterfaceSubClass` keys to match against specific USB device attributes. The USB specification defines which keys to include when matching your driver to a USB device. For information about the specific key combinations, see  at [`https://www.usb.org`](https://developer.apple.comhttps://www.usb.org).

## Topics

### Configuring the Driver Service
- [init](iousernetworkethernet/init.md)
  Handles the basic initialization of the service.
- [free](iousernetworkethernet/free.md)
  Performs any final cleanup for the service.
- [RegisterEthernetInterface](iousernetworkethernet/registerethernetinterface-4jqw8.md)
  Registers your driver with the networking stack.
### Declaring the Supported Media Types
- [ReportAvailableMediaTypes](iousernetworkethernet/reportavailablemediatypes.md)
  Tells the system what types of networking media your driver supports.
- [SelectMediaType](iousernetworkethernet/selectmediatype.md)
  Selects the media type to use when communicating with the network stack.
- [IOUserNetworkMediaType](iousernetworkmediatype.md)
  A structure describing a specific Ethernet type and configuration that your driver supports.
### Enabling Your Service
- [SetInterfaceEnable](iousernetworkethernet/setinterfaceenable-3v24g.md)
  Enables or disables your service.
### Configuring Link Attributes
- [SetTxPacketHeadroom](iousernetworkethernet/settxpacketheadroom.md)
  Reserves the specified number of bytes at the front of each packet.
- [SetTxPacketTailroom](iousernetworkethernet/settxpackettailroom.md)
  Reserves the specified number of bytes at the end of each packet.
- [SetSoftwareVlanSupport](iousernetworkethernet/setsoftwarevlansupport.md)
  Enables software VLAN support.
- [SetMulticastAddresses](iousernetworkethernet/setmulticastaddresses-7wjbn.md)
  Sets the device addresses to use for multicast filtering.
- [SetAllMulticastModeEnable](iousernetworkethernet/setallmulticastmodeenable-5rtva.md)
  Enables or disables multicast support for your service.
- [SetPromiscuousModeEnable](iousernetworkethernet/setpromiscuousmodeenable-82bt.md)
  Enables or disables support for monitoriong all network packets.
- [SetWakeOnMagicPacketSupport](iousernetworkethernet/setwakeonmagicpacketsupport.md)
  Tells the system whether the device supports being woken up when a specially formatted packet arrives.
- [SetWakeOnMagicPacketEnable](iousernetworkethernet/setwakeonmagicpacketenable.md)
  Enables or disables support for waking up the device when a specially formatted packet arrives.
- [IOUserNetworkMACAddress](iousernetworkmacaddress.md)
  A hardware address for a device.
### Reporting the Connection Status
- [ReportLinkStatus](iousernetworkethernet/reportlinkstatus-5cxiq.md)
  Reports the status of the link between the device and your driver to the system.
- [ReportLinkQuality](iousernetworkethernet/reportlinkquality-4noh0.md)
  Reports the quality of the link between the device and your driver to the system.
- [ReportDataBandwidths](iousernetworkethernet/reportdatabandwidths-10ssx.md)
  Reports the input and output bandwidth between the device and your driver to the system.
- [IOUserNetworkLinkStatus](iousernetworklinkstatus.md)
  A type for specifying the state of your device’s connection.
- [IOUserNetworkLinkQuality](iousernetworklinkquality.md)
  A type for specifying the quality of your device’s connection to the host.
### Instance Methods
- [GetHardwareAssists](iousernetworkethernet/gethardwareassists-4kj3q.md)
- [GetMaxTransferUnit](iousernetworkethernet/getmaxtransferunit-mvla.md)
- [RegisterEthernetInterface](iousernetworkethernet/registerethernetinterface-fffz.md)
- [ReportNicProxyLimits](iousernetworkethernet/reportnicproxylimits-9yg2x.md)
- [SetHardwareAssists](iousernetworkethernet/sethardwareassists-5dvbf.md)
- [SetMTU](iousernetworkethernet/setmtu.md)
- [addHardwareCountsWithInterfaceStatistics](iousernetworkethernet/addhardwarecountswithinterfacestatistics.md)
- [bpfAttach](iousernetworkethernet/bpfattach.md)
- [bpfTap](iousernetworkethernet/bpftap.md)
- [bpfTapInputPacket](iousernetworkethernet/bpftapinputpacket.md)
- [bpfTapOutputPacket](iousernetworkethernet/bpftapoutputpacket.md)
- [getBSDName](iousernetworkethernet/getbsdname.md)
- [getBSDNamePrefix](iousernetworkethernet/getbsdnameprefix.md)
- [getBSDUnitNumber](iousernetworkethernet/getbsdunitnumber.md)
- [getFeatureFlags](iousernetworkethernet/getfeatureflags.md)
- [getHardwareAddress](iousernetworkethernet/gethardwareaddress.md)
- [getHardwareAssists](iousernetworkethernet/gethardwareassists-7o0q0.md)
- [getInitialMedia](iousernetworkethernet/getinitialmedia.md)
- [getInterfaceSubFamily](iousernetworkethernet/getinterfacesubfamily.md)
- [getMaxTransferUnit](iousernetworkethernet/getmaxtransferunit-3iokl.md)
- [getSupportedMediaArray](iousernetworkethernet/getsupportedmediaarray.md)
- [getTSOOptions](iousernetworkethernet/gettsooptions.md)
- [getTxDataOffset](iousernetworkethernet/gettxdataoffset.md)
- [handleChosenMedia](iousernetworkethernet/handlechosenmedia.md)
- [hwConfigNicProxyData](iousernetworkethernet/hwconfignicproxydata-345tz.md)
- [hwConfigNicProxyData](iousernetworkethernet/hwconfignicproxydata-7u8wb.md)
- [processInterfaceCommand](iousernetworkethernet/processinterfacecommand.md)
- [registerEthernetInterface](iousernetworkethernet/registerethernetinterface-8pzu9.md)
- [registerEthernetInterface](iousernetworkethernet/registerethernetinterface-948c9.md)
- [reportDataBandwidths](iousernetworkethernet/reportdatabandwidths-95d7h.md)
- [reportLinkQuality](iousernetworkethernet/reportlinkquality-2tcue.md)
- [reportLinkStatus](iousernetworkethernet/reportlinkstatus-4qtrf.md)
- [reportNicProxyLimits](iousernetworkethernet/reportnicproxylimits-6p2r1.md)
- [setAllMulticastModeEnable](iousernetworkethernet/setallmulticastmodeenable-3aocm.md)
- [setHardwareAddress](iousernetworkethernet/sethardwareaddress.md)
- [setHardwareAssists](iousernetworkethernet/sethardwareassists-2uqz7.md)
- [setHardwareAssists](iousernetworkethernet/sethardwareassists-3vpkr.md)
- [setInterfaceEnable](iousernetworkethernet/setinterfaceenable-6pfsx.md)
- [setMaxTransferUnit](iousernetworkethernet/setmaxtransferunit.md)
- [setMulticastAddresses](iousernetworkethernet/setmulticastaddresses-1o4z3.md)
- [setPowerState](iousernetworkethernet/setpowerstate.md)
- [setPromiscuousModeEnable](iousernetworkethernet/setpromiscuousmodeenable-34fjm.md)
- [start](iousernetworkethernet/start.md)
- [stop](iousernetworkethernet/stop.md)
- [updateInterfaceDescriptor](iousernetworkethernet/updateinterfacedescriptor.md)

## Relationships

### Inherits From
- [IOService](../DriverKit/IOService.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkethernet)*