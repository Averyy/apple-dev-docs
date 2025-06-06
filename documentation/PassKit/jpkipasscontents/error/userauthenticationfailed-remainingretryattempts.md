# JPKIPassContents.Error.userAuthenticationFailed(remainingRetryAttempts:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: case

Credential authentication request provided was rejected.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+

## Declaration

```swift
case userAuthenticationFailed(remainingRetryAttempts: Int)
```

#### Discussion

- remainingRetryAttempts: The number of failed attempts left before the credential is locked out.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/jpkipasscontents/error/userauthenticationfailed(remainingretryattempts:))*