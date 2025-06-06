# platformCredentials(forRelyingParty:)

**Framework**: Authentication Services  
**Kind**: method

Gets a list of passkeys available for authenticating with the given relying party.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 16.4+
- macOS 13.3+

## Declaration

```swift
func platformCredentials(forRelyingParty relyingParty: String) async -> [ASAuthorizationWebBrowserPlatformPublicKeyCredential]
```

#### Return Value

A list of credentials stored on the keychain, or managed by third-party credential managers, that are appropriate for responding to the current challenge.

#### Discussion

Before calling this method, check that the value of [`authorizationStateForPlatformCredentials`](asauthorizationwebbrowserpublickeycredentialmanager/authorizationstateforplatformcredentials.md) is [`ASAuthorizationWebBrowserPublicKeyCredentialManager.AuthorizationState.authorized`](asauthorizationwebbrowserpublickeycredentialmanager/authorizationstate/authorized.md) and call [`requestAuthorizationForPublicKeyCredentials(_:)`](asauthorizationwebbrowserpublickeycredentialmanager/requestauthorizationforpublickeycredentials(_:).md) if your app needs authorization. If you call this method without authorization, it returns an empty array.

## Parameters

- `relyingParty`: The name of the relying party, which you receive from the web server that issues the authentication challenge.

## See Also

- [struct ASAuthorizationWebBrowserPlatformPublicKeyCredential](asauthorizationwebbrowserplatformpublickeycredential-swift.struct.md)
  A structure that describes a passkey stored in the keychain, or managed by a third-party credential manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationwebbrowserpublickeycredentialmanager/platformcredentials(forrelyingparty:))*