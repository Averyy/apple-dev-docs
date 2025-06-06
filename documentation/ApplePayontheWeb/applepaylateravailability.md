# ApplePayLaterAvailability

**Framework**: Apple Pay on the Web  
**Kind**: enum

Values you use to enable or disable Apple Pay Later for a specific transaction.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
enum ApplePayLaterAvailability
```

#### Overview

The following table describes the Apple Pay Later availability reasons.

| Availability reason | Description |
| --- | --- |
| `available` | Apple Pay Later is available. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) This is the default. |
| `unavailableItemIneligible` | Apple Pay Later is unavailable because one or more ineligible or prohibited items are in the shopping cart, such as gift cards |
| `unavailableRecurringTransaction` | Apple Pay Later is unavailable because there’s a recurring payment or subscription in the shopping cart. |

Set the `applePayLaterAvailability` property to only one of these reasons as a string, for example:

```javascript
applePayLaterAvailability = “unavailableRecurringTransaction”;
```

## Topics

### Enumeration Cases
- [available](applepaylateravailability/available.md)
- [unavailableItemIneligible](applepaylateravailability/unavailableitemineligible.md)
- [unavailableRecurringTransaction](applepaylateravailability/unavailablerecurringtransaction.md)

## See Also

- [applePayLaterAvailability](applepayrequestbase/applepaylateravailability.md)
  A value that indicates whether Apple Pay Later is available for a transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaylateravailability)*