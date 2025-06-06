# identifier

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

A unique identifier for the shipping method, used by the app.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var identifier: String? { get set }
```

#### Discussion

This property isn’t user visible.

Use this property of the shipping method passed to your delegate in the [`paymentAuthorizationViewController(_:didSelect:completion:)`](pkpaymentauthorizationviewcontrollerdelegate/paymentauthorizationviewcontroller(_:didselect:completion:)-9otrj.md) method to identify the chosen shipping method.

## See Also

- [var detail: String?](pkshippingmethod/detail.md)
  A user-readable description of the shipping method.
- [var dateComponentsRange: PKDateComponentsRange?](pkshippingmethod/datecomponentsrange.md)
  An expected range of delivery or shipping dates for a package, or the time range when an item is available for pickup.
- [class PKDateComponentsRange](pkdatecomponentsrange.md)
  An object that specifies the start and end dates for a range of time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkshippingmethod/identifier)*