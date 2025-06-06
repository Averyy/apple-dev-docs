# kSCPropNetIPv4ConfigMethod

**Framework**: System Configuration  
**Kind**: var

The IPv4 key `ConfigMethod`, whose value is of type `CFString`.

**Availability**:
- macOS 10.1+

## Declaration

```swift
let kSCPropNetIPv4ConfigMethod: CFString
```

#### Discussion

This key can be passed the following constants:

- `kSCValNetIPv4ConfigMethodBOOTP`, which has the value `BOOTP`
- `kSCValNetIPv4ConfigMethodDHCP`, which has the value `DHCP`
- `kSCValNetIPv4ConfigMethodINFORM`, which has the value `INFORM`
- `kSCValNetIPv4ConfigMethodLinkLocal`, which has the value `LinkLocal`
- `kSCValNetIPv4ConfigMethodManual`, which has the value `Manual`
- `kSCValNetIPv4ConfigMethodPPP`, which has the value `PPP`

## See Also

- [let kSCPropNetIPv4Addresses: CFString](kscpropnetipv4addresses-swift.var.md)
  The IPv4 key `Addresses`, whose value is of type `CFArray`, containing elements of type `CFString`.
- [let kSCPropNetIPv4DHCPClientID: CFString](kscpropnetipv4dhcpclientid-swift.var.md)
  The IPv4 key `DHCPClientID`, whose value is of type `CFString`.
- [let kSCPropNetIPv4Router: CFString](kscpropnetipv4router-swift.var.md)
  The IPv4 key `Router`, whose value is of type `CFString`.
- [let kSCPropNetIPv4SubnetMasks: CFString](kscpropnetipv4subnetmasks-swift.var.md)
  The IPv4 key `SubnetMasks`, whose value is of type `CFArray`, containing elements of type `CFString`.
- [let kSCPropNetIPv4DestAddresses: CFString](kscpropnetipv4destaddresses-swift.var.md)
  The IPv4 key `DestAddresses`, whose value is of type `CFArray`, containing elements of type `CFString`.
- [let kSCPropNetIPv4BroadcastAddresses: CFString](kscpropnetipv4broadcastaddresses-swift.var.md)
  The IPv4 key `BroadcastAddresses`, whose value is of type `CFArray`, containing elements of type `CFString`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/kscpropnetipv4configmethod-swift.var)*