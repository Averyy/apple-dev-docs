# password(withIdentifier:)

**Framework**: ManagedApp  
**Kind**: method

Provides a password by its identifier.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- visionOS 2.4+

## Declaration

```swift
func password(withIdentifier identifier: String) async throws(ManagedAppError) -> String
```

## Mentions

- [Accessing provisioned secrets with identifiers](accessing-provisioned-secrets-with-identifiers.md)

#### Return Value

The requested password.

#### Discussion

The MDM server can update the password at any time. After that, [`identifiers`](managedappidentitiesprovider/identifiers.md) yields a new array of identifiers. Call this method again to obtain the updated password.

The MDM server can change the available passwords at any time. When that happens, the list of valid identifiers updates accordingly. For example, the list of valid identifiers might change between the time that the app accesses [`identifiers`](managedappidentitiesprovider/identifiers.md) and then calls this method passing in one of its elements. So, the app needs to handle the case that this method throws [`ManagedAppError.invalidIdentifier`](managedapperror/invalididentifier.md).

> ❗ **Important**: Avoid storing the password and instead, call this method whenever the app needs the password. For security reasons, avoid logging or displaying the password.

> **Note**: [`ManagedAppError.invalidIdentifier`](managedapperror/invalididentifier.md) if no password exists with the specified identifier.

## Parameters

- `identifier`: The identifier of the requested password. This function throws   if the value you supply isn’t currently in  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedapp/managedapppasswordsprovider/password(withidentifier:))*