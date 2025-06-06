# campaignToken

**Framework**: StoreKit  
**Kind**: property

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

#### Discussion

A campaign token is a 40-byte string that represents an ad campaign. By setting the `campaignToken`, you can measure the effectiveness of an Apple Services Performance Partners Program link or an App Store Connect Analytics campaign.

For more information, see [`Apple Services Performance Partners Program`](https://developer.apple.comhttps://apple.com/itunes/affiliates) and [`App Store Connect`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/iTunesConnect_Guide/Chapters/About.html#//apple_ref/doc/uid/TP40011225).

## See Also

- [var providerToken: String?](skoverlay/appclipconfiguration/providertoken.md)
  A token that represents the provider of an app promotion campaign, and that you use to measure the campaign’s effectiveness.
- [func setAdditionalValue(Any?, forKey: String)](skoverlay/appclipconfiguration/setadditionalvalue(_:forkey:).md)
  Sets an additional value for a key, such as a value for measuring the effectiveness of an ad campaign.
- [func additionalValue(forKey: String) -> Any?](skoverlay/appclipconfiguration/additionalvalue(forkey:).md)
  Returns the object associated with the key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skoverlay/appclipconfiguration/campaigntoken)*