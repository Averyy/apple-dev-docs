# priceTiers

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The price tiers of the subscription, in ascending order of seat count.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)
- watchOS 27.3+ (Beta)

## Declaration

```swift
let priceTiers: [Product.SubscriptionInfo.PricingTerms.SeatBasedPricing.PriceTier]
```

## Mentions

- [Supporting multiseat purchases in your app](../../../../supporting-multiseat-purchases-in-your-app.md)

## Discussion

Each tier covers a range of seats, from [`minimumSeats`](./pricetier/minimumseats.md) to [`maximumSeats`](./pricetier/maximumseats.md), and gives the price of one seat in that range. A subscription with per-seat pricing has one tier.

Each seat costs the per-seat price of the tier it falls in, so adding seats doesn’t lower the price of the seats in earlier tiers. For example, with tiers for 1–5 seats at $9.99 and 6–10 seats at $7.99, 8 seats cost 5 × $9.99 plus 3 × $7.99, or $73.92. No API calculates the total, so add up the tiers yourself:

```swift
func totalPrice(
    forSeats seatCount: Int,
    in tiers: [Product.SubscriptionInfo.PricingTerms.SeatBasedPricing.PriceTier]
) -> Decimal {
    tiers.reduce(Decimal.zero) { total, tier in
        let lastSeat = min(seatCount, tier.maximumSeats ?? seatCount)
        let seatsInTier = max(0, lastSeat - tier.minimumSeats + 1)
        return total + Decimal(seatsInTier) * tier.billingInfo.price
    }
}
```

To display the total, format it with the product’s [`priceFormatStyle`](../../../priceformatstyle.md).

## See Also

### Getting the price tiers
- [Product.SubscriptionInfo.PricingTerms.SeatBasedPricing.PriceTier](./pricetier.md)
  A per-seat price that applies to a range of seats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/pricingterms-swift.struct/seatbasedpricing/pricetiers)*