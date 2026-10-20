# HMHome.ProvisionalHomeTransferResult.FailedAccessory.Reason

**Framework**: HomeKit  
**Kind**: enum  
**Role**: Enumeration

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
- [HMHome.ProvisionalHomeTransferResult.FailedAccessory.Reason.unknown](./reason-swift.enum/unknown.md)
  An unspecified error prevented the transfer of the accessory to the home hub.
- [HMHome.ProvisionalHomeTransferResult.FailedAccessory.Reason.unsupportedAccessoryType](./reason-swift.enum/unsupportedaccessorytype.md)
  A kind of accessory for which the home hub doesn’t support transfer.

## Relationships

### Conforms To
- [Copyable](../../../../Swift/copyable.md)
- [Decodable](../../../../Swift/decodable.md)
- [Encodable](../../../../Swift/encodable.md)
- [Equatable](../../../../Swift/equatable.md)
- [Escapable](../../../../Swift/escapable.md)
- [Hashable](../../../../Swift/hashable.md)
- [RawRepresentable](../../../../Swift/rawrepresentable.md)
- [Sendable](../../../../Swift/sendable.md)
- [SendableMetatype](../../../../Swift/sendablemetatype.md)

## See Also

### Describing the failed accessory
- [init(uuid: UUID, name: String, reason: HMHome.ProvisionalHomeTransferResult.FailedAccessory.Reason, localizedFailureDescription: String?)](./init%28uuid,name,reason,localizedfailuredescription%29.md)
  Creates the structure that contains information about why a transfer failed.
- [var uuid: UUID](./uuid.md)
  A unique identifier for the accessory.
- [var name: String](./name.md)
  The name of the accessory.
- [var reason: HMHome.ProvisionalHomeTransferResult.FailedAccessory.Reason](./reason-swift.property.md)
  A value that indicates why the transfer failed.
- [var localizedFailureDescription: String?](./localizedfailuredescription.md)
  A localized string that explains why the transfer failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/provisionalhometransferresult/failedaccessory/reason-swift.enum)*