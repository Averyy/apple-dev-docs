# transports

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

The array of transport types.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
var transports: [ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor.Transport] { get set }
```

```objc
@property (nonatomic) NSArray<NSString *> * transports;
```

## See Also

### Creating the descriptor
- [init(credentialID: Data, transports: [ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor.Transport])](./init%28credentialid,transports%29.md)
  Creates the object with the credential ID and the array of transports.
- [ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor.Transport](./transport.md)
  A structure that defines the security key credential transport type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationsecuritykeypublickeycredentialdescriptor/transports)*