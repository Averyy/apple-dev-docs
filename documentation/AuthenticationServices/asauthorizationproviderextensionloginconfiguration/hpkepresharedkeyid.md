# hpkePreSharedKeyID

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- macOS 15.0+

## Declaration

```swift
var hpkePreSharedKeyID: Data? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSData * hpkePreSharedKeyID;
```

#### Discussion

The PreSharedKey Id to be used for HPKE PSK or AuthPSK mode.  This is requred if the hpkePreSharedKey is set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginconfiguration/hpkepresharedkeyid)*