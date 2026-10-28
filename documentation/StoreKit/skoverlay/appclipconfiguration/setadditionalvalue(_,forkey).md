# setAdditionalValue(_:forKey:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Instance Method

Sets an additional value for a key, such as a value for measuring the effectiveness of an ad campaign.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func setAdditionalValue(_ value: Any?, forKey key: String)
```

```objc
- (void) setAdditionalValue:(id) value forKey:(NSString *) key;
```

## Discussion

Set additional values to verify and associate an app installation with an ad campaign. For more information, see [`SKAdNetwork`](../../skadnetwork.md).

## Parameters

- `value`: The value to associate with the `key`.
- `key`: The string that identifies an additional value.

## See Also

### Verifying Advertising Campaigns
- [var campaignToken: String?](./campaigntoken.md)
  A token you use to represent an ad campaign and measure its effectiveness.
- [var providerToken: String?](./providertoken.md)
  A token that represents the provider of an app promotion campaign, and that you use to measure the campaign’s effectiveness.
- [func additionalValue(forKey: String) -> Any?](./additionalvalue%28forkey%29.md)
  Returns the object associated with the key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skoverlay/appclipconfiguration/setadditionalvalue(_:forkey:))*