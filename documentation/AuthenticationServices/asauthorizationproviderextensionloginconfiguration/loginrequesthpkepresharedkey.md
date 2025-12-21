# loginRequestHPKEPreSharedKey

**Framework**: Authentication Services  
**Kind**: property

**Availability**:
- macOS 15.0+

## Declaration

```swift
var loginRequestHPKEPreSharedKey: Data? { get set }
```

#### Discussion

The PreSharedKey to be used for HKPE for embedded login assertions. Setting this value will change the mode to PSK if the loginRequestHPKEPreSharedKeyID is also set. Must be at least 32 bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginconfiguration/loginrequesthpkepresharedkey)*