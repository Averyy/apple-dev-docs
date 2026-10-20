# additionalValue(forKey:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (id) additionalValueForKey:(NSString *) key;
```

#### Return Value

The associated value of the key.

#### Discussion

Additional values are values you use to verify and associate an app installation with an ad campaign. For more information, see [`SKAdNetwork`](../../skadnetwork.md).

## Parameters

- `key`: The string that identifies an additional value.

## See Also

### Verifying Advertising Campaigns
- [var campaignToken: String?](./campaigntoken.md)
  A token you use to represent an ad campaign and measure its effectiveness.
- [var providerToken: String?](./providertoken.md)
  A token that represents the provider of an app promotion campaign, and that you use to measure the campaign’s effectiveness.
- [func setAdditionalValue(Any?, forKey: String)](./setadditionalvalue%28_,forkey%29.md)
  Sets an additional value for a key, such as a value for measuring the effectiveness of an ad campaign.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skoverlay/appclipconfiguration/additionalvalue(forkey:))*