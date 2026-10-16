# isProvisionalHome

**Framework**: HomeKit  
**Kind**: property

A property that indicates if the home is a temporary, provisional home for use by installation services.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
var isProvisionalHome: Bool { get }
```

## See Also

- [func isProvisionalHome(forPairingIdentifier: String) async throws -> Bool](hmhome/isprovisionalhome(forpairingidentifier:).md)
  Checks whether the home is a temporary, provisional home for use by installation services.
- [func transferProvisionalHome(connectionDetails: HMHome.ProvisionalHomeConnectionDetails, targetHomeUniqueIdentifier: UUID) async throws(HMHome.ProvisionalHomeTransferError) -> HMHome.ProvisionalHomeTransferResult](hmhome/transferprovisionalhome(connectiondetails:targethomeuniqueidentifier:).md)
  Transfers a temporary, provisional home to a person’s home hub.
- [HMHome.ProvisionalHomeConnectionDetails](hmhome/provisionalhomeconnectiondetails.md)
  A structure that contains the token to transfer a temporary, provisional home to a person’s home hub.
- [HMHome.ProvisionalHomeTransferResult](hmhome/provisionalhometransferresult.md)
  The outcome of transferring a temporary home to a home hub.
- [HMHome.ProvisionalHomeTransferError](hmhome/provisionalhometransfererror.md)
  Errors that occur when transferring a temporary home to a person’s home hub.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/isprovisionalhome)*