# init(relyingPartyIdentifier:userName:credentialID:userHandle:recordIdentifier:)

**Framework**: Authentication Services  
**Kind**: init  
**Role**: Initializer

Creates and initializes a passkey credential identity.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(relyingPartyIdentifier: String, userName: String, credentialID: Data, userHandle: Data, recordIdentifier: String?)
```

```objc
+ (instancetype) identityWithRelyingPartyIdentifier:(NSString *) relyingPartyIdentifier userName:(NSString *) userName credentialID:(NSData *) credentialID userHandle:(NSData *) userHandle recordIdentifier:(NSString *) recordIdentifier;
```

#### Return Value

The new credential identity object.

## See Also

### Creating a credential identity
- [convenience init(relyingPartyIdentifier: String, userName: String, credentialID: Data, userHandle: Data, recordIdentifier: String?)](./init%28relyingpartyidentifier,username,credentialid,userhandle,recordidentifier%29-7u7p1.md)
  Initializes a passkey credential identity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeycredentialidentity/init(relyingpartyidentifier:username:credentialid:userhandle:recordidentifier:)-9iuhb)*