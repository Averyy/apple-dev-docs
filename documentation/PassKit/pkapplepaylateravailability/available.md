# PKApplePayLaterAvailability.available

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: case  
**Role**: Case

Apple Pay Later is available.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
case available
```

```c
PKApplePayLaterAvailable
```

## See Also

### Availability values
- [PKApplePayLaterAvailability.unavailableItemIneligible](./unavailableitemineligible.md)
  Apple Pay Later is unavailable because one or more ineligible or prohibited items are in the shopping cart, such as gift cards.
- [PKApplePayLaterAvailability.unavailableRecurringTransaction](./unavailablerecurringtransaction.md)
  Apple Pay Later is unavailable because there’s a recurring payment or subscription in the shopping cart.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkapplepaylateravailability/available)*