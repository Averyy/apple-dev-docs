# presentAccountsToSetUp(_:reason:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

Present system UI that shows the user email accounts they may wish to set up in Mail to receive one-time codes.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
@MainActor
func presentAccountsToSetUp(_ accounts: [DeliveredVerificationCodesManager.AccountRecordForSetUp], reason: DeliveredVerificationCodesManager.SetUpReason) async throws -> Bool
```

## Return Value

Whether the client should proceed with the operation that required this check.

## Discussion

If any of the supplied accounts receive codes at an email address that is not set up in Mail on the current device, the system will present UI that explains to the user that they may want to set up the account so that the device can receive one-time codes sent there. No UI will be presented if all email addresses are already set up.

> **Throws**: `DeliveredVerificationCodesManager.VerificationError` if the check cannot be performed.

## Parameters

- `accounts`: The list of accounts to check.
- `reason`: Why you need verification codes for these accounts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/deliveredverificationcodesmanager/presentaccountstosetup(_:reason:))*