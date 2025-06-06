# prepareInterfaceToProvideCredential(for:)

**Framework**: Authentication Services  
**Kind**: method

Prepares the interface for a user interaction, like a database login, that enables it to access and return the credential for the given identity.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func prepareInterfaceToProvideCredential(for credentialIdentity: ASPasswordCredentialIdentity)
```

#### Discussion

The system calls this method when your extension can’t provide the requested credential without user interaction. Set up the view controller for any user interaction required to provide the requested credential. Limit user interaction to operations required for providing the requested credential, like showing an authentication UI to unlock the user’s passwords database.

Call the context’s [`completeRequest(withSelectedCredential:completionHandler:)`](ascredentialproviderextensioncontext/completerequest(withselectedcredential:completionhandler:).md) to provide the credential. Alternatively, if an error occurs, call [`cancelRequest(withError:)`](ascredentialproviderextensioncontext/cancelrequest(witherror:).md) instead and pass an error with domain [`ASExtensionErrorDomain`](asextensionerrordomain.md) and an appropriate error code from [`ASExtensionError.Code`](asextensionerror/code.md). For example, if your app can’t find the credential identity in the database, pass an error with code [`ASExtensionError.Code.credentialIdentityNotFound`](asextensionerror/code/credentialidentitynotfound.md).

## Parameters

- `credentialIdentity`: The credential identity for which a credential should be provided.

## See Also

- [func provideCredentialWithoutUserInteraction(for: ASPasswordCredentialIdentity)](ascredentialproviderviewcontroller/providecredentialwithoutuserinteraction(for:)-7jlg0.md)
  Attempts to provide the user-requested credential with no further user interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialproviderviewcontroller/prepareinterfacetoprovidecredential(for:)-18ukb)*