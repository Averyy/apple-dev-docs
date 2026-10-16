# HMHome.ProvisionalHomeTransferResult.FailedAccessory.Reason

**Framework**: HomeKit  
**Kind**: enum

Values that explain why a transfer failed.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
enum Reason
```

## Topics

### Failure reasons
- [HMHome.ProvisionalHomeTransferResult.FailedAccessory.Reason.unknown](hmhome/provisionalhometransferresult/failedaccessory/reason-swift.enum/unknown.md)
  An unspecified error prevented the transfer of the accessory to the home hub.
- [HMHome.ProvisionalHomeTransferResult.FailedAccessory.Reason.unsupportedAccessoryType](hmhome/provisionalhometransferresult/failedaccessory/reason-swift.enum/unsupportedaccessorytype.md)
  A kind of accessory for which the home hub doesn’t support transfer.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [init(uuid: UUID, name: String, reason: HMHome.ProvisionalHomeTransferResult.FailedAccessory.Reason, localizedFailureDescription: String?)](hmhome/provisionalhometransferresult/failedaccessory/init(uuid:name:reason:localizedfailuredescription:).md)
  Creates the structure that contains information about why a transfer failed.
- [var uuid: UUID](hmhome/provisionalhometransferresult/failedaccessory/uuid.md)
  A unique identifier for the accessory.
- [var name: String](hmhome/provisionalhometransferresult/failedaccessory/name.md)
  The name of the accessory.
- [var reason: HMHome.ProvisionalHomeTransferResult.FailedAccessory.Reason](hmhome/provisionalhometransferresult/failedaccessory/reason-swift.property.md)
  A value that indicates why the transfer failed.
- [var localizedFailureDescription: String?](hmhome/provisionalhometransferresult/failedaccessory/localizedfailuredescription.md)
  A localized string that explains why the transfer failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/provisionalhometransferresult/failedaccessory/reason-swift.enum)*