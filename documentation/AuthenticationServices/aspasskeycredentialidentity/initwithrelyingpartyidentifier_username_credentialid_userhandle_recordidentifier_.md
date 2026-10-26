# initWithRelyingPartyIdentifier:userName:credentialID:userHandle:recordIdentifier:

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

Initializes a passkey credential identity.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```objc
- (instancetype) initWithRelyingPartyIdentifier:(NSString *) relyingPartyIdentifier userName:(NSString *) userName credentialID:(NSData *) credentialID userHandle:(NSData *) userHandle recordIdentifier:(NSString *) recordIdentifier;
```

#### Return Value

The initialized credential identity.

## Parameters

- `relyingPartyIdentifier`: The relying party identifier associated with this credential.
- `userName`: The username associated with this credential.
- `credentialID`: The credential identifier for this credential.
- `userHandle`: The user handle associated with this credential.
- `recordIdentifier`: The record identifier for this credential.

## See Also

### Creating a credential identity
- [convenience init(relyingPartyIdentifier: String, userName: String, credentialID: Data, userHandle: Data, recordIdentifier: String?)](./init%28relyingpartyidentifier,username,credentialid,userhandle,recordidentifier%29-9iuhb.md)
  Creates and initializes a passkey credential identity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeycredentialidentity/initwithrelyingpartyidentifier:username:credentialid:userhandle:recordidentifier:)*