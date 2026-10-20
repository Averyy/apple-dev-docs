# PKApplePayLaterAvailability.unavailableItemIneligible

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: case  
**Role**: Case

Apple Pay Later is unavailable because one or more ineligible or prohibited items are in the shopping cart, such as gift cards.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
case unavailableItemIneligible
```

```c
PKApplePayLaterUnavailableItemIneligible
```

## See Also

### Availability values
- [PKApplePayLaterAvailability.available](./available.md)
  Apple Pay Later is available.
- [PKApplePayLaterAvailability.unavailableRecurringTransaction](./unavailablerecurringtransaction.md)
  Apple Pay Later is unavailable because there’s a recurring payment or subscription in the shopping cart.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkapplepaylateravailability/unavailableitemineligible)*