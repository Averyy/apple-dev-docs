# updateConversionValue(_:)

**Framework**: StoreKit  
**Kind**: method

Updates the conversion value and verifies the first launch of an app installed as a result of an ad.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class func updateConversionValue(_ conversionValue: Int)
```

## Mentions

- [SKAdNetwork 2 release notes](skadnetwork-2-release-notes.md)

#### Discussion

Apps that ad networks advertise call [`updateConversionValue(_:)`](skadnetwork/updateconversionvalue(_:).md) or [`registerAppForAdNetworkAttribution()`](skadnetwork/registerappforadnetworkattribution().md) when the app first launches, to register the attribution.

> ❗ **Important**:  Provide a valid conversion value within the range of `>=0` and `<=63` when calling [`updateConversionValue(_:)`](skadnetwork/updateconversionvalue(_:).md) to register the attribution. Invalid conversion values cause the method to fail, and the conversion to fail to register.

Apps may call [`updateConversionValue(_:)`](skadnetwork/updateconversionvalue(_:).md) again within a rolling 24-hour period to update the conversion value. Calling this method serves two purposes:

- It registers the attribution by generating an install notification — the cryptographically signed data that confirms that a user installed and launched this app as a result of an ad.
- It enables the app to provide and update a conversion value.

Conversion values are a 6-bit value that the ad network or the app defines. The app decides when to update the value, which it can do any number of times before a rolling 24-hour timer expires. The 24-hour timer restarts each time the app calls this method with a valid conversion value greater than the previous value. When the timer expires, the conversion value is final and subsequent calls to [`updateConversionValue(_:)`](skadnetwork/updateconversionvalue(_:).md) have no effect.

The device sends the install notification postback to the ad network’s URL within 0-24 hours after the timer expires. The postback only contains the final conversion value if sending the data meets Apple’s privacy threshold. Only postbacks with an ad attribution can contain a conversion value; non-winning postbacks don’t include a conversion value. For more information, see [`Receiving ad attributions and postbacks`](receiving-ad-attributions-and-postbacks.md).

Ad networks must verify the postback after receiving it. See [`Verifying an install-validation postback`](verifying-an-install-validation-postback.md) for more information.

## Parameters

- `conversionValue`: An unsigned 6-bit value (  and  ). The app or the ad network determines the meaning of the value. The default value is  .

## See Also

- [class func registerAppForAdNetworkAttribution()](skadnetwork/registerappforadnetworkattribution.md)
  Verifies the first launch of an app installed as a result of an ad.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skadnetwork/updateconversionvalue(_:))*