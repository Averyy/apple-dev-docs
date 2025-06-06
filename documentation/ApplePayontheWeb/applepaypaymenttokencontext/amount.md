# amount

**Framework**: Apple Pay on the Web  
**Kind**: property

The amount to authorize for the payment token context.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
required DOMString amount;
```

#### Discussion

The sum of the [`amount`](applepaypaymenttokencontext/amount.md) of all the payment token contexts in a payment request must be less than or equal to the grand total amount of the enclosing payment request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaypaymenttokencontext/amount)*