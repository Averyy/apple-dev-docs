# SKCloudServiceSetupOptionsKey

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

Keys to specify the types of setup options for a cloud service.

## Declaration

```swift
struct SKCloudServiceSetupOptionsKey
```

```c
typedef NSString * SKCloudServiceSetupOptionsKey;
```

## Topics

### Initializing
- [init(rawValue: String)](./skcloudservicesetupoptionskey/init%28rawvalue%29.md)
  Initializes a cloud service setup options key based on the provided raw value.
### Indicating Setup Options
- [static let action: SKCloudServiceSetupOptionsKey](./skcloudservicesetupoptionskey/action.md)
  A key that specifies the action for a setup entry point.
- [struct SKCloudServiceSetupAction](./skcloudservicesetupaction.md)
  A string used to specify the type of setup action to offer for a cloud service.
- [static let iTunesItemIdentifier: SKCloudServiceSetupOptionsKey](./skcloudservicesetupoptionskey/itunesitemidentifier.md)
  A key that specifies the iTunes Store item that the user is trying to access through the service.
- [static let affiliateToken: SKCloudServiceSetupOptionsKey](./skcloudservicesetupoptionskey/affiliatetoken.md)
  A key that specifies the iTunes Store affiliate token.
- [static let campaignToken: SKCloudServiceSetupOptionsKey](./skcloudservicesetupoptionskey/campaigntoken.md)
  A key that specifies the iTunes Store affiliate campaign token.
- [static let messageIdentifier: SKCloudServiceSetupOptionsKey](./skcloudservicesetupoptionskey/messageidentifier.md)
  A key that is used to select the main message presented to the user for this setup view.
- [struct SKCloudServiceSetupMessageIdentifier](./skcloudservicesetupmessageidentifier.md)
  Identifiers for the available messages the setup view can present to the user.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Loading the setup view
- [Offering Apple Music Subscription in Your App](./offering-apple-music-subscription-in-your-app.md)
  Allow eligible customers to subscribe to Apple Music.
- [func load(options: [SKCloudServiceSetupOptionsKey : Any], completionHandler: ((Bool, (any Error)?) -> Void)?)](./skcloudservicesetupviewcontroller/load%28options,completionhandler%29.md)
  Loads the cloud service setup view with the specified options.
- [class SKArcadeService](./skarcadeservice.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skcloudservicesetupoptionskey)*