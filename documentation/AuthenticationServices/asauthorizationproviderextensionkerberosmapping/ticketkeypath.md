# ticketKeyPath

**Framework**: Authentication Services  
**Kind**: property

The keypath in the response JSON that uses this set of mappings.

**Availability**:
- macOS 13.0+

## Declaration

```swift
var ticketKeyPath: String? { get set }
```

#### Discussion

If the response tokens from the login contain this keypath, the system uses this mapping to create a Kerberos ticket. The expected response is a JSON dictionary with the supplied key names containing Kerberos ticket values.

## See Also

- [var clientNameKeyName: String?](asauthorizationproviderextensionkerberosmapping/clientnamekeyname.md)
  The key name of the Kerberos client name string.
- [var encryptionKeyTypeKeyName: String?](asauthorizationproviderextensionkerberosmapping/encryptionkeytypekeyname.md)
  The key name of the Kerberos session key type number.
- [var messageBufferKeyName: String?](asauthorizationproviderextensionkerberosmapping/messagebufferkeyname.md)
  The key name of the Base 64-encoded Kerberos AS-REP string.
- [var realmKeyName: String?](asauthorizationproviderextensionkerberosmapping/realmkeyname.md)
  The key name of the Kerberos realm string.
- [var serviceNameKeyName: String?](asauthorizationproviderextensionkerberosmapping/servicenamekeyname.md)
  The key name of the Kerberos service name string.
- [var sessionKeyKeyName: String?](asauthorizationproviderextensionkerberosmapping/sessionkeykeyname.md)
  The key name of the Kerberos session key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionkerberosmapping/ticketkeypath)*