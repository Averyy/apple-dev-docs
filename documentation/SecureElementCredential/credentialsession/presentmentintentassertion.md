# CredentialSession.PresentmentIntentAssertion

**Framework**: SecureElementCredential  
**Kind**: class  
**Role**: Class

An object that signals your app’s intention to make exclusive use of the device’s contactless features.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
final class PresentmentIntentAssertion
```

## Mentions

- [Accessing and using secure element credentials](../accessing-and-using-secure-element-credentials.md)

## Overview

Create an instance of this type to obtain a 60-second exclusive use window of the user interface for a selected credential. This prevents interruptions to your app from Wallet, any other default contactless app, or other apps using the SecureElementCredential framework.

> **Note**: A presentment intent assertion isn’t required before launching the presentment sheet.

The assertion expires when any of the following occur:

- The assertion instance deinitializes.
- You call the [`relinquish()`](./presentmentintentassertion/relinquish%28%29.md) method to indicate that you no longer need the assertion.
- The system’s 60-second timeout expires.
- The session encounters a [`CredentialSession.Event.cardEmulationTimeout`](./event/cardemulationtimeout.md), potentially caused by one of the performTransaction methods.

Apps can only acquire an assertion 15 seconds after relinquishing the previous assertion.

Any of the `transaction` methods automatically acquire an internal instance of the `PresentmentIntentAssertion`. Because of this, call `relinquish()` prior to using the transaction methods. The following sequence shows how this works in a SwiftUI application:

1. Call [`acquirePresentmentAssertion()`](./acquirepresentmentassertion%28%29.md) before showing any proprietary payment UI. 2.Call [`relinquish()`](./presentmentintentassertion/relinquish%28%29.md) to stop using the assertion before invoking the transaction method.
2. Invoke [`configuration()`](./configuration%28%29.md) to start a transactionTask.
3. Perform the transaction with the transactionTask.
4. Call [`invalidate()`](../credentialtransaction/configuration/invalidate%28%29.md) after presenting the credential.
5. Optionally, call [`acquirePresentmentAssertion()`](./acquirepresentmentassertion%28%29.md)  to finish up any proprietary payment UI.
6. Call [`relinquish()`](./presentmentintentassertion/relinquish%28%29.md) again to end use of the assertion.

In a UIKit app, use the following approach:

1. Call [`acquirePresentmentAssertion()`](./acquirepresentmentassertion%28%29.md) prior to showing any proprietary payment UI.
2. Call [`relinquish()`](./presentmentintentassertion/relinquish%28%29.md) to stop using the assertion before invoking the transaction API.
3. Perform the transaction task.
4. Optionally, call [`acquirePresentmentAssertion()`](./acquirepresentmentassertion%28%29.md) to finish up any proprietary payment UI.
5. Call [`relinquish()`](./presentmentintentassertion/relinquish%28%29.md) again to end use of the assertion.

## Topics

### Inspecting assertion state
- [var state: CredentialSession.PresentmentIntentAssertion.State](./presentmentintentassertion/state-swift.property.md)
  The state of a presentment intent assertion, indicating whether it’s currently valid.
- [CredentialSession.PresentmentIntentAssertion.State](./presentmentintentassertion/state-swift.enum.md)
  An enumeration of possible states of a presentment intent assertion.
### Relinquishing presentment intent
- [func relinquish() async throws](./presentmentintentassertion/relinquish%28%29.md)
  Ends the presentment intent assertion.

## See Also

### Acquiring exclusive foreground privileges
- [func acquirePresentmentAssertion() async throws -> CredentialSession.PresentmentIntentAssertion](./acquirepresentmentassertion%28%29.md)
  Indicates that the app intends to present a credential to a contactless interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/presentmentintentassertion)*