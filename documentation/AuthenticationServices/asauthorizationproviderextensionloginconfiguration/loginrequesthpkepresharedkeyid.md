# loginRequestHPKEPreSharedKeyID

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- macOS 15.0+

## Declaration

```swift
var loginRequestHPKEPreSharedKeyID: Data? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSData * loginRequestHPKEPreSharedKeyID;
```

#### Discussion

The PreSharedKey Id to be used for HPKE PSK for embedded login assertions.  This is required if the loginRequestHPKEPreSharedKey is set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginconfiguration/loginrequesthpkepresharedkeyid)*