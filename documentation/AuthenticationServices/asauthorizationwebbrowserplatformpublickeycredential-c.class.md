# ASAuthorizationWebBrowserPlatformPublicKeyCredential

**Framework**: Authentication Services  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- visionOS 1.1+

## Declaration

```objc
@interface ASAuthorizationWebBrowserPlatformPublicKeyCredential : NSObject
```

## Topics

### Instance Properties
- [credentialID](./asauthorizationwebbrowserplatformpublickeycredential-c.class/credentialid.md)
  The identifier the operating system uses for this credential.
- [customTitle](./asauthorizationwebbrowserplatformpublickeycredential-c.class/customtitle.md)
  A string the person can supply to describe this credential.
- [name](./asauthorizationwebbrowserplatformpublickeycredential-c.class/name.md)
  The user name for the account associated with this credential.
- [providerName](./asauthorizationwebbrowserplatformpublickeycredential-c.class/providername.md)
  The name of the app that manages this credential, or “iCloud Keychain” if it’s the operating system.
- [relyingParty](./asauthorizationwebbrowserplatformpublickeycredential-c.class/relyingparty.md)
  The relying party that issues challenges for this credential.
- [userHandle](./asauthorizationwebbrowserplatformpublickeycredential-c.class/userhandle.md)
  A unique identifier for the user account at the relying party.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Using passkeys
- [- platformCredentialsForRelyingParty:completionHandler:](./asauthorizationwebbrowserpublickeycredentialmanager/platformcredentialsforrelyingparty_completionhandler_.md)
  Gets a list of passkeys available for authenticating with the given relying party.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationwebbrowserplatformpublickeycredential-c.class)*