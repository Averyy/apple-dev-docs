# HMHome.ProvisionalHomeTransferError

**Framework**: HomeKit  
**Kind**: enum  
**Role**: Enumeration

Errors that occur when transferring a temporary home to a person’s home hub.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
enum ProvisionalHomeTransferError
```

#### Overview

This error type indicates that HomeKit was unable to attempt or complete a transfer, and HomeKit didn’t transfer any accessories to the home hub. To view information about partially successful transfers and error information for an individual accessory, use [`HMHome.ProvisionalHomeTransferResult`](./provisionalhometransferresult.md).

## Topics

### Detecting transfer errors
- [HMHome.ProvisionalHomeTransferError.authenticationFailed](./provisionalhometransfererror/authenticationfailed.md)
  Authentication with the home hub failed.
- [HMHome.ProvisionalHomeTransferError.connectionFailed](./provisionalhometransfererror/connectionfailed.md)
  Establishing a network connection to the home hub failed.
- [HMHome.ProvisionalHomeTransferError.serverError](./provisionalhometransfererror/servererror.md)
  An unexpected server-side error or internal error occurred.
- [HMHome.ProvisionalHomeTransferError.targetHomeRejected](./provisionalhometransfererror/targethomerejected.md)
  The home hub rejected the target home identifier.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Error](../../Swift/error.md)
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
- [HMHome.ProvisionalHomeTransferResult](./provisionalhometransferresult.md)
  The outcome of transferring a temporary home to a home hub.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/provisionalhometransfererror)*