# accountDisplayName

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

The display name for the account.

**Availability**:
- macOS 13.0+

## Declaration

```swift
var accountDisplayName: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * accountDisplayName;
```

## Mentions

- [Configuring authentication with the identity provider (IdP)](../configuring-authentication-with-the-identity-provider-idp.md)

#### Discussion

The system uses this value for notifications and login prompts.

## See Also

### Obtaining the recommended configuration
- [var invalidCredentialPredicate: String?](./invalidcredentialpredicate.md)
  The predicate string that identifies invalid credential errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginconfiguration/accountdisplayname)*