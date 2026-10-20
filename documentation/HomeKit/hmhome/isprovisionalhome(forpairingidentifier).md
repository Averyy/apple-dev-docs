# isProvisionalHome(forPairingIdentifier:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Checks whether the home is a temporary, provisional home for use by installation services.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
func isProvisionalHome(forPairingIdentifier pairingIdentifier: String) async throws -> Bool
```

#### Return Value

`true` if this is a provisional home configured with the given identifier or `false` if the home isn’t a provisional home or doesn’t match the given pairing identifier.

#### Overview

Performs an asynchronous query with the provided identifier to check if the home is a temporary, provisional home.

## Parameters

- `pairingIdentifier`: The home’s pairing identifier.

## See Also

### Providing installation services
- [var isProvisionalHome: Bool](./isprovisionalhome.md)
  A property that indicates if the home is a temporary, provisional home for use by installation services.
- [func transferProvisionalHome(connectionDetails: HMHome.ProvisionalHomeConnectionDetails, targetHomeUniqueIdentifier: UUID) async throws(HMHome.ProvisionalHomeTransferError) -> HMHome.ProvisionalHomeTransferResult](./transferprovisionalhome%28connectiondetails,targethomeuniqueidentifier%29.md)
  Transfers a temporary, provisional home to a person’s home hub.
- [HMHome.ProvisionalHomeConnectionDetails](./provisionalhomeconnectiondetails.md)
  A structure that contains the token to transfer a temporary, provisional home to a person’s home hub.
- [HMHome.ProvisionalHomeTransferResult](./provisionalhometransferresult.md)
  The outcome of transferring a temporary home to a home hub.
- [HMHome.ProvisionalHomeTransferError](./provisionalhometransfererror.md)
  Errors that occur when transferring a temporary home to a person’s home hub.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/isprovisionalhome(forpairingidentifier:))*