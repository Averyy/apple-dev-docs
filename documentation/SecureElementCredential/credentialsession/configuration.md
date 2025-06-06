# configuration()

**Framework**: SecureElementCredential  
**Kind**: method

Retrieves a transaction configuration related to this session.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
nonisolated
func configuration() async throws -> CredentialTransaction.Configuration
```

#### Discussion

This method provides a way to get the session configuration after performing a transaction task with a SwiftUI view.

Clients should call [`invalidate()`](credentialtransaction/configuration/invalidate().md) on this configuration after completing each transaction.

> ⚠️ **Warning**: Don’t import UIKit in any file that imports this type. This causes ambiguity resolving the [`SecureElementCredential`](SecureElementCredential.md) framework’s SwiftUI and UIKit symbols.

Don’t import UIKit in any file that imports this type. This causes ambiguity resolving the [`SecureElementCredential`](SecureElementCredential.md) framework’s SwiftUI and UIKit symbols.

## See Also

- [CredentialTransaction.Configuration](credentialtransaction/configuration.md)
  An object that provides configuration information for a transaction that the client intends to peform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/configuration())*