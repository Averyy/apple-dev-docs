# realmKeyName

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

The key name of the Kerberos realm string.

**Availability**:
- macOS 13.0+

## Declaration

```swift
var realmKeyName: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * realmKeyName;
```

## See Also

### Getting the properties
- [var clientNameKeyName: String?](./clientnamekeyname.md)
  The key name of the Kerberos client name string.
- [var encryptionKeyTypeKeyName: String?](./encryptionkeytypekeyname.md)
  The key name of the Kerberos session key type number.
- [var messageBufferKeyName: String?](./messagebufferkeyname.md)
  The key name of the Base 64-encoded Kerberos AS-REP string.
- [var serviceNameKeyName: String?](./servicenamekeyname.md)
  The key name of the Kerberos service name string.
- [var sessionKeyKeyName: String?](./sessionkeykeyname.md)
  The key name of the Kerberos session key.
- [var ticketKeyPath: String?](./ticketkeypath.md)
  The keypath in the response JSON that uses this set of mappings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionkerberosmapping/realmkeyname)*