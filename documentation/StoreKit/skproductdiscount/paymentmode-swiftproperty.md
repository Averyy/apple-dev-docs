# paymentMode

**Framework**: StoreKit  
**Kind**: property

The payment mode for this product discount.

**Availability**:
- iOS 11.2+
- iPadOS 11.2+
- Mac Catalyst 13.1+
- macOS 10.13.2+
- tvOS 11.2+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
var paymentMode: SKProductDiscount.PaymentMode { get }
```

#### Discussion

The payment mode indicates how the product discount [`price`](skproductdiscount/price.md) is charged:

- One or more times, for [`SKProductDiscount.PaymentMode.payAsYouGo`](skproductdiscount/paymentmode-swift.enum/payasyougo.md) mode
- Once in advance, for [`SKProductDiscount.PaymentMode.payUpFront`](skproductdiscount/paymentmode-swift.enum/payupfront.md) mode
- No initial charge, for [`SKProductDiscount.PaymentMode.freeTrial`](skproductdiscount/paymentmode-swift.enum/freetrial.md) mode.

Use the payment mode to display an accurate description of the product discount in your UI. For design guidance, see [`Human Interface Guidelines > In-App Purchase`](https://developer.apple.comhttps://developer.apple.com/ios/human-interface-guidelines/technologies/in-app-purchase/).

## See Also

- [var price: NSDecimalNumber](skproductdiscount/price.md)
  The discount price of the product in the local currency.
- [var priceLocale: Locale](skproductdiscount/pricelocale.md)
  The locale used to format the discount price of the product.
- [SKProductDiscount.PaymentMode](skproductdiscount/paymentmode-swift.enum.md)
  Values representing the payment modes for a product discount.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproductdiscount/paymentmode-swift.property)*