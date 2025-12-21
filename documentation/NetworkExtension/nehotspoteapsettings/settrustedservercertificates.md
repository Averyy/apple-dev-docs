# setTrustedServerCertificates(_:)

**Framework**: Network Extension  
**Kind**: method

Sets trusted EAP server certificates for an enterprise Wi-Fi or Hotspot 2.0 network.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func setTrustedServerCertificates(_ certificates: [Any]) -> Bool
```

#### Return Value

Returns [`false`](https://developer.apple.com/documentation/Swift/false) if any element in the array is not an object of type [`SecCertificate`](https://developer.apple.com/documentation/Security/SecCertificate) or if the OS fails to find a persistent reference for each element from the application’s keychain; else return [`true`](https://developer.apple.com/documentation/Swift/true).

#### Discussion

Your app must store the certificates in keychain access group `$(TeamIdentifierPrefix)com.apple.networkextensionsharing`. The OS uses [`SecItemCopyMatching(_:_:)`](https://developer.apple.com/documentation/Security/SecItemCopyMatching(_:_:)) to obtain a persistent reference to each certificate from the application’s keychain and uses it during EAP authentication.

The number of elements in the certificate array may not be more than 10.

## Parameters

- `certificates`: An array of   objects. The EAP peer uses these certificates to evaluate the trust of the server certificate chain.

## See Also

- [func setIdentity(SecIdentity) -> Bool](nehotspoteapsettings/setidentity(_:).md)
  Sets the client identity for EAP authentication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspoteapsettings/settrustedservercertificates(_:))*