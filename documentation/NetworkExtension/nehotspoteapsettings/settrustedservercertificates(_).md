# setTrustedServerCertificates(_:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) setTrustedServerCertificates:(NSArray *) certificates;
```

## Return Value

Returns [`false`](../../Swift/false.md) if any element in the array is not an object of type [`SecCertificate`](../../Security/seccertificate.md) or if the OS fails to find a persistent reference for each element from the application’s keychain; else return [`true`](../../Swift/true.md).

## Discussion

Your app must store the certificates in keychain access group `$(TeamIdentifierPrefix)com.apple.networkextensionsharing`. The OS uses [`SecItemCopyMatching(_:_:)`](../../Security/secitemcopymatching%28_,_%29.md) to obtain a persistent reference to each certificate from the application’s keychain and uses it during EAP authentication.

The number of elements in the certificate array may not be more than 10.

## Parameters

- `certificates`: An array of [`SecCertificate`](../../Security/seccertificate.md) objects. The EAP peer uses these certificates to evaluate the trust of the server certificate chain.

## See Also

### Setting Keychain-based EAP Properties
- [func setIdentity(SecIdentity) -> Bool](./setidentity%28_%29.md)
  Sets the client identity for EAP authentication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspoteapsettings/settrustedservercertificates(_:))*