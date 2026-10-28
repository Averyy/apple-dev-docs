# SetSoftwareVlanSupport

**Framework**: NetworkingDriverKit  
**Kind**: method  
**Role**: Instance Method

Enables software VLAN support.

**Availability**:
- DriverKit

## Declaration

```c
kern_return_t SetSoftwareVlanSupport(bool isSupported);
```

## Return Value

`kIOReturnSuccess` on success, or another value if an error occurred.

## Parameters

- `isSupported`: If `YES`, enable software VLAN support; otherwise, disable it.

## See Also

### Configuring Link Attributes
- [SetTxPacketHeadroom](./settxpacketheadroom.md)
  Reserves the specified number of bytes at the front of each packet.
- [SetTxPacketTailroom](./settxpackettailroom.md)
  Reserves the specified number of bytes at the end of each packet.
- [SetMulticastAddresses](./setmulticastaddresses-7wjbn.md)
  Sets the device addresses to use for multicast filtering.
- [SetAllMulticastModeEnable](./setallmulticastmodeenable-5rtva.md)
  Enables or disables multicast support for your service.
- [SetPromiscuousModeEnable](./setpromiscuousmodeenable-82bt.md)
  Enables or disables support for monitoriong all network packets.
- [SetWakeOnMagicPacketSupport](./setwakeonmagicpacketsupport.md)
  Tells the system whether the device supports being woken up when a specially formatted packet arrives.
- [SetWakeOnMagicPacketEnable](./setwakeonmagicpacketenable.md)
  Enables or disables support for waking up the device when a specially formatted packet arrives.
- [IOUserNetworkMACAddress](../iousernetworkmacaddress.md)
  A hardware address for a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkethernet/setsoftwarevlansupport)*