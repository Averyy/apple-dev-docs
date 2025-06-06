# setIdentity(_:)

**Framework**: Network Extension  
**Kind**: method

Sets the client identity for EAP authentication.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func setIdentity(_ identity: SecIdentity) -> Bool
```

#### Return Value

Returns `false` if the parameter is not an object of `SecIdentityRef` type or if the persistent reference is not found in the application’s keychain; otherwise returns `true`.

#### Discussion

Your app must store `SecIdentity` in the keychain access group $`(Team​Identifier​Prefix)com​.apple​.networkextensionsharing`. The OS uses [`SecItemCopyMatching(_:_:)`](https://developer.apple.com/documentation/Security/SecItemCopyMatching(_:_:)) to obtain a persistent reference to this identity from the application’s keychain and uses it during EAP authentication.

## Parameters

- `identity`: The EAP peer identity, a   object that contains a   object and an associated   object.

## See Also

- [func setTrustedServerCertificates([Any]) -> Bool](nehotspoteapsettings/settrustedservercertificates(_:).md)
  Sets trusted EAP server certificates for an enterprise Wi-Fi or Hotspot 2.0 network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspoteapsettings/setidentity(_:))*