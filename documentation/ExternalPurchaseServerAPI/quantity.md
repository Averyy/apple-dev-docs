# quantity

**Framework**: External Purchase Server API  
**Kind**: typealias

The quantity of the product the customer purchased in a single transaction.

**Availability**:
- External Purchase Server API 1.0.0+

## Declaration

```swift
int64 quantity
```

#### Discussion

The `quantity` field applies only to purchases. Don’t include a `quantity` for refunds.

Set `quantity` to `1` when a customer purchases a single product. Use a value greater than `1` when someone purchases a multiple of the same product in one transaction.

> ❗ **Important**: Amount values always represent the total amount for the line item, not a per-item amount. The `quantity` value is not used for calculations.

Multiple items may be considered a single product if they are sold as a package. For example, a 10-pack of game gems may be a single product with a quantity of `1`.

If the [`productType`](producttype.md) is `SUBSCRIPTION`, use a `quantity` greater than `1` to indicate a purchase of multiple subscriptions that renew as one, for example, a multi-seat subscription. If subscriptions can have different billing dates or renewal schedules, report them as separate line items with a `quantity` of `1`.

## See Also

- [type productIdentifier](productidentifier.md)
  A string that identifies the product.
- [type productType](producttype.md)
  The type of product in the transaction, whether it’s a one-time buy, or a subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalpurchaseserverapi/quantity)*