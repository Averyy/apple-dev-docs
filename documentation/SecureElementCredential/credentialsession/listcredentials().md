# listCredentials()

**Framework**: SecureElementCredential  
**Kind**: method  
**Role**: Instance Method

Retrieves a list of of credentials to which the app has access rights.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
func listCredentials() async throws -> [CredentialSession.Credential]
```

## Mentions

- [Accessing and using secure element credentials](../accessing-and-using-secure-element-credentials.md)

## Return Value

An array of credentials to which the calling app has access rights. The order of credentials in this array is random.

## Discussion

When you call this method, the framework caches a snapshot of these credentials. Because credentials can change, refresh your data models whenever your app performs any kind of write operation using the [SecureElementCredential](../SecureElementCredential.md) framework. Also update whenever your app returns to the foreground.

> **Note**: When you call this method from an app extension that has the [`Digital Credentials API - Mobile Document Provider`](../../BundleResources/entitlements/com.apple.developer.identity-document-services.document-provider.mobile-document-types.md) entitlement, the returned array contains only credentials configured as Government ID credentials on the [Apple Business Register](https://register.apple.com/login) (ABR) portal.

- The most common errors are:

  - [`CredentialSession.ErrorCode.sessionInvalidated`](./errorcode/sessioninvalidated.md): The credential session has been invalidated.
  - [`CredentialSession.ErrorCode.invalidSessionState`](./errorcode/invalidsessionstate.md): The session isn’t in the [`CredentialSession.State.management`](./state-swift.enum/management.md) state.

## See Also

### Accessing credentials
- [CredentialSession.Credential](./credential.md)
  Information about a credential that a credential session retrieves from the Secure Element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/listcredentials())*