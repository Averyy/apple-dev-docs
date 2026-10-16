# HMHome.ProvisionalHomeTransferResult.TransferredAccessory

**Framework**: HomeKit  
**Kind**: struct

An accessory that you transferred from a temporary home to a person’s home hub.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
struct TransferredAccessory
```

## Topics

### Describing the transferred accessory
- [init(uuid: UUID, name: String)](hmhome/provisionalhometransferresult/transferredaccessory/init(uuid:name:).md)
  Creates a structure that represents an accessory that was successfully transferred from a temporary home to a person’s home hub.
- [var uuid: UUID](hmhome/provisionalhometransferresult/transferredaccessory/uuid.md)
  A unique identifier for the accessory.
- [var name: String](hmhome/provisionalhometransferresult/transferredaccessory/name.md)
  The name of the accessory.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var transferredAccessories: [HMHome.ProvisionalHomeTransferResult.TransferredAccessory]](hmhome/provisionalhometransferresult/transferredaccessories.md)
  An array of accessories that you transferred from a temporary home to a person’s home hub.
- [var failedAccessories: [HMHome.ProvisionalHomeTransferResult.FailedAccessory]](hmhome/provisionalhometransferresult/failedaccessories.md)
  An array of accessories that failed to transfer to a person’s home hub.
- [HMHome.ProvisionalHomeTransferResult.FailedAccessory](hmhome/provisionalhometransferresult/failedaccessory.md)
  An accessory that HomeKit was unable to transfer to a person’s home hub.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/provisionalhometransferresult/transferredaccessory)*