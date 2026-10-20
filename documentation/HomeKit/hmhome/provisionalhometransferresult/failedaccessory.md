# HMHome.ProvisionalHomeTransferResult.FailedAccessory

**Framework**: HomeKit  
**Kind**: struct  
**Role**: Structure

An accessory that HomeKit was unable to transfer to a person’s home hub.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
struct FailedAccessory
```

## Topics

### Describing the failed accessory
- [init(uuid: UUID, name: String, reason: HMHome.ProvisionalHomeTransferResult.FailedAccessory.Reason, localizedFailureDescription: String?)](./failedaccessory/init%28uuid,name,reason,localizedfailuredescription%29.md)
  Creates the structure that contains information about why a transfer failed.
- [var uuid: UUID](./failedaccessory/uuid.md)
  A unique identifier for the accessory.
- [var name: String](./failedaccessory/name.md)
  The name of the accessory.
- [var reason: HMHome.ProvisionalHomeTransferResult.FailedAccessory.Reason](./failedaccessory/reason-swift.property.md)
  A value that indicates why the transfer failed.
- [HMHome.ProvisionalHomeTransferResult.FailedAccessory.Reason](./failedaccessory/reason-swift.enum.md)
  Values that explain why a transfer failed.
- [var localizedFailureDescription: String?](./failedaccessory/localizedfailuredescription.md)
  A localized string that explains why the transfer failed.

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
- [HMHome.ProvisionalHomeTransferResult.TransferredAccessory](./transferredaccessory.md)
  An accessory that you transferred from a temporary home to a person’s home hub.
- [var failedAccessories: [HMHome.ProvisionalHomeTransferResult.FailedAccessory]](./failedaccessories.md)
  An array of accessories that failed to transfer to a person’s home hub.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/provisionalhometransferresult/failedaccessory)*