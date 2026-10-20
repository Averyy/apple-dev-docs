# campaignToken

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

A token you use to represent an ad campaign and measure its effectiveness.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
var campaignToken: String? { get set }
```

```objc
@property (nonatomic, retain, nullable) NSString * campaignToken;
```

#### Discussion

A campaign token is a 40-byte string that represents an ad campaign. By setting the `campaignToken`, you can measure the effectiveness of an Apple Services Performance Partners Program link or an App Store Connect Analytics campaign.

For more information, see [Apple Services Performance Partners Program](https://apple.com/itunes/affiliates) and [App Store Connect](https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/iTunesConnect_Guide/Chapters/About.html#//apple_ref/doc/uid/TP40011225).

## See Also

### Verifying Advertising Campaigns
- [var providerToken: String?](./providertoken.md)
  A token that represents the provider of an app promotion campaign, and that you use to measure the campaign’s effectiveness.
- [func setAdditionalValue(Any?, forKey: String)](./setadditionalvalue%28_,forkey%29.md)
  Sets an additional value for a key; for example, a value for measuring the effectiveness of an ad campaign.
- [func additionalValue(forKey: String) -> Any?](./additionalvalue%28forkey%29.md)
  Returns the object associated with the key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skoverlay/appconfiguration/campaigntoken)*