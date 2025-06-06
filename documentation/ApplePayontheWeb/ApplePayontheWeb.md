# Apple Pay on the Web

**Framework**: Apple Pay on the Web  
**Kind**: module

Support Apple Pay on your website with JavaScript-based APIs.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

#### Overview

Safari supports two JavaScript APIs that let you accept Apple Pay payments from customers on your website:

- [`Payment Request API`](https://developer.apple.com/documentation/apple_pay_on_the_web/payment_request_api), a [`W3C candidate API`](https://developer.apple.comhttps://www.w3.org/TR/payment-request/)
- [`Apple Pay JS API`](https://developer.apple.com/documentation/apple_pay_on_the_web/apple_pay_js_api), analogous to the [`PassKit (Apple Pay and Wallet)`](https://developer.apple.com/documentation/PassKit) framework for Apple Pay in apps.

> 💡 **Tip**:  You can try out Apple Pay transactions on the demo page. See [`Apple Pay on the Web Interactive Demo`](https://developer.apple.comhttps://applepaydemo.apple.com).

 You can try out Apple Pay transactions on the demo page. See [`Apple Pay on the Web Interactive Demo`](https://developer.apple.comhttps://applepaydemo.apple.com).

Apple Pay is available on all iOS devices with a Secure Element — an industry-standard, certified chip designed to store payment information safely. In macOS, users must have an Apple Pay-capable iPhone or Apple Watch to authorize the payment, or a Mac with Touch ID.

##### Apple Pay Availability By Region and Platform

Apple Pay is available in [`supported regions`](https://developer.apple.comhttps://www.apple.com/ios/feature-availability/#apple-pay).

The Apple Pay APIs are available in Safari on the following platforms:

|  |  |  |
| --- | --- | --- |
|  | iOS 10 and later ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) macOS 10.12 and later | iOS 11.2 and later ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) (Not available in macOS) |
|  | iOS 11.3 and later ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) macOS 10.12.6 and later, in Safari 11.1 and later | iOS 11.3 and later ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) (Not available in macOS) |

In iOS, Safari and [`SFSafariViewController`](https://developer.apple.com/documentation/SafariServices/SFSafariViewController) objects support Apple Pay.

See [`Checking for Apple Pay availability`](https://developer.apple.com/documentation/apple_pay_on_the_web/apple_pay_js_api/checking_for_apple_pay_availability) to ensure your implementation only displays the Apple Pay button on supported devices.

> **Note**:  Regulations in some regions may require specific configurations in your implementation. For more information, see [`Complying with regional regulations`](https://developer.apple.com/documentation/PassKit/complying-with-regional-regulations).

 Regulations in some regions may require specific configurations in your implementation. For more information, see [`Complying with regional regulations`](https://developer.apple.com/documentation/PassKit/complying-with-regional-regulations).

##### Apple Pay Requirements

The requirements for using Apple Pay on your website are:

- Your website must comply with the Apple Pay guidelines. For more information, see [`Acceptable Use Guidelines for Apple Pay on the Web`](https://developer.apple.comhttps://developer.apple.com/apple-pay/acceptable-use-guidelines-for-websites/).
- You must have an Apple Developer Account and complete the registration. For more information, see [`Configuring Your Environment`](https://developer.apple.com/documentation/apple_pay_on_the_web/configuring_your_environment).
- All pages that include Apple Pay must be served over HTTPS. For more information, see [`Setting Up Your Server`](https://developer.apple.com/documentation/apple_pay_on_the_web/setting_up_your_server).

For design guidance, see [`Human Interface Guidelines > Apple Pay`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/apple-pay/overview/introduction/).

## Topics

### Essentials
- [Using the Apple Pay JS SDK for iOS 18](using-the-apple-pay-js-sdk-for-ios-18.md)
  Add the latest Apple Pay JS SDK.
### Apple Pay setup
- [Setting Up Your Server](setting-up-your-server.md)
  Set up your server for secure communications with Apple Pay.
- [Configuring Your Environment](configuring-your-environment.md)
  Create your Apple Pay merchant ID and certificates, and verify your domain.
- [Maintaining Your Environment](maintaining-your-environment.md)
  Prevent interruptions in your Apple Pay service by keeping certificates and domain verification current.
### Apple Pay Later visual merchandising widget
- [Adding an Apple Pay Later visual merchandising widget](adding-an-apple-pay-later-visual-merchandising-widget.md)
  Configure and style Apple Pay Later visual merchandising widgets to match your website.
### Apple order tracking button
- [Adding a Track with Apple Wallet button](adding-a-track-with-apple-wallet-button.md)
  Configure and style an Apple Wallet Button to match your website.
### Apple Pay buttons
- [Displaying Apple Pay Buttons Using JavaScript](displaying-apple-pay-buttons-using-javascript.md)
  Load and configure the JavaScript Apple Pay button.
- [ApplePayButton](applepaybutton.md)
  An object that displays a button either to trigger payments through Apple Pay or to prompt the user to set up a card.
- [Displaying Apple Pay Buttons Using CSS](displaying-apple-pay-buttons-using-css.md)
  Use CSS templates to display Apple Pay buttons in Safari.
### Apple Pay JavaScript APIs
- [Choosing an API for Implementing Apple Pay on Your Website](choosing-an-api-for-implementing-apple-pay-on-your-website.md)
  Compare Apple Pay JS and Payment Request API to choose the right implementation for your website.
- [Apple Pay on the Web version history](apple-pay-on-the-web-version-history.md)
  Learn about features in each version of Apple Pay on the Web.
- [Apple Pay JS API](apple-pay-js-api.md)
  Implement Apple Pay on the web using Apple’s JavaScript API.
- [Payment Request API](payment-request-api.md)
  Accept payments on your website with Apple Pay using the Payment Request API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ApplePayontheWeb)*