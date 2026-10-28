# HMHome.ProvisionalHomeConnectionDetails

**Framework**: HomeKit  
**Kind**: struct  
**Role**: Structure

A structure that contains the token to transfer a temporary, provisional home to a person’s home hub.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
struct ProvisionalHomeConnectionDetails
```

## Overview

Use the `prepare-session` REST endpoint of the home hub to obtain the transfer token that allows you to transfer a provisional home to a person’s home hub. The token encapsulates all connection and authentication information the installation controller needs to complete the check-in handshake and the mTLS credential exchange with the home hub.

## Topics

### Creating connection details
- [init(transferToken: Data)](./provisionalhomeconnectiondetails/init%28transfertoken%29.md)
  Creates a structure that contains the token you need to transfer a temporary home to a person’s home hub.
- [var transferToken: Data](./provisionalhomeconnectiondetails/transfertoken.md)
  An opaque token you need to transfer a temporary home to a person’s home hub.

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
- [HMHome.ProvisionalHomeTransferResult](./provisionalhometransferresult.md)
  The outcome of transferring a temporary home to a home hub.
- [HMHome.ProvisionalHomeTransferError](./provisionalhometransfererror.md)
  Errors that occur when transferring a temporary home to a person’s home hub.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/provisionalhomeconnectiondetails)*