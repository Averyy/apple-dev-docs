# iTunesItemIdentifier

**Framework**: StoreKit  
**Kind**: property  
**Role**: Type Property

A key that specifies the iTunes Store item that the user is trying to access through the service.

**Availability**:
- iOS 10.1+ - Deprecated in 18.0
- iPadOS 10.1+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- tvOS 10.0+ - Deprecated in 18.0

> **Deprecated**: Use the itemID property of MusicSubscriptionOffer.Options from MusicKit.

## Declaration

```swift
static let iTunesItemIdentifier: SKCloudServiceSetupOptionsKey
```

```c
extern SKCloudServiceSetupOptionsKey const SKCloudServiceSetupOptionsITunesItemIdentifierKey;
```

## Discussion

The only iTunes Store items that are supported are song, video, playlist, and album.

## See Also

### Indicating Setup Options
- [static let action: SKCloudServiceSetupOptionsKey](./action.md)
  A key that specifies the action for a setup entry point.
- [struct SKCloudServiceSetupAction](../skcloudservicesetupaction.md)
  A string used to specify the type of setup action to offer for a cloud service.
- [static let affiliateToken: SKCloudServiceSetupOptionsKey](./affiliatetoken.md)
  A key that specifies the iTunes Store affiliate token.
- [static let campaignToken: SKCloudServiceSetupOptionsKey](./campaigntoken.md)
  A key that specifies the iTunes Store affiliate campaign token.
- [static let messageIdentifier: SKCloudServiceSetupOptionsKey](./messageidentifier.md)
  A key that is used to select the main message presented to the user for this setup view.
- [struct SKCloudServiceSetupMessageIdentifier](../skcloudservicesetupmessageidentifier.md)
  Identifiers for the available messages the setup view can present to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skcloudservicesetupoptionskey/itunesitemidentifier)*