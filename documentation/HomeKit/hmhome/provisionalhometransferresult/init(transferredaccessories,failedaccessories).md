# init(transferredAccessories:failedAccessories:)

**Framework**: HomeKit  
**Kind**: init  
**Role**: Initializer

Creates a structure that describes the outcome of a provisional home transfer.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
init(transferredAccessories: [HMHome.ProvisionalHomeTransferResult.TransferredAccessory], failedAccessories: [HMHome.ProvisionalHomeTransferResult.FailedAccessory])
```

## Return Value

The outcome of transferring a provisional home to a home hub.

## Parameters

- `transferredAccessories`: The accessories that HomeKit successfully transferred from the temporary home to the person’s home hub.
- `failedAccessories`: The accessories that HomeKit was unable to transfer to the person’s home hub.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/provisionalhometransferresult/init(transferredaccessories:failedaccessories:))*