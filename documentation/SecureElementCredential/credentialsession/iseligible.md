# isEligible

**Framework**: SecureElementCredential  
**Kind**: property

A Boolean value that indicates whether the app or app extension is eligible to start a credential session.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
static var isEligible: Bool { get async throws }
```

## Mentions

- [Accessing and using secure element credentials](accessing-and-using-secure-element-credentials.md)

#### Discussion

Always check the value of this property before calling [`startSession()`](credentialsession/startsession().md) to dynamically determine if the current device and user configuration can use the Secure Element credential service.

- The most common errors are: - [`CredentialSession.ErrorCode.resourceUnavailable`](credentialsession/errorcode/resourceunavailable.md): The system service is temporarily unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/iseligible)*