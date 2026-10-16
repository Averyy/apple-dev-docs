# transferProvisionalHome(connectionDetails:targetHomeUniqueIdentifier:)

**Framework**: HomeKit  
**Kind**: method

Transfers a temporary, provisional home to a person’s home hub.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
func transferProvisionalHome(connectionDetails: HMHome.ProvisionalHomeConnectionDetails, targetHomeUniqueIdentifier: UUID) async throws(HMHome.ProvisionalHomeTransferError) -> HMHome.ProvisionalHomeTransferResult
```

#### Return Value

Transfer results for each accessory, allowing you to identify a partially successful transfer.

#### Overview

When you transfer a temporary home to a person’s home hub, HomeKit encodes a snapshot of all paired accessories, creates a secure channel with the connection details’ [`transferToken`](hmhome/provisionalhomeconnectiondetails/transfertoken.md), and uses the channel to send the snapshot to the home hub.

> **Note**: Error information for failures that occur when transferring a temporary, provisional home to a person’s home hub.

## Parameters

- `connectionDetails`: A structure containing the opaque token HomeKit uses to transfer a provisional home to a home hub.
- `targetHomeUniqueIdentifier`: The UUID you obtain from the home installation server that identifies the destination home on a home hub. This UUID is distinct from a provisional home’s own identifier.

## See Also

- [var isProvisionalHome: Bool](hmhome/isprovisionalhome.md)
  A property that indicates if the home is a temporary, provisional home for use by installation services.
- [func isProvisionalHome(forPairingIdentifier: String) async throws -> Bool](hmhome/isprovisionalhome(forpairingidentifier:).md)
  Checks whether the home is a temporary, provisional home for use by installation services.
- [HMHome.ProvisionalHomeConnectionDetails](hmhome/provisionalhomeconnectiondetails.md)
  A structure that contains the token to transfer a temporary, provisional home to a person’s home hub.
- [HMHome.ProvisionalHomeTransferResult](hmhome/provisionalhometransferresult.md)
  The outcome of transferring a temporary home to a home hub.
- [HMHome.ProvisionalHomeTransferError](hmhome/provisionalhometransfererror.md)
  Errors that occur when transferring a temporary home to a person’s home hub.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/transferprovisionalhome(connectiondetails:targethomeuniqueidentifier:))*