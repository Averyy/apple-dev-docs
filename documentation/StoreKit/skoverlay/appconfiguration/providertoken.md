# providerToken

**Framework**: StoreKit  
**Kind**: property

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

#### Discussion

When you set a provider token, you must also set the [`campaignToken`](skoverlay/appconfiguration/campaigntoken.md).

When promoting your own apps, set your own provider token using `providerToken`. This allows you to track a promotion’s effectiveness independently from any affiliate campaign that shares the same campaign token.

When promoting apps by other developers, set `providerToken` using their provider token. This allows those developers to track the effectiveness of your App Store Connect Analytics campaign.

## See Also

- [var campaignToken: String?](skoverlay/appconfiguration/campaigntoken.md)
  A token you use to represent an ad campaign and measure its effectiveness.
- [func setAdditionalValue(Any?, forKey: String)](skoverlay/appconfiguration/setadditionalvalue(_:forkey:).md)
  Sets an additional value for a key; for example, a value for measuring the effectiveness of an ad campaign.
- [func additionalValue(forKey: String) -> Any?](skoverlay/appconfiguration/additionalvalue(forkey:).md)
  Returns the object associated with the key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skoverlay/appconfiguration/providertoken)*