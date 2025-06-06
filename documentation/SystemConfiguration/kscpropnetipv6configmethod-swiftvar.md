# kSCPropNetIPv6ConfigMethod

**Framework**: System Configuration  
**Kind**: var

The IPv6 key `ConfigMethod`, whose value is of type `CFString`.

**Availability**:
- macOS 10.1+

## Declaration

```swift
let kSCPropNetIPv6ConfigMethod: CFString
```

#### Discussion

This key can be passed the following constants:

- `kSCValNetIPv6ConfigMethodAutomatic`, which has the value `Automatic`
- `kSCValNetIPv6ConfigMethodManual`, which has the value `Manual`
- `kSCValNetIPv6ConfigMethodRouterAdvertisement`, which has the value `RouterAdvertisement`
- `kSCValNetIPv6ConfigMethod6to4`, which has the value `6to4`

## See Also

- [let kSCPropNetIPv6Addresses: CFString](kscpropnetipv6addresses-swift.var.md)
  The IPv6 key `Addresses`, whose value is of type `CFArray`, containing elements of type `CFString`.
- [let kSCPropNetIPv6DestAddresses: CFString](kscpropnetipv6destaddresses-swift.var.md)
  The IPv6 key `DestAddresses`, whose value is of type `CFArray`, containing elements of type `CFString`.
- [let kSCPropNetIPv6Flags: CFString](kscpropnetipv6flags-swift.var.md)
  The IPv6 key `Flags`, whose value is of type `CFNumber`.
- [let kSCPropNetIPv6PrefixLength: CFString](kscpropnetipv6prefixlength-swift.var.md)
  The IPv6 key `PrefixLength`, whose value is of type `CFArray`, containing elements of type `CFNumber`.
- [let kSCPropNetIPv6Router: CFString](kscpropnetipv6router-swift.var.md)
  The IPv6 key `Router`, whose value is of type `CFString`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/kscpropnetipv6configmethod-swift.var)*