# HMHome.ProvisionalHomeTransferResult

**Framework**: HomeKit  
**Kind**: struct  
**Role**: Structure

The outcome of transferring a temporary home to a home hub.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
struct ProvisionalHomeTransferResult
```

## Overview

HomeKit only returns a transfer result if the home hub accepted the transfer request and attempted the transfer. It’s possible for a transfer to be partially successful. Always check the result’s [`failedAccessories`](./provisionalhometransferresult/failedaccessories.md) and [`transferredAccessories`](./provisionalhometransferresult/transferredaccessories.md) properties.

## Topics

### Creating a transfer result
- [init(transferredAccessories: [HMHome.ProvisionalHomeTransferResult.TransferredAccessory], failedAccessories: [HMHome.ProvisionalHomeTransferResult.FailedAccessory])](./provisionalhometransferresult/init%28transferredaccessories,failedaccessories%29.md)
  Creates a structure that describes the outcome of a provisional home transfer.
### Inspecting transfer outcomes
- [var transferredAccessories: [HMHome.ProvisionalHomeTransferResult.TransferredAccessory]](./provisionalhometransferresult/transferredaccessories.md)
  An array of accessories that you transferred from a temporary home to a person’s home hub.
- [HMHome.ProvisionalHomeTransferResult.TransferredAccessory](./provisionalhometransferresult/transferredaccessory.md)
  An accessory that you transferred from a temporary home to a person’s home hub.
- [var failedAccessories: [HMHome.ProvisionalHomeTransferResult.FailedAccessory]](./provisionalhometransferresult/failedaccessories.md)
  An array of accessories that failed to transfer to a person’s home hub.
- [HMHome.ProvisionalHomeTransferResult.FailedAccessory](./provisionalhometransferresult/failedaccessory.md)
  An accessory that HomeKit was unable to transfer to a person’s home hub.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Providing installation services
- [var isProvisionalHome: Bool](./isprovisionalhome.md)
  A property that indicates if the home is a temporary, provisional home for use by installation services.
- [func isProvisionalHome(forPairingIdentifier: String) async throws -> Bool](./isprovisionalhome%28forpairingidentifier%29.md)
  Checks whether the home is a temporary, provisional home for use by installation services.
- [func transferProvisionalHome(connectionDetails: HMHome.ProvisionalHomeConnectionDetails, targetHomeUniqueIdentifier: UUID) async throws(HMHome.ProvisionalHomeTransferError) -> HMHome.ProvisionalHomeTransferResult](./transferprovisionalhome%28connectiondetails,targethomeuniqueidentifier%29.md)
  Transfers a temporary, provisional home to a person’s home hub.
- [HMHome.ProvisionalHomeConnectionDetails](./provisionalhomeconnectiondetails.md)
  A structure that contains the token to transfer a temporary, provisional home to a person’s home hub.
- [HMHome.ProvisionalHomeTransferError](./provisionalhometransfererror.md)
  Errors that occur when transferring a temporary home to a person’s home hub.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/provisionalhometransferresult)*