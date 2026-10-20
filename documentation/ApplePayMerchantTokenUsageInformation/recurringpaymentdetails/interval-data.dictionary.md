# RecurringPaymentDetails.Interval

**Framework**: Apple Pay Merchant Token Usage Information API  
**Kind**: dictionary  
**Role**: Object

The payment interval.

## Declaration

```
object RecurringPaymentDetails.Interval
```

## Properties

- `count` (number): The number of units that make up the total payment interval. The default value is `1`.

  **Minimum**: `1`
- `unit` (string) *(required)*: The amount of time — in calendar units, such as day, month, or year — that represents a fraction of the total payment interval.

  **Allowed Values**: `minute`, `hour`, `day`, `week`, `month`, `year`


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepaymerchanttokenusageinformation/recurringpaymentdetails/interval-data.dictionary)*