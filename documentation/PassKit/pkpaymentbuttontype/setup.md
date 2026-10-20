# PKPaymentButtonType.setUp

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: case  
**Role**: Case

An Apple Pay button useful for prompting the user to set up a card.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
case setUp
```

```c
PKPaymentButtonTypeSetUp
```

#### Discussion

This button looks like:

![A button with the text “Set up” and the Apple Pay logo.](https://developer.apple.com/tutorials/images/com.apple.passkit/media-2903982@2x.png)

You can display this button when the device and parental controls support Apple Pay but the user has not yet added a card. Use the [`PKPaymentAuthorizationViewController`](../pkpaymentauthorizationviewcontroller.md) class’s [`canMakePayments()`](../pkpaymentauthorizationviewcontroller/canmakepayments%28%29.md) method to determine whether the device supports Apple Pay. If [`canMakePayments()`](../pkpaymentauthorizationviewcontroller/canmakepayments%28%29.md) returns [`true`](../../Swift/true.md), call [`canMakePayments(usingNetworks:capabilities:)`](../pkpaymentauthorizationviewcontroller/canmakepayments%28usingnetworks,capabilities%29.md) to determine whether the user has added any cards.

As soon as the user taps this button, initiate the process of setting up a new card (for example, by calling the [`openPaymentSetup()`](../pkpasslibrary/openpaymentsetup%28%29.md) method).

For design guidance, see [Human Interface Guidelines > Apple Pay > Buttons and Marks](https://developer.apple.com/design/human-interface-guidelines/apple-pay/overview/buttons-and-marks/).

## See Also

### Payment button types
- [PKPaymentButtonType.plain](./plain.md)
  An Apple Pay button with the Apple Pay logo only, useful when an additional call to action isn’t needed.
- [PKPaymentButtonType.buy](./buy.md)
  An Apple Pay button useful for product purchases.
- [PKPaymentButtonType.addMoney](./addmoney.md)
  An Apple Pay button useful for adding money to a card, account, or payment system.
- [PKPaymentButtonType.book](./book.md)
  An Apple Pay button useful for booking trips, flights, or other experiences.
- [PKPaymentButtonType.checkout](./checkout.md)
  An Apple Pay button useful for purchase experiences that include other payment buttons that start with “Check out”.
- [PKPaymentButtonType.continue](./continue.md)
  An Apple Pay button useful for general purchases.
- [PKPaymentButtonType.contribute](./contribute.md)
  An Apple Pay button useful to help people contribute money to projects, causes, organizations, and other entities.
- [PKPaymentButtonType.donate](./donate.md)
  An Apple Pay button used by approved nonprofit organization that lets people make donations.
- [PKPaymentButtonType.inStore](./instore.md)
  An Apple Pay button useful for paying bills or invoices.
- [PKPaymentButtonType.order](./order.md)
  An Apple Pay button useful for placing orders for such as like meals or flowers.
- [PKPaymentButtonType.reload](./reload.md)
  An Apple Pay button useful for adding money to a card, account, or payment system.
- [PKPaymentButtonType.rent](./rent.md)
  An Apple Pay button useful for renting items such as cars or scooters.
- [PKPaymentButtonType.subscribe](./subscribe.md)
  An Apple Pay button useful for purchasing a subscription such as a gym membership or meal-kit delivery service.
- [PKPaymentButtonType.support](./support.md)
  An Apple Pay button useful supporting people give money to projects, causes, organizations, and other entities.
- [PKPaymentButtonType.tip](./tip.md)
  An Apple Pay button useful useful for letting people tip for goods or services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentbuttontype/setup)*