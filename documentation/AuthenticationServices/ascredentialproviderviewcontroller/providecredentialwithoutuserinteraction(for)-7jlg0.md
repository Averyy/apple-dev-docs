# provideCredentialWithoutUserInteraction(for:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

Attempts to provide the user-requested credential with no further user interaction.

**Availability**:
- iOS 12.0+ - Deprecated in 17.0
- iPadOS 12.0+ - Deprecated in 17.0
- Mac Catalyst 13.1+ - Deprecated in 17.0
- macOS 11.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`provideCredentialWithoutUserInteraction(for:)`](./providecredentialwithoutuserinteraction%28for%29-3mo23.md) instead.

## Declaration

```swift
func provideCredentialWithoutUserInteraction(for credentialIdentity: ASPasswordCredentialIdentity)
```

```objc
- (void) provideCredentialWithoutUserInteractionForIdentity:(ASPasswordCredentialIdentity *) credentialIdentity;
```

#### Discussion

When the user selects a credential identity from the QuickType bar, the system calls the [`provideCredentialWithoutUserInteraction(for:)`](./providecredentialwithoutuserinteraction%28for%29-7jlg0.md) method to ask your extension to provide the corresponding credential.

Call the context’s [`completeRequest(withSelectedCredential:completionHandler:)`](../ascredentialproviderextensioncontext/completerequest%28withselectedcredential,completionhandler%29.md) method to provide the credential if the extension can do so without further user interaction. If not—for example, because the user must first unlock a password database—call the [`cancelRequest(withError:)`](../ascredentialproviderextensioncontext/cancelrequest%28witherror%29.md) method instead using an error with domain [`ASExtensionErrorDomain`](../asextensionerrordomain.md) and code [`userInteractionRequired`](../asextensionerror/userinteractionrequired.md). In turn, the system calls your [`prepareInterfaceToProvideCredential(for:)`](./prepareinterfacetoprovidecredential%28for%29-18ukb.md) method to give your extension a chance to present an interface to handle the needed user interaction.

You can alternatively call the cancel method to indicate other error conditions using one of the codes in [`ASExtensionError.Code`](../asextensionerror/code.md).

> **Note**:  When the system calls this method, your extension’s view controller isn’t showing. Don’t attempt to perform any user interaction from this method.

## Parameters

- `credentialIdentity`: The credential identity for which a credential should be provided.

## See Also

### Deprecated methods
- [func prepareInterfaceToProvideCredential(for: ASPasswordCredentialIdentity)](./prepareinterfacetoprovidecredential%28for%29-18ukb.md)
  Prepares the interface for a user interaction, like a database login, that enables it to access and return the credential for the given identity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialproviderviewcontroller/providecredentialwithoutuserinteraction(for:)-7jlg0)*