# HMHome.ProvisionalHomeConnectionDetails

**Framework**: HomeKit  
**Kind**: struct

A structure that contains the token to transfer a temporary, provisional home to a person’s home hub.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
struct ProvisionalHomeConnectionDetails
```

#### Overview

Use the `prepare-session` REST endpoint of the home hub to obtain the transfer token that allows you to transfer a provisional home to a person’s home hub. The token encapsulates all connection and authentication information the installation controller needs to complete the check-in handshake and the mTLS credential exchange with the home hub.

## Topics

### Creating connection details
- [init(transferToken: Data)](hmhome/provisionalhomeconnectiondetails/init(transfertoken:).md)
  Creates a structure that contains the token you need to transfer a temporary home to a person’s home hub.
- [var transferToken: Data](hmhome/provisionalhomeconnectiondetails/transfertoken.md)
  An opaque token you need to transfer a temporary home to a person’s home hub.

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
- [HMHome.ProvisionalHomeTransferResult](hmhome/provisionalhometransferresult.md)
  The outcome of transferring a temporary home to a home hub.
- [HMHome.ProvisionalHomeTransferError](hmhome/provisionalhometransfererror.md)
  Errors that occur when transferring a temporary home to a person’s home hub.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/provisionalhomeconnectiondetails)*