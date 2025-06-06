# oncancel

**Framework**: Apple Pay on the Web  
**Kind**: property

An event handler that is automatically called when the payment UI is dismissed.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
attribute EventHandler oncancel;
```

#### Discussion

This function can be called even after an [`onpaymentauthorized`](applepaysession/onpaymentauthorized.md) event has been dispatched. Both the user and the web page can dismiss the payment sheet and abandon the transaction.

## See Also

- [abort](applepaysession/abort.md)
  Aborts the current Apple Pay session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaysession/oncancel)*