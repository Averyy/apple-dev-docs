# HMHome.ProvisionalHomeTransferResult

**Framework**: HomeKit  
**Kind**: struct

The outcome of transferring a temporary home to a home hub.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
struct ProvisionalHomeTransferResult
```

#### Overview

HomeKit only returns a transfer result if the home hub accepted the transfer request and attempted the transfer. It’s possible for a transfer to be partially successful. Always check the result’s [`failedAccessories`](hmhome/provisionalhometransferresult/failedaccessories.md) and [`transferredAccessories`](hmhome/provisionalhometransferresult/transferredaccessories.md) properties.

## Topics

### Creating a transfer result
- [init(transferredAccessories: [HMHome.ProvisionalHomeTransferResult.TransferredAccessory], failedAccessories: [HMHome.ProvisionalHomeTransferResult.FailedAccessory])](hmhome/provisionalhometransferresult/init(transferredaccessories:failedaccessories:).md)
  Creates a structure that describes the outcome of a provisional home transfer.
### Inspecting transfer outcomes
- [var transferredAccessories: [HMHome.ProvisionalHomeTransferResult.TransferredAccessory]](hmhome/provisionalhometransferresult/transferredaccessories.md)
  An array of accessories that you transferred from a temporary home to a person’s home hub.
- [HMHome.ProvisionalHomeTransferResult.TransferredAccessory](hmhome/provisionalhometransferresult/transferredaccessory.md)
  An accessory that you transferred from a temporary home to a person’s home hub.
- [var failedAccessories: [HMHome.ProvisionalHomeTransferResult.FailedAccessory]](hmhome/provisionalhometransferresult/failedaccessories.md)
  An array of accessories that failed to transfer to a person’s home hub.
- [HMHome.ProvisionalHomeTransferResult.FailedAccessory](hmhome/provisionalhometransferresult/failedaccessory.md)
  An accessory that HomeKit was unable to transfer to a person’s home hub.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var isProvisionalHome: Bool](hmhome/isprovisionalhome.md)
  A property that indicates if the home is a temporary, provisional home for use by installation services.
- [func isProvisionalHome(forPairingIdentifier: String) async throws -> Bool](hmhome/isprovisionalhome(forpairingidentifier:).md)
  Checks whether the home is a temporary, provisional home for use by installation services.
- [func transferProvisionalHome(connectionDetails: HMHome.ProvisionalHomeConnectionDetails, targetHomeUniqueIdentifier: UUID) async throws(HMHome.ProvisionalHomeTransferError) -> HMHome.ProvisionalHomeTransferResult](hmhome/transferprovisionalhome(connectiondetails:targethomeuniqueidentifier:).md)
  Transfers a temporary, provisional home to a person’s home hub.
- [HMHome.ProvisionalHomeConnectionDetails](hmhome/provisionalhomeconnectiondetails.md)
  A structure that contains the token to transfer a temporary, provisional home to a person’s home hub.
- [HMHome.ProvisionalHomeTransferError](hmhome/provisionalhometransfererror.md)
  Errors that occur when transferring a temporary home to a person’s home hub.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/provisionalhometransferresult)*