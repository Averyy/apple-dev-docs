# SetWakeOnMagicPacketEnable

**Framework**: NetworkingDriverKit  
**Kind**: method  
**Role**: Instance Method

Enables or disables support for waking up the device when a specially formatted packet arrives.

**Availability**:
- DriverKit

## Declaration

```cpp
virtual kern_return_t SetWakeOnMagicPacketEnable(bool enable);
```

## Return Value

`kIOReturnSuccess` on success, or another value if an error occurred.

## Discussion

Override this method and use it to configure your driver’s wake-on-magic-packet support.

## Parameters

- `enable`: If `YES`, enable promiscuous mode for the device; otherwise, disable it.

## See Also

### Configuring Link Attributes
- [SetTxPacketHeadroom](./settxpacketheadroom.md)
  Reserves the specified number of bytes at the front of each packet.
- [SetTxPacketTailroom](./settxpackettailroom.md)
  Reserves the specified number of bytes at the end of each packet.
- [SetSoftwareVlanSupport](./setsoftwarevlansupport.md)
  Enables software VLAN support.
- [SetMulticastAddresses](./setmulticastaddresses-7wjbn.md)
  Sets the device addresses to use for multicast filtering.
- [SetAllMulticastModeEnable](./setallmulticastmodeenable-5rtva.md)
  Enables or disables multicast support for your service.
- [SetPromiscuousModeEnable](./setpromiscuousmodeenable-82bt.md)
  Enables or disables support for monitoriong all network packets.
- [SetWakeOnMagicPacketSupport](./setwakeonmagicpacketsupport.md)
  Tells the system whether the device supports being woken up when a specially formatted packet arrives.
- [IOUserNetworkMACAddress](../iousernetworkmacaddress.md)
  A hardware address for a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkethernet/setwakeonmagicpacketenable)*