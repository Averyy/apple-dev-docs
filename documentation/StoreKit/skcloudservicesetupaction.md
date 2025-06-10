# SKCloudServiceSetupAction

**Framework**: StoreKit  
**Kind**: struct

A string used to specify the type of setup action to offer for a cloud service.

## Declaration

```swift
struct SKCloudServiceSetupAction
```

## Topics

### Initializers
- [init(rawValue: String)](skcloudservicesetupaction/init(rawvalue:).md)
  Initializes a setup action to offer for a cloud service using the specified value.
### Type Properties
- [static let subscribe: SKCloudServiceSetupAction](skcloudservicesetupaction/subscribe.md)
  A subscribe action in a cloud service setup view, such as an offer to subscribe to Apple Music.

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
- [static let iTunesItemIdentifier: SKCloudServiceSetupOptionsKey](skcloudservicesetupoptionskey/itunesitemidentifier.md)
  A key that specifies the iTunes Store item that the user is trying to access through the service.
- [static let affiliateToken: SKCloudServiceSetupOptionsKey](skcloudservicesetupoptionskey/affiliatetoken.md)
  A key that specifies the iTunes Store affiliate token.
- [static let campaignToken: SKCloudServiceSetupOptionsKey](skcloudservicesetupoptionskey/campaigntoken.md)
  A key that specifies the iTunes Store affiliate campaign token.
- [static let messageIdentifier: SKCloudServiceSetupOptionsKey](skcloudservicesetupoptionskey/messageidentifier.md)
  A key that is used to select the main message presented to the user for this setup view.
- [struct SKCloudServiceSetupMessageIdentifier](skcloudservicesetupmessageidentifier.md)
  Identifiers for the available messages the setup view can present to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skcloudservicesetupaction)*