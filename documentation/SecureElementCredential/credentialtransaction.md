# CredentialTransaction

**Framework**: SecureElementCredential  
**Kind**: class

A transaction object for performing wired and contactless operations in SwiftUI views.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+
- Mac Catalyst 18.1+

## Declaration

```swift
class CredentialTransaction
```

## Mentions

- [Accessing and using secure element credentials](accessing-and-using-secure-element-credentials.md)

#### Overview

Use the [`transactionTask(_:action:)`](https://developer.apple.com/documentation/SwiftUI/View/transactionTask(_:action:)) view modifier to create a task for working with a credential. The `action` closure receives a `CredentialTransaction` instance that it can perform actions on.

You can call the methods of `CredentialTransaction` and [`CredentialTransaction.Configuration`](credentialtransaction/configuration.md) from both apps and app extensions.

> ⚠️ **Warning**:  Don’t import UIKit in any file that imports this type. This causes ambiguity resolving the [`SecureElementCredential`](SecureElementCredential.md) framework’s SwiftUI and UIKit symbols.

## Topics

### Configuring transactions
- [CredentialTransaction.Configuration](credentialtransaction/configuration.md)
  An object that provides configuration information for a transaction that the client intends to perform.
### Performing transactions
- [func performTransaction(using: Credential, options: CardEmulationOptions) async throws](credentialtransaction/performtransaction(using:options:).md)
  Prompts the user for authorization and then activates a credential for card emulation.
- [func performTransactionInWiredMode(using: Credential, instanceAID: Data) async throws](credentialtransaction/performtransactioninwiredmode(using:instanceaid:).md)
  Enters wired mode to perform a transaction.
- [func performCardEmulationTransactionWithCurrentCredential(options: CardEmulationOptions) async throws](credentialtransaction/performcardemulationtransactionwithcurrentcredential(options:).md)
  Activate the current credential to perform a transaction in card emulation mode.
### Supporting types
- [typealias Credential](credential.md)
- [typealias CardEmulationOptions](cardemulationoptions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialtransaction)*