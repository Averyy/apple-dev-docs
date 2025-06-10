# pricingCurrency

**Framework**: External Purchase Server API  
**Kind**: typealias

The currency used in the transaction to bill or refund the customer.

**Availability**:
- External Purchase Server API 1.0.0+

## Declaration

```swift
string pricingCurrency
```

#### Discussion

Maximum length: 128. Use a three-letter ISO 4217 currency code to specify the currency.

The `pricingCurrency` is the currency used in the transaction to charge or refund the customer. The pricing currency affects your reporting currency, [`reportingCurrency`](reportingcurrency.md), which you use to report all amount values.

The currencies Apple supports are listed as allowed values on the [`reportingCurrency`](reportingcurrency.md) page.

> ❗ **Important**: If your `pricingCurrency` isn’t a currency that Apple supports, you must use EUR or USD as the [`reportingCurrency`](reportingcurrency.md).

## See Also

- [type amountTaxExclusive](amounttaxexclusive.md)
  The amount, in milli-units, that the customer paid or was refunded, excluding taxes.
- [type amountTaxInclusive](amounttaxinclusive.md)
  The amount, in milli-units, that the customer paid, including taxes.
- [type netAmountTaxExclusive](netamounttaxexclusive.md)
  The net amount, in milli-units, that you charged the customer, pre-tax, and after deducting all refunds.
- [type taxAmount](taxamount.md)
  The amount, in milli-units, that the customer paid in taxes.
- [type taxCountry](taxcountry.md)
  The three-letter country code of the country that collects the taxes for the transaction.
- [type reportingCurrency](reportingcurrency.md)
  The currency the line item uses to report all amount values.
- [type exchangeRate](exchangerate.md)
  A decimal value that is the exchange rate you use to convert the pricing currency to the reporting currency, when the two currencies differ.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalpurchaseserverapi/pricingcurrency)*