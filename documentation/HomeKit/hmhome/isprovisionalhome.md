# isProvisionalHome

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

A property that indicates if the home is a temporary, provisional home for use by installation services.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
var isProvisionalHome: Bool { get }
```

## See Also

### Providing installation services
- [func isProvisionalHome(forPairingIdentifier: String) async throws -> Bool](./isprovisionalhome%28forpairingidentifier%29.md)
  Checks whether the home is a temporary, provisional home for use by installation services.
- [func transferProvisionalHome(connectionDetails: HMHome.ProvisionalHomeConnectionDetails, targetHomeUniqueIdentifier: UUID) async throws(HMHome.ProvisionalHomeTransferError) -> HMHome.ProvisionalHomeTransferResult](./transferprovisionalhome%28connectiondetails,targethomeuniqueidentifier%29.md)
  Transfers a temporary, provisional home to a person’s home hub.
- [HMHome.ProvisionalHomeConnectionDetails](./provisionalhomeconnectiondetails.md)
  A structure that contains the token to transfer a temporary, provisional home to a person’s home hub.
- [HMHome.ProvisionalHomeTransferResult](./provisionalhometransferresult.md)
  The outcome of transferring a temporary home to a home hub.
- [HMHome.ProvisionalHomeTransferError](./provisionalhometransfererror.md)
  Errors that occur when transferring a temporary home to a person’s home hub.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/isprovisionalhome)*