# IOUserNetworkMACAddress

**Framework**: NetworkingDriverKit  
**Kind**: struct

A hardware address for a device.

**Availability**:
- DriverKit ?+
- Unknown ?+ - Deprecated

## Declaration

```swift
struct IOUserNetworkMACAddress;
```

## Topics

### Getting the MAC Address
- [octet](iousernetworkmacaddress/octet.md)
  The hardware address, specified as a series of six bytes.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkmacaddress)*