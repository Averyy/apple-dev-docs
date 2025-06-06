# SetMulticastAddresses

**Framework**: NetworkingDriverKit  
**Kind**: method

Sets the device addresses to use for multicast filtering.

**Availability**:
- DriverKit ?+
- Unknown ?+ - Deprecated

## Declaration

```swift
kern_return_t SetMulticastAddresses(const IOUserNetworkMACAddress * addresses, uint32_t count);
```

#### Return Value

`kIOReturnSuccess` on success, or another value if an error occurred.

#### Discussion

Override this method and use it to set up a Ethernet multicast filter on your device.

## Parameters

- `addresses`: An array of MAC addresses for the devices to monitor.
- `count`: The number of items in the   parameter.

## See Also

- [SetTxPacketHeadroom](iousernetworkethernet/settxpacketheadroom.md)
  Reserves the specified number of bytes at the front of each packet.
- [SetTxPacketTailroom](iousernetworkethernet/settxpackettailroom.md)
  Reserves the specified number of bytes at the end of each packet.
- [SetSoftwareVlanSupport](iousernetworkethernet/setsoftwarevlansupport.md)
  Enables software VLAN support.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkethernet/setmulticastaddresses-7wjbn)*