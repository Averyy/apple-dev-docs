# SetMulticastAddresses

**Framework**: NetworkingDriverKit  
**Kind**: method  
**Role**: Instance Method

Sets the device addresses to use for multicast filtering.

**Availability**:
- DriverKit

## Declaration

```cpp
virtual kern_return_t SetMulticastAddresses(const IOUserNetworkMACAddress *addresses, uint32_t count);
```

## Return Value

`kIOReturnSuccess` on success, or another value if an error occurred.

## Discussion

Override this method and use it to set up a Ethernet multicast filter on your device.

## Parameters

- `addresses`: An array of MAC addresses for the devices to monitor.
- `count`: The number of items in the `addresses` parameter.

## See Also

### Configuring Link Attributes
- [SetTxPacketHeadroom](./settxpacketheadroom.md)
  Reserves the specified number of bytes at the front of each packet.
- [SetTxPacketTailroom](./settxpackettailroom.md)
  Reserves the specified number of bytes at the end of each packet.
- [SetSoftwareVlanSupport](./setsoftwarevlansupport.md)
  Enables software VLAN support.
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

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkethernet/setmulticastaddresses-7wjbn)*