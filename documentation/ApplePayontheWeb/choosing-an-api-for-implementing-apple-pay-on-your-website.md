# Choosing an API for Implementing Apple Pay on Your Website

**Framework**: Apple Pay on the Web

Compare Apple Pay JS and Payment Request API to choose the right implementation for your website.

#### Overview

Safari supports two APIs for implementing payment requests: [`Apple Pay JS API`](apple-pay-js-api.md), and the W3C [`Payment Request API`](payment-request-api.md). Both APIs present the same Apple Pay payment sheet on Safari, and offer nearly the same user experience.

To help you decide which API to implement, or whether to implement both, first determine which features your solution requires, and choose the API that matches your needs.

##### Features of Apple Pay Js Api

Use [`Apple Pay JS API`](apple-pay-js-api.md) if you depend on any of its unique features:

 You can provide robust error handling:

- Customizable error messages and field indications create a better user experience. See [`ApplePayError`](applepayerror.md) for more information.
- You can report errors the user can correct, even after the user authorizes payment.
- You can retry if an error occurs after the user authorizes payment. With [`Payment Request API`](payment-request-api.md), the user must restart their transaction.

 When customers with affiliated cards visit your website, you can provide these additional benefits:

- Apple Pay can automatically select the affiliated card instead of the customer’s default card.
- You can adjust prices or other terms of a sale for customers using your affiliated card. For example, you might provide free shipping when customers use your cobranded VISA credit card.

 You can request a phonetic name in [`Apple Pay JS API`](apple-pay-js-api.md) only.

##### Features of Payment Request Api

Use [`Payment Request API`](payment-request-api.md) for these benefits:

-  Payment Request API-based code can support a variety platforms and browsers. Apple Pay is available on Safari; other payment methods are available on other browsers and platforms.
-   The Payment Request API is defined by the [`World Wide Web Consortium (W3C)`](https://developer.apple.comhttps://www.w3.org/TR/payment-request/).

##### Choose an Api to Support Your Customers

To better reach your customers, choose an API that works on their devices, as follows:

-  Supported in iOS 10 and later, and macOS 10.12 and later.
-  Supported in iOS 11.3 and later, and Safari 11.1 on macOS 10.12 and later.

When implementing [`Payment Request API`](payment-request-api.md), consider also implementing [`Apple Pay JS API`](apple-pay-js-api.md) as a fallback for customers whose devices run an older operating system version.

##### Requirements for Both Apis

The same first steps, configurations, and guidelines for using Apple Pay on the web apply regardless of which API you choose to implement.

For more information, see Apple Pay setup,  Apple Pay buttons, and for design guidance see [`Human Interface Guidelines > Apple Pay on the Web`](https://developer.apple.comhttps://developer.apple.com/apple-pay/web-human-interface-guidelines/).

## See Also

- [Apple Pay on the Web version history](apple-pay-on-the-web-version-history.md)
  Learn about features in each version of Apple Pay on the Web.
- [Apple Pay JS API](apple-pay-js-api.md)
  Implement Apple Pay on the web using Apple’s JavaScript API.
- [Payment Request API](payment-request-api.md)
  Accept payments on your website with Apple Pay using the Payment Request API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/choosing-an-api-for-implementing-apple-pay-on-your-website)*