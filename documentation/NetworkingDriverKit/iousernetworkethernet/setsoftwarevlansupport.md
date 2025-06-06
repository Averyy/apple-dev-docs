# SetSoftwareVlanSupport

**Framework**: NetworkingDriverKit  
**Kind**: method

Enables software VLAN support.

**Availability**:
- DriverKit ?+

## Declaration

```swift
kern_return_t SetSoftwareVlanSupport(bool isSupported);
```

#### Return Value

`kIOReturnSuccess` on success, or another value if an error occurred.

## Parameters

- `isSupported`: If  , enable software VLAN support; otherwise, disable it.

## See Also

- [SetTxPacketHeadroom](iousernetworkethernet/settxpacketheadroom.md)
  Reserves the specified number of bytes at the front of each packet.
- [SetTxPacketTailroom](iousernetworkethernet/settxpackettailroom.md)
  Reserves the specified number of bytes at the end of each packet.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkethernet/setsoftwarevlansupport)*