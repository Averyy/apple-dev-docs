# iTunesItemIdentifier

**Framework**: StoreKit  
**Kind**: property

A key that specifies the iTunes Store item that the user is trying to access through the service.

**Availability**:
- iOS 10.1+
- iPadOS 10.1+
- Mac Catalyst 13.1+
- tvOS 10.0+

## Declaration

```swift
static let iTunesItemIdentifier: SKCloudServiceSetupOptionsKey
```

#### Discussion

The only iTunes Store items that are supported are song, video, playlist, and album.

## See Also

- [static let action: SKCloudServiceSetupOptionsKey](skcloudservicesetupoptionskey/action.md)
  A key that specifies the action for a setup entry point.
- [struct SKCloudServiceSetupAction](skcloudservicesetupaction.md)
  A string used to specify the type of setup action to offer for a cloud service.
- [static let affiliateToken: SKCloudServiceSetupOptionsKey](skcloudservicesetupoptionskey/affiliatetoken.md)
  A key that specifies the iTunes Store affiliate token.
- [static let campaignToken: SKCloudServiceSetupOptionsKey](skcloudservicesetupoptionskey/campaigntoken.md)
  A key that specifies the iTunes Store affiliate campaign token.
- [static let messageIdentifier: SKCloudServiceSetupOptionsKey](skcloudservicesetupoptionskey/messageidentifier.md)
  A key that is used to select the main message presented to the user for this setup view.
- [struct SKCloudServiceSetupMessageIdentifier](skcloudservicesetupmessageidentifier.md)
  Identifiers for the available messages the setup view can present to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skcloudservicesetupoptionskey/itunesitemidentifier)*