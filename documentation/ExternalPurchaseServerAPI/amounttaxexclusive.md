# amountTaxExclusive

**Framework**: External Purchase Server API  
**Kind**: typealias

The amount, in milli-units, that the customer paid or was refunded, excluding taxes.

**Availability**:
- External Purchase Server API 1.0.0+

## Declaration

```swift
int64 amountTaxExclusive
```

#### Discussion

This value must equal [`amountTaxInclusive`](amounttaxinclusive.md) minus [`taxAmount`](taxamount.md). The `amountTaxExclusive` value is the amount in milli-units that the user paid, excluding taxes. For refunds, it is the amount in milli-units of the refund, excluding taxes.

Provide all amount field values in milli-units of the currency you state in the [`reportingCurrency`](reportingcurrency.md) field. One unit of the currency equals 1000 milli-units. For example, if the amount is `€2.99`, the amount in milli-units is `2990`.

## See Also

- [type amountTaxInclusive](amounttaxinclusive.md)
  The amount, in milli-units, that the customer paid, including taxes.
- [type netAmountTaxExclusive](netamounttaxexclusive.md)
  The net amount, in milli-units, that you charged the customer, pre-tax, and after deducting all refunds.
- [type taxAmount](taxamount.md)
  The amount, in milli-units, that the customer paid in taxes.
- [type taxCountry](taxcountry.md)
  The three-letter country code of the country that collects the taxes for the transaction.
- [type pricingCurrency](pricingcurrency.md)
  The currency used in the transaction to bill or refund the customer.
- [type reportingCurrency](reportingcurrency.md)
  The currency the line item uses to report all amount values.
- [type exchangeRate](exchangerate.md)
  A decimal value that is the exchange rate you use to convert the pricing currency to the reporting currency, when the two currencies differ.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalpurchaseserverapi/amounttaxexclusive)*