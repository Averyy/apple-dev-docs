# productType

**Framework**: External Purchase Server API  
**Kind**: typealias  
**Role**: Type

The type of product in the transaction, whether it’s a one-time buy, or a subscription.

**Availability**:
- External Purchase Server API 1.0.0+

## Declaration

```
string productType
```

## Possible Values

- `ONE_TIME_BUY`
- `SUBSCRIPTION`

#### Discussion

Allowed values: `ONE_TIME_BUY`, `SUBSCRIPTION`

Use  `ONE_TIME_BUY` for in-app products that customers purchase once. Use `SUBSCRIPTION` for in-app products that have periodic renewals.

## See Also

### Providing product info
- [type productIdentifier](./productidentifier.md)
  A string that identifies the product.
- [type quantity](./quantity.md)
  The quantity of the product the customer purchased in a single transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalpurchaseserverapi/producttype)*