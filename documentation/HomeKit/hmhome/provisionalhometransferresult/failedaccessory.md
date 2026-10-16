# HMHome.ProvisionalHomeTransferResult.FailedAccessory

**Framework**: HomeKit  
**Kind**: struct

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
- [init(uuid: UUID, name: String, reason: HMHome.ProvisionalHomeTransferResult.FailedAccessory.Reason, localizedFailureDescription: String?)](hmhome/provisionalhometransferresult/failedaccessory/init(uuid:name:reason:localizedfailuredescription:).md)
  Creates the structure that contains information about why a transfer failed.
- [var uuid: UUID](hmhome/provisionalhometransferresult/failedaccessory/uuid.md)
  A unique identifier for the accessory.
- [var name: String](hmhome/provisionalhometransferresult/failedaccessory/name.md)
  The name of the accessory.
- [var reason: HMHome.ProvisionalHomeTransferResult.FailedAccessory.Reason](hmhome/provisionalhometransferresult/failedaccessory/reason-swift.property.md)
  A value that indicates why the transfer failed.
- [HMHome.ProvisionalHomeTransferResult.FailedAccessory.Reason](hmhome/provisionalhometransferresult/failedaccessory/reason-swift.enum.md)
  Values that explain why a transfer failed.
- [var localizedFailureDescription: String?](hmhome/provisionalhometransferresult/failedaccessory/localizedfailuredescription.md)
  A localized string that explains why the transfer failed.

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
- [HMHome.ProvisionalHomeTransferResult.TransferredAccessory](hmhome/provisionalhometransferresult/transferredaccessory.md)
  An accessory that you transferred from a temporary home to a person’s home hub.
- [var failedAccessories: [HMHome.ProvisionalHomeTransferResult.FailedAccessory]](hmhome/provisionalhometransferresult/failedaccessories.md)
  An array of accessories that failed to transfer to a person’s home hub.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/provisionalhometransferresult/failedaccessory)*