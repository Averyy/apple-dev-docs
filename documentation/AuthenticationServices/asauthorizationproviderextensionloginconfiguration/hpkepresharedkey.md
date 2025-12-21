# hpkePreSharedKey

**Framework**: Authentication Services  
**Kind**: property

**Availability**:
- macOS 15.0+

## Declaration

```swift
var hpkePreSharedKey: Data? { get set }
```

#### Discussion

The PreSharedKey to be used for HKPE. Setting this value will change the mode to PSK or AuthPSK if the hpkeAuthPublicKey is also set. Must be at least 32 bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginconfiguration/hpkepresharedkey)*