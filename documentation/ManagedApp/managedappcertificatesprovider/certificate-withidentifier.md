# certificate(withIdentifier:)

**Framework**: ManagedApp  
**Kind**: method

Provides a certificate by its identifier.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- macOS 27.0+ (Beta)
- visionOS 2.4+

## Declaration

```swift
func certificate(withIdentifier identifier: String) async throws(ManagedAppError) -> SecCertificate
```

#### Return Value

The requested certificate

#### Discussion

The MDM server can update the certificate at any time. After that, [`identifiers`](managedappidentitiesprovider/identifiers.md) yields a new array of identifiers. Call this method again to obtain the updated certificate.

The MDM server can change the available certificates at any time. When that happens, the list of valid identifiers updates accordingly. For example, the list of valid identifiers might change between the time that the app accesses [`identifiers`](managedappidentitiesprovider/identifiers.md) and then calls this method passing in one of its elements. So, the app needs to handle the case that this method throws [`ManagedAppError.invalidIdentifier`](managedapperror/invalididentifier.md).

> ❗ **Important**: Avoid storing the certificate and instead, call this method whenever the app needs the certificate. For security reasons, avoid logging or displaying the certificate. Even though the certificate is a “public” certificate, it can contain sensitive information.

> **Note**: [`ManagedAppError.invalidIdentifier`](managedapperror/invalididentifier.md) if no certificate exists with the specified identifier.

## Parameters

- `identifier`: The identifier of the requested certificate. This function throws [`ManagedAppError.invalidIdentifier`](managedapperror/invalididentifier.md) if the value you supply isn’t currently in [`identifiers`](managedappidentitiesprovider/identifiers.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedapp/managedappcertificatesprovider/certificate(withidentifier:))*