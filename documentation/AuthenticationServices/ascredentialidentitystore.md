# ASCredentialIdentityStore

**Framework**: Authentication Services  
**Kind**: class

A container that your extension fills to provide credentials through the QuickType bar.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class ASCredentialIdentityStore
```

#### Overview

Make credential identities available to users directly as AutoFill suggestions by adding them to the [`shared`](ascredentialidentitystore/shared.md) instance of the identity store. You can add identities during configuration in your extension’s override of the [`prepareInterfaceForExtensionConfiguration()`](ascredentialproviderviewcontroller/prepareinterfaceforextensionconfiguration().md) method. You can also update the shared store from within your extension’s host app.

Be sure to update the shared store whenever your app’s database changes to avoid showing stale identities as AutoFill suggestions. Take advantage of the incremental change methods [`saveCredentialIdentities(_:completion:)`](ascredentialidentitystore/savecredentialidentities(_:completion:)-1bbx6.md) and [`removeCredentialIdentities(_:completion:)`](ascredentialidentitystore/removecredentialidentities(_:completion:)-67lcw.md) to avoid rewriting the entire store every time you need to make a change.

You can fetch previously saved credential identities with [`credentialIdentities(forService:credentialIdentityTypes:)`](ascredentialidentitystore/credentialidentities(forservice:credentialidentitytypes:).md). Call this method when preparing to store a credential to check whether your app has a saved credential for this domain.

When the user disables your extension, the system clears and disables your shared store. So before making updates, check to see that the store’s enabled to avoid unnecessary activity:

## Topics

### Getting the shared store
- [class var shared: ASCredentialIdentityStore](ascredentialidentitystore/shared.md)
  The shared credential identity store.
### Checking the state of the store
- [func getState((ASCredentialIdentityStoreState) -> Void)](ascredentialidentitystore/getstate(_:).md)
  Gets the state of the credential identity store.
- [class ASCredentialIdentityStoreState](ascredentialidentitystorestate.md)
  A representation of the state of a credential identity store.
### Adding and removing credential identities
- [func saveCredentialIdentities([any ASCredentialIdentity], completion: ((Bool, (any Error)?) -> Void)?)](ascredentialidentitystore/savecredentialidentities(_:completion:)-1bbx6.md)
  Save the supplied credential identities to the store.
- [func replaceCredentialIdentities([any ASCredentialIdentity], completion: ((Bool, (any Error)?) -> Void)?)](ascredentialidentitystore/replacecredentialidentities(_:completion:).md)
  Replaces existing credential identities with new credential identities.
- [func removeAllCredentialIdentities(((Bool, (any Error)?) -> Void)?)](ascredentialidentitystore/removeallcredentialidentities(_:).md)
  Removes all existing credential identities from the store.
- [func removeCredentialIdentities([any ASCredentialIdentity], completion: ((Bool, (any Error)?) -> Void)?)](ascredentialidentitystore/removecredentialidentities(_:completion:)-67lcw.md)
  Remove the given credential identities from the store.
- [protocol ASCredentialIdentity](ascredentialidentity.md)
  A protocol that credential identity classes conform to that uniquely identifies credentials.
- [class ASPasskeyCredentialIdentity](aspasskeycredentialidentity.md)
  A description that uniquely identifies a particular passkey credential.
- [class ASPasswordCredentialIdentity](aspasswordcredentialidentity.md)
  A description that uniquely identifies a particular password credential.
### Fetching saved credential identities
- [func credentialIdentities(forService: ASCredentialServiceIdentifier?, credentialIdentityTypes: ASCredentialIdentityStore.IdentityTypes) async -> [any ASCredentialIdentity]](ascredentialidentitystore/credentialidentities(forservice:credentialidentitytypes:).md)
  Retrieves an array of all previously saved credential identities in the store for your extension.
- [class ASCredentialServiceIdentifier](ascredentialserviceidentifier.md)
  An identifier representing a particular service for which the user needs a credential, like a web site.
- [ASCredentialIdentityStore.IdentityTypes](ascredentialidentitystore/identitytypes.md)
  The defined identity types for use in retrieving credentials.
### Recognizing errors
- [struct ASCredentialIdentityStoreError](ascredentialidentitystoreerror.md)
  A credential identity store error.
- [let ASCredentialIdentityStoreErrorDomain: String](ascredentialidentitystoreerrordomain.md)
  The domain for a credential identity store error.
- [ASCredentialIdentityStoreError.Code](ascredentialidentitystoreerror/code.md)
  Constants that represent credential identity store error codes.
### Deprecated methods
- [func saveCredentialIdentities([ASPasswordCredentialIdentity], completion: ((Bool, (any Error)?) -> Void)?)](ascredentialidentitystore/savecredentialidentities(_:completion:)-5vs4m.md)
  Saves the given credential identities to the store.
- [func replaceCredentialIdentities(with: [ASPasswordCredentialIdentity], completion: ((Bool, (any Error)?) -> Void)?)](ascredentialidentitystore/replacecredentialidentities(with:completion:).md)
  Replaces existing credential identities with new credential identities.
- [func removeCredentialIdentities([ASPasswordCredentialIdentity], completion: ((Bool, (any Error)?) -> Void)?)](ascredentialidentitystore/removecredentialidentities(_:completion:)-2ygnf.md)
  Removes the given credential identities from the store.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func prepareInterfaceForExtensionConfiguration()](ascredentialproviderviewcontroller/prepareinterfaceforextensionconfiguration.md)
  Prepares the interface to enable the user to configure the extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialidentitystore)*