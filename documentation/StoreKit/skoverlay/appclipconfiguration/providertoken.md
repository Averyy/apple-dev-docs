# providerToken

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

A token that represents the provider of an app promotion campaign, and that you use to measure the campaign’s effectiveness.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
var providerToken: String? { get set }
```

```objc
@property (nonatomic, retain, nullable) NSString * providerToken;
```

## Discussion

When you set a provider token, you must also set the [`campaignToken`](../appconfiguration/campaigntoken.md).

When promoting your own apps, set your own provider token using `providerToken`. This allows you to track a promotion’s effectiveness independently from any affiliate campaign that shares the same campaign token.

When promoting apps by other developers, set `providerToken` using their provider token. This allows those developers to track the effectiveness of your App Store Connect Analytics campaign.

## See Also

### Verifying Advertising Campaigns
- [var campaignToken: String?](./campaigntoken.md)
  A token you use to represent an ad campaign and measure its effectiveness.
- [func setAdditionalValue(Any?, forKey: String)](./setadditionalvalue%28_,forkey%29.md)
  Sets an additional value for a key, such as a value for measuring the effectiveness of an ad campaign.
- [func additionalValue(forKey: String) -> Any?](./additionalvalue%28forkey%29.md)
  Returns the object associated with the key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skoverlay/appclipconfiguration/providertoken)*