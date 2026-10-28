# credentialWithUser:password:

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Type Method

Creates a password credential instance with a given user name and password.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```objc
+ (instancetype) credentialWithUser:(NSString *) user password:(NSString *) password;
```

## Return Value

The credential object.

## Parameters

- `user`: The username for the credential.
- `password`: The password for the credential.

## See Also

### Creating a credential
- [init(user: String, password: String)](./init%28user,password%29.md)
  Initializes a password credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasswordcredential/credentialwithuser:password:)*