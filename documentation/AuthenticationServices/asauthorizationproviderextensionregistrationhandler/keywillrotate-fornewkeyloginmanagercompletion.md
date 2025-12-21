# keyWillRotate(for:newKey:loginManager:completion:)

**Framework**: Authentication Services  
**Kind**: method

**Availability**:
- macOS 15.0+

## Declaration

```swift
optional func keyWillRotate(for keyType: ASAuthorizationProviderExtensionKeyType, newKey: SecKey, loginManager: ASAuthorizationProviderExtensionLoginManager) async -> Bool
```

#### Discussion

The specified keyType will rotate to a new key. The rotation is complete when the completion handler is called.  This is only called by the system for automatic key rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionregistrationhandler/keywillrotate(for:newkey:loginmanager:completion:))*