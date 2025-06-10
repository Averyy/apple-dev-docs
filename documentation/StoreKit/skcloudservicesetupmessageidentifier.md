# SKCloudServiceSetupMessageIdentifier

**Framework**: StoreKit  
**Kind**: struct

Identifiers for the available messages the setup view can present to the user.

## Declaration

```swift
struct SKCloudServiceSetupMessageIdentifier
```

## Topics

### Initializing Identifiers
- [init(rawValue: String)](skcloudservicesetupmessageidentifier/init(rawvalue:).md)
  Initializes a cloud service setup message identifier based on the provided raw value.
### Message Identifiers
- [static let addMusic: SKCloudServiceSetupMessageIdentifier](skcloudservicesetupmessageidentifier/addmusic.md)
  Message identifier for adding music.
- [static let connect: SKCloudServiceSetupMessageIdentifier](skcloudservicesetupmessageidentifier/connect.md)
  Message identifier for connecting.
- [static let join: SKCloudServiceSetupMessageIdentifier](skcloudservicesetupmessageidentifier/join.md)
  Message identifier for joining.
- [static let playMusic: SKCloudServiceSetupMessageIdentifier](skcloudservicesetupmessageidentifier/playmusic.md)
  Message identifier for playing music.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [static let action: SKCloudServiceSetupOptionsKey](skcloudservicesetupoptionskey/action.md)
  A key that specifies the action for a setup entry point.
- [struct SKCloudServiceSetupAction](skcloudservicesetupaction.md)
  A string used to specify the type of setup action to offer for a cloud service.
- [static let iTunesItemIdentifier: SKCloudServiceSetupOptionsKey](skcloudservicesetupoptionskey/itunesitemidentifier.md)
  A key that specifies the iTunes Store item that the user is trying to access through the service.
- [static let affiliateToken: SKCloudServiceSetupOptionsKey](skcloudservicesetupoptionskey/affiliatetoken.md)
  A key that specifies the iTunes Store affiliate token.
- [static let campaignToken: SKCloudServiceSetupOptionsKey](skcloudservicesetupoptionskey/campaigntoken.md)
  A key that specifies the iTunes Store affiliate campaign token.
- [static let messageIdentifier: SKCloudServiceSetupOptionsKey](skcloudservicesetupoptionskey/messageidentifier.md)
  A key that is used to select the main message presented to the user for this setup view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skcloudservicesetupmessageidentifier)*