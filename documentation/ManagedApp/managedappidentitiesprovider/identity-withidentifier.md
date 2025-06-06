# identity(withIdentifier:)

**Framework**: ManagedApp  
**Kind**: method

Provides an identity by its identifier.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- visionOS 2.4+

## Declaration

```swift
func identity(withIdentifier identifier: String) async throws(ManagedAppError) -> SecIdentity
```

#### Return Value

The requested identity.

#### Discussion

The MDM server can update the identity at any time. After that, [`identifiers`](managedappidentitiesprovider/identifiers.md) yields a new array of identifiers. Call this method again to obtain the updated identity.

The MDM server can change the available identities at any time. When that happens, the list of valid identifiers updates accordingly. For example, the list of valid identifiers might change between the time that the app accesses [`identifiers`](managedappidentitiesprovider/identifiers.md) and then calls this method passing in one of its elements. So, the app needs to handle the case that this method throws [`ManagedAppError.invalidIdentifier`](managedapperror/invalididentifier.md).

When using identities in your app, observe the following caveats:

- Avoid putting identities in a file, database, or in the keychain. Storing an identity might not work as intended, for example, you’re unable to retrieve a hardware-bound key after putting it in the keychain.
- [`SecIdentity`](https://developer.apple.com/documentation/Security/SecIdentity) references underlying keychain data that can disappear if the MDM admin removes the identity at runtime. Call this function as needed for a fresh reference rather than holding on to the result of a prior call for an extended period of time.
- For security reasons, avoid logging or displaying the identity’s certificate or private key. Even though the cerificate is a “public” certificate, it can contain sensitive information.

> **Note**: [`ManagedAppError.invalidIdentifier`](managedapperror/invalididentifier.md) if no identity exists with the specified identifier.

[`ManagedAppError.invalidIdentifier`](managedapperror/invalididentifier.md) if no identity exists with the specified identifier.

## Parameters

- `identifier`: The identifier of the requested identity. This function throws   if the value you supply isn’t currently in  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedapp/managedappidentitiesprovider/identity(withidentifier:))*