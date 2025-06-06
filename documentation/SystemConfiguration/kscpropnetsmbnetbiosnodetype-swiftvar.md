# kSCPropNetSMBNetBIOSNodeType

**Framework**: System Configuration  
**Kind**: var

The SMB key `NetBIOSNodeType`, whose value is of type `CFString`.

**Availability**:
- macOS 10.5+

## Declaration

```swift
let kSCPropNetSMBNetBIOSNodeType: CFString
```

#### Discussion

This key can be passed the following constants:

- `kSCValNetSMBNetBIOSNodeTypeBroadcast`, which has the value `Broadcast`
- `kSCValNetSMBNetBIOSNodeTypePeer`, which has the value `Peer`
- `kSCValNetSMBNetBIOSNodeTypeMixed`, which has the value `Mixed`
- `kSCValNetSMBNetBIOSNodeTypeHybrid`, which has the value `Hybrid`

## See Also

- [let kSCPropNetSMBNetBIOSName: CFString](kscpropnetsmbnetbiosname-swift.var.md)
  The SMB key `NetBIOSName`, whose value is of type `CFString`.
- [let kSCPropNetSMBWINSAddresses: CFString](kscpropnetsmbwinsaddresses-swift.var.md)
  The SMB key `WINSAddresses`, whose value is of type `CFArray`, containing elements of type `CFString`.
- [let kSCPropNetSMBWorkgroup: CFString](kscpropnetsmbworkgroup-swift.var.md)
  The SMB key `Workgroup`, whose value is of type `CFString`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/kscpropnetsmbnetbiosnodetype-swift.var)*