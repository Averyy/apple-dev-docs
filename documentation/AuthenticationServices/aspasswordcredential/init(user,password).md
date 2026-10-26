# init(user:password:)

**Framework**: Authentication Services  
**Kind**: init  
**Role**: Initializer

Initializes a password credential.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(user: String, password: String)
```

```objc
- (instancetype) initWithUser:(NSString *) user password:(NSString *) password;
```

## Parameters

- `user`: The username associated with the credential.
- `password`: The password associated with the credential.

## See Also

### Creating a credential
- [+ credentialWithUser:password:](./credentialwithuser_password_.md)
  Creates a password credential instance with a given user name and password.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasswordcredential/init(user:password:))*