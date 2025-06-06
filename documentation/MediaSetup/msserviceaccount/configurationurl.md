# configurationURL

**Framework**: Media Setup  
**Kind**: property

The path to access the configuration endpoint of your streaming media service for HomePod.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
var configurationURL: URL? { get set }
```

## See Also

- [var authorizationTokenURL: URL?](msserviceaccount/authorizationtokenurl.md)
  A URL the system can access to request an OAuth token for the user’s HomePod speakers.
- [var authorizationScope: String?](msserviceaccount/authorizationscope.md)
  A list of permissions for the token request.
- [var clientID: String?](msserviceaccount/clientid.md)
  A user identifier for the token request.
- [var clientSecret: String?](msserviceaccount/clientsecret.md)
  A string that authenticates the user’s setup request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediasetup/msserviceaccount/configurationurl)*