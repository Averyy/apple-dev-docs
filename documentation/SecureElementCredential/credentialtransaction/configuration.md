# CredentialTransaction.Configuration

**Framework**: SecureElementCredential  
**Kind**: class

An object that provides configuration information for a transaction that the client intends to peform.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
class Configuration
```

## Mentions

- [Accessing and using secure element credentials](accessing-and-using-secure-element-credentials.md)

#### Overview

In SwiftUI apps, you fetch a `Configuration` for use in calling the doc://com.apple.documentation/documentation/SwiftUI/View/transactionTask(_:action) view modifer to perform wired transactions and card emulation. Inside the task closure, call [`invalidate()`](credentialtransaction/configuration/invalidate().md) on the configuration when you finish your transaction work.

## Topics

### Invalidating a configuration
- [func invalidate() async throws](credentialtransaction/configuration/invalidate.md)
  Invalidates the configuration and transitions the underlying session state to management.
### Comparing configurations
- [static func == (CredentialTransaction.Configuration, CredentialTransaction.Configuration) -> Bool](credentialtransaction/configuration/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [Equatable Implementations](credentialtransaction/configuration/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)

## See Also

- [func configuration() async throws -> CredentialTransaction.Configuration](credentialsession/configuration.md)
  Retrieves a transaction configuration related to this session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialtransaction/configuration)*