# ASDeliveredVerificationCodesManager

**Framework**: Authentication Services  
**Kind**: class  
**Role**: Class

This class allows interacting with one-time codes delivered to the system.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
class ASDeliveredVerificationCodesManager
```

## Overview

The codes may be delivered from many different sources, for example, email or SMS.

## Topics

### Structures
- [ASDeliveredVerificationCodesManager.AccountRecordForSetUp](./asdeliveredverificationcodesmanager/accountrecordforsetup.md)
  An account that a client would like the user to be able to receive verification codes for.
- [ASDeliveredVerificationCodesManager.VerificationError](./asdeliveredverificationcodesmanager/verificationerror.md)
### Initializers
- [init()](./asdeliveredverificationcodesmanager/init%28%29.md)
### Instance Methods
- [func consumeOneTimeCode(ASVerificationCode) async throws](./asdeliveredverificationcodesmanager/consumeonetimecode%28_%29.md)
  Mark a one-time code as “consumed” by the current process.
- [func oneTimeCodes(preferredDuration: TimeInterval, anchor: ASPresentationAnchor) async throws -> some AsyncSequence<ASVerificationCode, any Error>
](./asdeliveredverificationcodesmanager/onetimecodes%28preferredduration,anchor%29-6x2k6.md)
  Stream one-time codes received by the system.
- [func oneTimeCodes(preferredDuration: TimeInterval, anchor: ASPresentationAnchor) async throws -> some AsyncSequence<ASVerificationCode, any Error>
](./asdeliveredverificationcodesmanager/onetimecodes%28preferredduration,anchor%29-tyrg.md)
  Stream one-time codes received by the system.
- [func presentAccountsToSetUp([ASDeliveredVerificationCodesManager.AccountRecordForSetUp], reason: ASDeliveredVerificationCodesManager.SetUpReason, anchor: ASPresentationAnchor) async throws -> Bool](./asdeliveredverificationcodesmanager/presentaccountstosetup%28_,reason,anchor%29-7e3ja.md)
  Present system UI that shows the user email accounts they may wish to set up in Mail to receive one-time codes.
- [func presentAccountsToSetUp([ASDeliveredVerificationCodesManager.AccountRecordForSetUp], reason: ASDeliveredVerificationCodesManager.SetUpReason, anchor: ASPresentationAnchor) async throws -> Bool](./asdeliveredverificationcodesmanager/presentaccountstosetup%28_,reason,anchor%29-8utoh.md)
  Present system UI that shows the user email accounts they may wish to set up in Mail to receive one-time codes.
### Enumerations
- [ASDeliveredVerificationCodesManager.SetUpReason](./asdeliveredverificationcodesmanager/setupreason.md)
  Why a client needs verification codes for a set of accounts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asdeliveredverificationcodesmanager)*