# additionalValue(forKey:)

**Framework**: StoreKit  
**Kind**: method

Returns the object associated with the key.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func additionalValue(forKey key: String) -> Any?
```

#### Return Value

The associated value of the key.

#### Discussion

Additional values are values you use to verify and associate an app installation with an ad campaign. For more information, see [`SKAdNetwork`](skadnetwork.md).

## Parameters

- `key`: The string that identifies an additional value.

## See Also

- [var campaignToken: String?](skoverlay/appclipconfiguration/campaigntoken.md)
  A token you use to represent an ad campaign and measure its effectiveness.
- [var providerToken: String?](skoverlay/appclipconfiguration/providertoken.md)
  A token that represents the provider of an app promotion campaign, and that you use to measure the campaign’s effectiveness.
- [func setAdditionalValue(Any?, forKey: String)](skoverlay/appclipconfiguration/setadditionalvalue(_:forkey:).md)
  Sets an additional value for a key, such as a value for measuring the effectiveness of an ad campaign.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skoverlay/appclipconfiguration/additionalvalue(forkey:))*