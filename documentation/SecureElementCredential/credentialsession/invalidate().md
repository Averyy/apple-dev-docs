# invalidate()

**Framework**: SecureElementCredential  
**Kind**: method  
**Role**: Instance Method

Inmediately invalidates a session.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
func invalidate() async throws
```

#### Discussion

Call this method when your app no longer needs a credential session. The system automatically invalidates a session when it deallocates, or when it encounters underlying errors.

When a session invalidates, its event stream also invalidates and deallocates.

You can invalidate a session while in any session state.

## See Also

### Managing the credential session life cycle
- [static func startSession() async throws -> CredentialSession](./startsession%28%29.md)
  Requests a session to view, manage, or use credentials in the Secure Element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/invalidate())*