# identityWithServiceIdentifier:user:recordIdentifier:

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Type Method

Creates and returns a password credential identity object with a service identifier.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) identityWithServiceIdentifier:(ASCredentialServiceIdentifier *) serviceIdentifier user:(NSString *) user recordIdentifier:(NSString *) recordIdentifier;
```

## Parameters

- `serviceIdentifier`: The service identifier for the identity.
- `user`: The user associated with the identity.
- `recordIdentifier`: A string that your app can set to correlate the identity with an entry in your password database.

## See Also

### Creating a credential identity
- [init(serviceIdentifier: ASCredentialServiceIdentifier, user: String, recordIdentifier: String?)](./init%28serviceidentifier,user,recordidentifier%29.md)
  Initializes a password credential identity.
- [class ASCredentialServiceIdentifier](../ascredentialserviceidentifier.md)
  An identifier representing a particular service for which the user needs a credential, like a web site.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasswordcredentialidentity/identitywithserviceidentifier:user:recordidentifier:)*