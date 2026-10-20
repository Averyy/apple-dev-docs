# failedAccessories

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

An array of accessories that failed to transfer to a person’s home hub.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
var failedAccessories: [HMHome.ProvisionalHomeTransferResult.FailedAccessory]
```

## See Also

### Inspecting transfer outcomes
- [var transferredAccessories: [HMHome.ProvisionalHomeTransferResult.TransferredAccessory]](./transferredaccessories.md)
  An array of accessories that you transferred from a temporary home to a person’s home hub.
- [HMHome.ProvisionalHomeTransferResult.TransferredAccessory](./transferredaccessory.md)
  An accessory that you transferred from a temporary home to a person’s home hub.
- [HMHome.ProvisionalHomeTransferResult.FailedAccessory](./failedaccessory.md)
  An accessory that HomeKit was unable to transfer to a person’s home hub.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/provisionalhometransferresult/failedaccessories)*