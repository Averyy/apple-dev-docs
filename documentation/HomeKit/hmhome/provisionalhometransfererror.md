# HMHome.ProvisionalHomeTransferError

**Framework**: HomeKit  
**Kind**: enum

Errors that occur when transferring a temporary home to a person’s home hub.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
enum ProvisionalHomeTransferError
```

#### Overview

This error type indicates that HomeKit was unable to attempt or complete a transfer, and HomeKit didn’t transfer any accessories to the home hub. To view information about partially successful transfers and error information for an individual accessory, use [`HMHome.ProvisionalHomeTransferResult`](hmhome/provisionalhometransferresult.md).

## Topics

### Detecting transfer errors
- [HMHome.ProvisionalHomeTransferError.authenticationFailed](hmhome/provisionalhometransfererror/authenticationfailed.md)
  Authentication with the home hub failed.
- [HMHome.ProvisionalHomeTransferError.connectionFailed](hmhome/provisionalhometransfererror/connectionfailed.md)
  Establishing a network connection to the home hub failed.
- [HMHome.ProvisionalHomeTransferError.serverError](hmhome/provisionalhometransfererror/servererror.md)
  An unexpected server-side error or internal error occurred.
- [HMHome.ProvisionalHomeTransferError.targetHomeRejected](hmhome/provisionalhometransfererror/targethomerejected.md)
  The home hub rejected the target home identifier.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Error](../swift/error.md)
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
- [HMHome.ProvisionalHomeTransferResult](hmhome/provisionalhometransferresult.md)
  The outcome of transferring a temporary home to a home hub.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/provisionalhometransfererror)*