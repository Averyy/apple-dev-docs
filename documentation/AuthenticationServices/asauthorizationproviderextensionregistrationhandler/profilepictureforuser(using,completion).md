# profilePictureForUser(using:completion:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 26.0+

## Declaration

```swift
optional func profilePictureForUser(using loginManager: ASAuthorizationProviderExtensionLoginManager, completion: @escaping @Sendable (Data) -> Void)
```

```swift
optional func profilePictureForUser(using loginManager: ASAuthorizationProviderExtensionLoginManager) async -> Data
```

```objc
- (void) profilePictureForUserUsingLoginManager:(ASAuthorizationProviderExtensionLoginManager *) loginManager completion:(void (^)(NSData *jpegData)) completion;
```

#### Discussion

Request the profile picture for the current user in jpeg format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionregistrationhandler/profilepictureforuser(using:completion:))*