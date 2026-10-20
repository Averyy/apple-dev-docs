# name

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

The name of the accessory.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
var name: String
```

## See Also

### Describing the failed accessory
- [init(uuid: UUID, name: String, reason: HMHome.ProvisionalHomeTransferResult.FailedAccessory.Reason, localizedFailureDescription: String?)](./init%28uuid,name,reason,localizedfailuredescription%29.md)
  Creates the structure that contains information about why a transfer failed.
- [var uuid: UUID](./uuid.md)
  A unique identifier for the accessory.
- [var reason: HMHome.ProvisionalHomeTransferResult.FailedAccessory.Reason](./reason-swift.property.md)
  A value that indicates why the transfer failed.
- [HMHome.ProvisionalHomeTransferResult.FailedAccessory.Reason](./reason-swift.enum.md)
  Values that explain why a transfer failed.
- [var localizedFailureDescription: String?](./localizedfailuredescription.md)
  A localized string that explains why the transfer failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/provisionalhometransferresult/failedaccessory/name)*