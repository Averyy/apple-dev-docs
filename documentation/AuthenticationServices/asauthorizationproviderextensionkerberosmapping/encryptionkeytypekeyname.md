# encryptionKeyTypeKeyName

**Framework**: Authentication Services  
**Kind**: property

The key name of the Kerberos session key type number.

**Availability**:
- macOS 13.0+

## Declaration

```swift
var encryptionKeyTypeKeyName: String? { get set }
```

#### Discussion

Ensure the value for this key is the correct encryption type for the session key. See section 7 of [`RFC 3962`](https://developer.apple.comhttps://datatracker.ietf.org/doc/html/rfc3962) for more information.

## See Also

- [var clientNameKeyName: String?](asauthorizationproviderextensionkerberosmapping/clientnamekeyname.md)
  The key name of the Kerberos client name string.
- [var messageBufferKeyName: String?](asauthorizationproviderextensionkerberosmapping/messagebufferkeyname.md)
  The key name of the Base 64-encoded Kerberos AS-REP string.
- [var realmKeyName: String?](asauthorizationproviderextensionkerberosmapping/realmkeyname.md)
  The key name of the Kerberos realm string.
- [var serviceNameKeyName: String?](asauthorizationproviderextensionkerberosmapping/servicenamekeyname.md)
  The key name of the Kerberos service name string.
- [var sessionKeyKeyName: String?](asauthorizationproviderextensionkerberosmapping/sessionkeykeyname.md)
  The key name of the Kerberos session key.
- [var ticketKeyPath: String?](asauthorizationproviderextensionkerberosmapping/ticketkeypath.md)
  The keypath in the response JSON that uses this set of mappings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionkerberosmapping/encryptionkeytypekeyname)*