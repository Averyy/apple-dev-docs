# PassKit (Apple Pay and Wallet)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: module  
**Role**: Technology

Process Apple Pay payments in your app, and create and distribute passes for the Wallet app.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.0+
- macOS 11.0+
- visionOS 1.0+
- watchOS 2.0+

## Overview

The PassKit framework lets you:

- Add Apple Pay to your app
- Manage passes in the user’s Wallet app

![The Apple Pay logo.](https://developer.apple.com/tutorials/images/com.apple.passkit/media-3975193@2x.png)

Apple Pay is a secure and easy way for users to make purchases in stores, in apps, and on the web. When you use PassKit APIs to support Apple Pay in your iOS and watchOS apps, your users can purchase real-world goods and services, or donate to nonprofit organizations, without ever leaving your app.

> **Note**:  To add Apple Pay to your web applications, see [Apple Pay on the Web](../ApplePayontheWeb/ApplePayontheWeb.md).
>
> For digital goods and services delivered within the app, see [In-App Purchase](https://developer.apple.com/in-app-purchase/) instead.

![The icon that respresents Wallet.](https://developer.apple.com/tutorials/images/com.apple.passkit/media-3975195@2x.png)

The Wallet app allows users to organize their boarding passes, tickets, gift cards, and loyalty cards. It also lets users manage their payment cards for Apple Pay. Using the PassKit framework, you can add passes to Wallet and have these passes appear on the user’s lock screen based on the time and place when the pass is relevant. You can also update a pass’s content using push notifications.

## Topics

### Apple pay support
- [Apple Pay](./apple-pay.md)
  Request and process Apple Pay payments in your app.
### Wallet support
- [Wallet](./wallet.md)
  Manage tickets, boarding passes, payment cards and other passes in the Wallet app.
### Structures
- [struct ApplePayMerchandisingAction](./applepaymerchandisingaction.md)
  Type of action taken when the button is tapped on the ApplePayMerchandisingView
- [struct ApplePayMerchandisingPartnerConfiguration](./applepaymerchandisingpartnerconfiguration.md)
  Defines the partner configuration for the ApplePayMerchandisingView
- [struct ApplePayMerchandisingStyle](./applepaymerchandisingstyle.md)
  Styling layout of the ApplePayMerchandisingView
- [struct ApplePayMerchandisingView](./applepaymerchandisingview.md)
### Variables
- [PKPaymentNetworkConecs](./pkpaymentnetwork/conecs.md)
- [PKPaymentNetworkElCorteIngles](./pkpaymentnetwork/elcorteingles.md)
- [PKPaymentNetworkElcard](./pkpaymentnetwork/elcard.md)
- [PKPaymentNetworkHimyan](./pkpaymentnetwork/himyan.md)
- [PKPaymentNetworkHumo](./pkpaymentnetwork/humo.md)
- [PKPaymentNetworkJaywan](./pkpaymentnetwork/jaywan.md)
  A Jaywan payment card.
- [PKPaymentNetworkMaal](./pkpaymentnetwork/maal.md)
- [PKPaymentNetworkMyDebit](./pkpaymentnetwork/mydebit.md)
- [PKPaymentNetworkPayPak](./pkpaymentnetwork/paypak.md)
- [PKPaymentNetworkRuPay](./pkpaymentnetwork/rupay.md)
- [PKPaymentNetworkUzCard](./pkpaymentnetwork/uzcard.md)
- [PKPaymentNetworkVerve](./pkpaymentnetwork/verve.md)

## See Also

### Related Documentation
- [Wallet Passes](../WalletPasses/WalletPasses.md)
  Create, distribute, and update passes for the Wallet app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/PassKit)*