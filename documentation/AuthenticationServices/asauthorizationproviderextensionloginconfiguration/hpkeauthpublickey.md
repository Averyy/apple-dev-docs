# hpkeAuthPublicKey

**Framework**: Authentication Services  
**Kind**: property

**Availability**:
- macOS 15.0+

## Declaration

```swift
var hpkeAuthPublicKey: SecKey? { get set }
```

#### Discussion

The Authentication public key to be used for HPKE.  Setting this value with changet the mode to Auth or AuthPSK if the hpkePreSharedKey is also set.  This public key is used to authenticate HPKE responses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginconfiguration/hpkeauthpublickey)*