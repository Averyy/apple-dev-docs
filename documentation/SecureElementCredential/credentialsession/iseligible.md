# isEligible

**Framework**: SecureElementCredential  
**Kind**: property

Clients should always check if this variable returns true to dynamically determine if the current device and user configuration can utilize this service before starting a session with this client

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
static var isEligible: Bool { get async throws }
```

## Mentions

- [Accessing and using secure element credentials](accessing-and-using-secure-element-credentials.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/iseligible)*