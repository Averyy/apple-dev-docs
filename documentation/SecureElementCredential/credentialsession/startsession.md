# startSession()

**Framework**: SecureElementCredential  
**Kind**: method

Requests a session to view, manage, or use credentials in the Secure Element.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
static func startSession() async throws -> CredentialSession
```

## Mentions

- [Accessing and using secure element credentials](accessing-and-using-secure-element-credentials.md)

#### Discussion

To start a session, your app needs to be in the foreground. Your app also needs to have the `com.apple.developer.secure-element-credential` entitlement. If your app lacks this entitlement, calls to [`SecureElementCredential`](SecureElementCredential.md) APIs raise [`fatalError(_:file:line:)`](https://developer.apple.com/documentation/Swift/fatalError(_:file:line:)).

If you also want to make your app eligible to be the system’s default contactless app, you need the `com.apple.developer.secure-element-credential.default-contactless-app` entitlement as well.

This method is asynchronous, which requires that you call it with the `await` keyword. When the system is ready to provide the session resource, the following events occur:

- The person using the app receives a GDPR privacy information sheet.
- The first time the app tries to access a credential session, the person using the app receives an alert to allow usage of the Secure Element. If they accept, the session proceeds normally. If they decline, the session invalidates and new sessions for this app fail immediately. To create a valid session, the person using the app needs to allow Secure Element access for the app in Settings.

Sessions start in the [`CredentialSession.State.management`](credentialsession/state-swift.enum/management.md) state. An app can have only one active session at a time. When your app no longer needs the credential session, call [`invalidate()`](credentialsession/invalidate().md). If your app goes into the background, the system automatically invalidates your session after a short delay.

## See Also

- [func invalidate() async throws](credentialsession/invalidate.md)
  Inmediately invalidates a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/startsession())*