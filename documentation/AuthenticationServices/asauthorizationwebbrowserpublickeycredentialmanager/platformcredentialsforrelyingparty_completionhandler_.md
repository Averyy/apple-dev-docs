# platformCredentialsForRelyingParty:completionHandler:

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

Gets a list of passkeys available for authenticating with the given relying party.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 16.4+
- macOS 13.3+

## Declaration

```objc
- (void) platformCredentialsForRelyingParty:(NSString *) relyingParty completionHandler:(void (^)(NSArray<ASAuthorizationWebBrowserPlatformPublicKeyCredential *> *)) completionHandler;
```

## Discussion

Before calling this method, check that the value of [`authorizationStateForPlatformCredentials`](./authorizationstateforplatformcredentials.md) is [`ASAuthorizationWebBrowserPublicKeyCredentialManager.AuthorizationState.authorized`](./authorizationstate/authorized.md) and call [`requestAuthorizationForPublicKeyCredentials(_:)`](./requestauthorizationforpublickeycredentials%28_%29.md) if your app needs authorization. If you call this method without authorization, it returns an empty array.

## Parameters

- `relyingParty`: The name of the relying party, which you receive from the web server that issues the authentication challenge.
- `completionHandler`: A block that the operating system calls to provide a list of passkeys available for authenticating with the given relying party.

## See Also

### Using passkeys
- [ASAuthorizationWebBrowserPlatformPublicKeyCredential](../asauthorizationwebbrowserplatformpublickeycredential-c.class.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationwebbrowserpublickeycredentialmanager/platformcredentialsforrelyingparty:completionhandler:)*