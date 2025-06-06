# registerAppForAdNetworkAttribution()

**Framework**: StoreKit  
**Kind**: method

Verifies the first launch of an app installed as a result of an ad.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.1+

## Declaration

```swift
class func registerAppForAdNetworkAttribution()
```

#### Discussion

Apps that an ad network campaign advertise call this method or [`updateConversionValue(_:)`](skadnetwork/updateconversionvalue(_:).md) when the app first launches. Both methods generate an install notification, which is the cryptographically signed data that validates that a user installed and launched this app as a result of an ad.

In iOS 15.4 and earlier, the first call to [`registerAppForAdNetworkAttribution()`](skadnetwork/registerappforadnetworkattribution().md) generates the notification if the device has attribution data for that app, and starts a 24-hour timer. Subsequent calls to this method have no effect, unless the ad already has a conversion value set, in which case calling [`registerAppForAdNetworkAttribution()`](skadnetwork/registerappforadnetworkattribution().md) resets the conversion value to `0`. You may, however, call [`updateConversionValue(_:)`](skadnetwork/updateconversionvalue(_:).md) to provide an updated conversion value and restart the timer.

The device sends one or more install notifications to ad network postback URLs within 0-24 hours after the timer expires. For more information about attribution-winning and non-winning postbacks, see [`Receiving ad attributions and postbacks`](receiving-ad-attributions-and-postbacks.md).

Ad networks must verify the postback after receiving it. For more information, see [`Verifying an install-validation postback`](verifying-an-install-validation-postback.md).

## See Also

- [class func updateConversionValue(Int)](skadnetwork/updateconversionvalue(_:).md)
  Updates the conversion value and verifies the first launch of an app installed as a result of an ad.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skadnetwork/registerappforadnetworkattribution())*