# SetTxPacketHeadroom

**Framework**: NetworkingDriverKit  
**Kind**: method

Reserves the specified number of bytes at the front of each packet.

**Availability**:
- DriverKit ?+

## Declaration

```swift
kern_return_t SetTxPacketHeadroom(uint16_t numBytes);
```

#### Return Value

`kIOReturnSuccess` on success, or another value if an error occurred.

## Parameters

- `numBytes`: The number of bytes to reserve at the front of the packet buffer.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkethernet/settxpacketheadroom)*