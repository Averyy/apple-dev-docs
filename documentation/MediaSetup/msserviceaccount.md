# MSServiceAccount

**Framework**: Media Setup  
**Kind**: class

Account details for accessing a streaming media service.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
class MSServiceAccount
```

## Topics

### Presenting Account Information to the User
- [init(serviceName: String, accountName: String)](msserviceaccount/init(servicename:accountname:).md)
  Creates a new account.
- [var serviceName: String](msserviceaccount/servicename.md)
  The localized name of the streaming media service.
- [var accountName: String](msserviceaccount/accountname.md)
  The user’s display name, email address, or other identifier in a streaming media service.
### Providing Parameters for an OAuth Request
- [var authorizationTokenURL: URL?](msserviceaccount/authorizationtokenurl.md)
  A URL the system can access to request an OAuth token for the user’s HomePod speakers.
- [var authorizationScope: String?](msserviceaccount/authorizationscope.md)
  A list of permissions for the token request.
- [var clientID: String?](msserviceaccount/clientid.md)
  A user identifier for the token request.
- [var clientSecret: String?](msserviceaccount/clientsecret.md)
  A string that authenticates the user’s setup request.
- [var configurationURL: URL?](msserviceaccount/configurationurl.md)
  The path to access the configuration endpoint of your streaming media service for HomePod.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MSSetupSession](mssetupsession.md)
  An object that manages the transfer of configuration information between your app, the system, your media service, and HomePod speakers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediasetup/msserviceaccount)*