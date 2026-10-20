# messageIdentifier

**Framework**: StoreKit  
**Kind**: property  
**Role**: Type Property

A key that is used to select the main message presented to the user for this setup view.

**Availability**:
- iOS 11.0+ - Deprecated in 18.0
- iPadOS 11.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- tvOS 11.0+ - Deprecated in 18.0

> **Deprecated**: Use the messageIdentifier property of MusicSubscriptionOffer.Options from MusicKit.

## Declaration

```swift
static let messageIdentifier: SKCloudServiceSetupOptionsKey
```

```c
extern SKCloudServiceSetupOptionsKey const SKCloudServiceSetupOptionsMessageIdentifierKey;
```

## Mentions

- [Offering Apple Music Subscription in Your App](../offering-apple-music-subscription-in-your-app.md)

#### Discussion

If this key is missing, the setup view is configured as if it is using the [`join`](../skcloudservicesetupmessageidentifier/join.md) key by default.

## See Also

### Indicating Setup Options
- [static let action: SKCloudServiceSetupOptionsKey](./action.md)
  A key that specifies the action for a setup entry point.
- [struct SKCloudServiceSetupAction](../skcloudservicesetupaction.md)
  A string used to specify the type of setup action to offer for a cloud service.
- [static let iTunesItemIdentifier: SKCloudServiceSetupOptionsKey](./itunesitemidentifier.md)
  A key that specifies the iTunes Store item that the user is trying to access through the service.
- [static let affiliateToken: SKCloudServiceSetupOptionsKey](./affiliatetoken.md)
  A key that specifies the iTunes Store affiliate token.
- [static let campaignToken: SKCloudServiceSetupOptionsKey](./campaigntoken.md)
  A key that specifies the iTunes Store affiliate campaign token.
- [struct SKCloudServiceSetupMessageIdentifier](../skcloudservicesetupmessageidentifier.md)
  Identifiers for the available messages the setup view can present to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skcloudservicesetupoptionskey/messageidentifier)*