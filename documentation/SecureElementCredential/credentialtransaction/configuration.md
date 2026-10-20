# CredentialTransaction.Configuration

**Framework**: SecureElementCredential  
**Kind**: class  
**Role**: Class

An object that provides configuration information for a transaction that the client intends to perform.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
class Configuration
```

## Mentions

- [Accessing and using secure element credentials](../accessing-and-using-secure-element-credentials.md)

#### Overview

In SwiftUI apps, you fetch a `Configuration` for use in calling the [`transactionTask(_:action:)`](../../SwiftUI/view/transactiontask%28_,action%29.md) view modifier to perform wired transactions and card emulation. Inside the task closure, call [`invalidate()`](./configuration/invalidate%28%29.md) on the configuration when you finish your transaction work.

## Topics

### Invalidating a configuration
- [func invalidate() async throws](./configuration/invalidate%28%29.md)
  Invalidates the configuration and transitions the underlying session state to management.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)

## See Also

### Using SwiftUI
- [func configuration() async throws -> CredentialTransaction.Configuration](../credentialsession/configuration%28%29.md)
  Retrieves a transaction configuration related to this session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialtransaction/configuration)*