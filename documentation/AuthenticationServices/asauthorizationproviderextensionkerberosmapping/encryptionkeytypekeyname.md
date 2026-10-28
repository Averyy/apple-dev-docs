# encryptionKeyTypeKeyName

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

The key name of the Kerberos session key type number.

**Availability**:
- macOS 13.0+

## Declaration

```swift
var encryptionKeyTypeKeyName: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * encryptionKeyTypeKeyName;
```

## Discussion

Ensure the value for this key is the correct encryption type for the session key. See section 7 of [RFC 3962](https://datatracker.ietf.org/doc/html/rfc3962) for more information.

## See Also

### Getting the properties
- [var clientNameKeyName: String?](./clientnamekeyname.md)
  The key name of the Kerberos client name string.
- [var messageBufferKeyName: String?](./messagebufferkeyname.md)
  The key name of the Base 64-encoded Kerberos AS-REP string.
- [var realmKeyName: String?](./realmkeyname.md)
  The key name of the Kerberos realm string.
- [var serviceNameKeyName: String?](./servicenamekeyname.md)
  The key name of the Kerberos service name string.
- [var sessionKeyKeyName: String?](./sessionkeykeyname.md)
  The key name of the Kerberos session key.
- [var ticketKeyPath: String?](./ticketkeypath.md)
  The keypath in the response JSON that uses this set of mappings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionkerberosmapping/encryptionkeytypekeyname)*