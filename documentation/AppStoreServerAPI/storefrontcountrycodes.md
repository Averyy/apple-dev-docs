# storefrontCountryCodes

**Framework**: App Store Server API  
**Kind**: typealias

A list of storefront country codes you provide to limit the storefronts for a subscription-renewal-date extension.

**Availability**:
- App Store Server API 1.7+

## Declaration

```swift
[storefrontCountryCode] storefrontCountryCodes
```

#### Discussion

You provide the list of storefront country codes in the [`MassExtendRenewalDateRequest`](massextendrenewaldaterequest.md) to limit the storefronts in which the App Store extends the subscription renewal date. To indicate that the extension applies in all storefronts, omit the [`storefrontCountryCodes`](storefrontcountrycodes.md) object from the [`MassExtendRenewalDateRequest`](massextendrenewaldaterequest.md) object.

## See Also

- [type extendByDays](extendbydays.md)
  The number of days to extend the subscription renewal date.
- [type extendReasonCode](extendreasoncode.md)
  The code that represents the reason for the subscription-renewal-date extension.
- [type productId](../AppStoreServerNotifications/productId.md)
  The product identifier of the In-App Purchase.
- [type requestIdentifier](requestidentifier.md)
  A string that contains a unique identifier you provide to track each subscription-renewal-date extension request.
- [type storefrontCountryCode](storefrontcountrycode.md)
  The three-letter code that represents the country or region associated with the App Store storefront.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/storefrontcountrycodes)*