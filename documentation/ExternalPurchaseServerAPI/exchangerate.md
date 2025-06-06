# exchangeRate

**Framework**: External Purchase Server API  
**Kind**: typealias

A decimal value that is the exchange rate you use to convert the pricing currency to the reporting currency, when the two currencies differ.

**Availability**:
- External Purchase Server API 1.0.0+

## Declaration

```swift
double exchangeRate
```

#### Discussion

Maximum length: 128.
The field must contain a number that can optionally be followed by a “.” and additional digits.

The `exchangeRate` field is required when the [`pricingCurrency`](pricingcurrency.md) and [`reportingCurrency`](reportingcurrency.md) fields differ. Use the `exchangeRate` to convert amounts in the pricing currency to amounts in the reporting currency. The conversion calculation is:

`(amount in pricing currency) * exchangeRate = (amount in reporting currency)`

> ❗ **Important**: To determine an exchange rate for your calculations, use the Bloomberg exchange rate from within 48 hours of the transaction date.

To determine an exchange rate for your calculations, use the Bloomberg exchange rate from within 48 hours of the transaction date.

If the [`pricingCurrency`](pricingcurrency.md) and [`reportingCurrency`](reportingcurrency.md) field values are the same currency, don’t include an `exchangeRate` in the line item. For more information about determining which reporting currency to use, see [`reportingCurrency`](reportingcurrency.md).

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
- [type pricingCurrency](pricingcurrency.md)
  The currency used in the transaction to bill or refund the customer.
- [type reportingCurrency](reportingcurrency.md)
  The currency the line item uses to report all amount values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalpurchaseserverapi/exchangerate)*