# prepareInterfaceToProvideCredential(for:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

Prepares the interface for a user interaction, like a database login, that enables it to access and return the credential for the given identity.

**Availability**:
- iOS 12.0+ - Deprecated in 17.0
- iPadOS 12.0+ - Deprecated in 17.0
- Mac Catalyst 13.1+ - Deprecated in 17.0
- macOS 11.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`prepareInterfaceToProvideCredential(for:)`](./prepareinterfacetoprovidecredential%28for%29-68qpo.md) instead.

## Declaration

```swift
func prepareInterfaceToProvideCredential(for credentialIdentity: ASPasswordCredentialIdentity)
```

```objc
- (void) prepareInterfaceToProvideCredentialForIdentity:(ASPasswordCredentialIdentity *) credentialIdentity;
```

## Discussion

The system calls this method when your extension can’t provide the requested credential without user interaction. Set up the view controller for any user interaction required to provide the requested credential. Limit user interaction to operations required for providing the requested credential, like showing an authentication UI to unlock the user’s passwords database.

Call the context’s [`completeRequest(withSelectedCredential:completionHandler:)`](../ascredentialproviderextensioncontext/completerequest%28withselectedcredential,completionhandler%29.md) to provide the credential. Alternatively, if an error occurs, call [`cancelRequest(withError:)`](../ascredentialproviderextensioncontext/cancelrequest%28witherror%29.md) instead and pass an error with domain [`ASExtensionErrorDomain`](../asextensionerrordomain.md) and an appropriate error code from [`ASExtensionError.Code`](../asextensionerror/code.md). For example, if your app can’t find the credential identity in the database, pass an error with code [`ASExtensionError.Code.credentialIdentityNotFound`](../asextensionerror/code/credentialidentitynotfound.md).

## Parameters

- `credentialIdentity`: The credential identity for which a credential should be provided.

## See Also

### Deprecated methods
- [func provideCredentialWithoutUserInteraction(for: ASPasswordCredentialIdentity)](./providecredentialwithoutuserinteraction%28for%29-7jlg0.md)
  Attempts to provide the user-requested credential with no further user interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialproviderviewcontroller/prepareinterfacetoprovidecredential(for:)-18ukb)*