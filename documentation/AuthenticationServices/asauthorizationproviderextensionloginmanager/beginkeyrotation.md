# beginKeyRotation(_:)

**Framework**: Authentication Services  
**Kind**: method

**Availability**:
- macOS 15.0+

## Declaration

```swift
func beginKeyRotation(_ keyType: ASAuthorizationProviderExtensionKeyType) -> SecKey?
```

#### Discussion

Generates a new key for the specified platform SSO key type using the strongest supported key strength returning the new key.  Nil is returned if there is an error generating the new key.

## Parameters

- `keyType`: The key type to retrieve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginmanager/beginkeyrotation(_:))*