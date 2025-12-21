# reportUnusedPasswordCredential(domain:userName:)

**Framework**: Authentication Services  
**Kind**: method

Report an unused password credential for a given domain and username. Password managers may remove or hide the password credential. This information is shared with all password managers enabled in the system.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+
- macOS 26.2+
- visionOS 26.2+

## Declaration

```swift
@MainActor
func reportUnusedPasswordCredential(domain: String, userName: String) async throws
```

#### Discussion

> **Note**: `ASAuthorizationError` if the system failed to accept the update.

## Parameters

- `domain`: The website domain that the credential is saved for.
- `userName`: The account user name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/credentialdatamanager/reportunusedpasswordcredential(domain:username:))*