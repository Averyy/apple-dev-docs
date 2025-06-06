# setAdditionalValue(_:forKey:)

**Framework**: StoreKit  
**Kind**: method

Sets an additional value for a key; for example, a value for measuring the effectiveness of an ad campaign.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func setAdditionalValue(_ value: Any?, forKey key: String)
```

#### Discussion

Set additional values to verify and associate an app installation with an ad campaign. For more information, see [`SKAdNetwork`](skadnetwork.md).

## Parameters

- `value`: The value to associate with the  .
- `key`: The string that identifies an additional value.

## See Also

- [var campaignToken: String?](skoverlay/appconfiguration/campaigntoken.md)
  A token you use to represent an ad campaign and measure its effectiveness.
- [var providerToken: String?](skoverlay/appconfiguration/providertoken.md)
  A token that represents the provider of an app promotion campaign, and that you use to measure the campaign’s effectiveness.
- [func additionalValue(forKey: String) -> Any?](skoverlay/appconfiguration/additionalvalue(forkey:).md)
  Returns the object associated with the key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skoverlay/appconfiguration/setadditionalvalue(_:forkey:))*