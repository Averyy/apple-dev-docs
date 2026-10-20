# HMHome.ProvisionalHomeTransferResult.TransferredAccessory

**Framework**: HomeKit  
**Kind**: struct  
**Role**: Structure

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
- [init(uuid: UUID, name: String)](./transferredaccessory/init%28uuid,name%29.md)
  Creates a structure that represents an accessory that was successfully transferred from a temporary home to a person’s home hub.
- [var uuid: UUID](./transferredaccessory/uuid.md)
  A unique identifier for the accessory.
- [var name: String](./transferredaccessory/name.md)
  The name of the accessory.

## Relationships

### Conforms To
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Inspecting transfer outcomes
- [var transferredAccessories: [HMHome.ProvisionalHomeTransferResult.TransferredAccessory]](./transferredaccessories.md)
  An array of accessories that you transferred from a temporary home to a person’s home hub.
- [var failedAccessories: [HMHome.ProvisionalHomeTransferResult.FailedAccessory]](./failedaccessories.md)
  An array of accessories that failed to transfer to a person’s home hub.
- [HMHome.ProvisionalHomeTransferResult.FailedAccessory](./failedaccessory.md)
  An accessory that HomeKit was unable to transfer to a person’s home hub.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/provisionalhometransferresult/transferredaccessory)*