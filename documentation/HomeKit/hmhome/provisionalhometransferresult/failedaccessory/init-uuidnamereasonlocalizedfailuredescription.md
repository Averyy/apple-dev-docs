# init(uuid:name:reason:localizedFailureDescription:)

**Framework**: HomeKit  
**Kind**: init

Creates the structure that contains information about why a transfer failed.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
init(uuid: UUID, name: String, reason: HMHome.ProvisionalHomeTransferResult.FailedAccessory.Reason, localizedFailureDescription: String? = nil)
```

#### Return Value

An accessory that wasn’t transferred to the home hub.

## Parameters

- `uuid`: A string that uniquely identifies the accessory.
- `name`: The name of the accessory.
- `reason`: A value that indicates why the transfer failed.
- `localizedFailureDescription`: A localized string that explains why the transfer failed.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/provisionalhometransferresult/failedaccessory/init(uuid:name:reason:localizedfailuredescription:))*