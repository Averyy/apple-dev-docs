# PKPaymentButtonType

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: enum

The Apple Pay button types you can display to initiate Apple Pay transactions.

**Availability**:
- iOS 8.3+
- iPadOS 8.3+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
enum PKPaymentButtonType
```

#### Overview

The button type you use for payments made with Apple Pay can affect the purchasing experience. Choose a button type that best fits with the terminology and flow of your purchase or payment experience. For design guidance, see [`Human Interface Guidelines > Apple Pay > Buttons and Marks`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/apple-pay/overview/buttons-and-marks/).

Before using a specific button type, check that it’s available to the iOS version that your app is running on. Create buttons using the [`buttonWithType:style:`](pkpaymentbutton/buttonwithtype:style:.md) method.

## Topics

### Payment button types
- [PKPaymentButtonType.plain](pkpaymentbuttontype/plain.md)
  An Apple Pay button with the Apple Pay logo only, useful when an additional call to action isn’t needed.
- [PKPaymentButtonType.buy](pkpaymentbuttontype/buy.md)
  An Apple Pay button useful for product purchases.
- [PKPaymentButtonType.addMoney](pkpaymentbuttontype/addmoney.md)
  An Apple Pay button useful for adding money to a card, account, or payment system.
- [PKPaymentButtonType.book](pkpaymentbuttontype/book.md)
  An Apple Pay button useful for booking trips, flights, or other experiences.
- [PKPaymentButtonType.checkout](pkpaymentbuttontype/checkout.md)
  An Apple Pay button useful for purchase experiences that include other payment buttons that start with “Check out”.
- [PKPaymentButtonType.continue](pkpaymentbuttontype/continue.md)
  An Apple Pay button useful for general purchases.
- [PKPaymentButtonType.contribute](pkpaymentbuttontype/contribute.md)
  An Apple Pay button useful to help people contribute money to projects, causes, organizations, and other entities.
- [PKPaymentButtonType.donate](pkpaymentbuttontype/donate.md)
  An Apple Pay button used by approved nonprofit organization that lets people make donations.
- [PKPaymentButtonType.inStore](pkpaymentbuttontype/instore.md)
  An Apple Pay button useful for paying bills or invoices.
- [PKPaymentButtonType.order](pkpaymentbuttontype/order.md)
  An Apple Pay button useful for placing orders for such as like meals or flowers.
- [PKPaymentButtonType.reload](pkpaymentbuttontype/reload.md)
  An Apple Pay button useful for adding money to a card, account, or payment system.
- [PKPaymentButtonType.rent](pkpaymentbuttontype/rent.md)
  An Apple Pay button useful for renting items such as cars or scooters.
- [PKPaymentButtonType.setUp](pkpaymentbuttontype/setup.md)
  An Apple Pay button useful for prompting the user to set up a card.
- [PKPaymentButtonType.subscribe](pkpaymentbuttontype/subscribe.md)
  An Apple Pay button useful for purchasing a subscription such as a gym membership or meal-kit delivery service.
- [PKPaymentButtonType.support](pkpaymentbuttontype/support.md)
  An Apple Pay button useful supporting people give money to projects, causes, organizations, and other entities.
- [PKPaymentButtonType.tip](pkpaymentbuttontype/tip.md)
  An Apple Pay button useful useful for letting people tip for goods or services.
- [PKPaymentButtonType.topUp](pkpaymentbuttontype/topup.md)
  An Apple Pay button useful for adding money to a card, account, or payment system.
### Initializers
- [init?(rawValue: Int)](pkpaymentbuttontype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum PKPaymentButtonStyle](pkpaymentbuttonstyle.md)
  A type that indicates the available appearances for an Apple Pay button.
- [var cornerRadius: CGFloat](pkpaymentbutton/cornerradius.md)
  The radius, in points, for the rounded corners on the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentbuttontype)*