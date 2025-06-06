# Setting up Apple Pay

**Framework**: PassKit (Apple Pay and Wallet)

Fulfill the requirements to provide Apple Pay as a payment option on your website or in your app.

#### Overview

To set up your Apple developer account and Xcode to implement Apple Pay in your apps, you complete three steps:

- Create a merchant identifier.
- Create a Payment Processing certificate.
- Enable Apple Pay in Xcode.

##### Create a Merchant Identifier

To enable your app to use Apple Pay, register an identifier with Apple that uniquely identifies your business as a merchant able to accept payments. This ID never expires, and you can use it in multiple websites and apps. See [`Create a merchant identifier`](https://developer.apple.comhttps://developer.apple.com/help/account/configure-app-capabilities/configure-apple-pay#create-a-merchant-identifier) for the setup steps.

##### Create a Payment Processing Certificate

Using your registered merchant identifier, create a certificate to secure transaction data. Apple Pay servers use the certificate’s public key to encrypt payment data. You (or your payment service provider) use the private key to decrypt the data to process payments. See [`Create a payment processing certificate`](https://developer.apple.comhttps://developer.apple.com/help/account/configure-app-capabilities/configure-apple-pay#create-a-payment-processing-certificate) for the setup steps.

> **Note**:  If you use an e-commerce provider or a payment platform, contact them for information about how to use their service with Apple Pay. See [`Payment Platforms`](https://developer.apple.comhttps://developer.apple.com/apple-pay/#payment-platforms) for a list of service providers.

 If you use an e-commerce provider or a payment platform, contact them for information about how to use their service with Apple Pay. See [`Payment Platforms`](https://developer.apple.comhttps://developer.apple.com/apple-pay/#payment-platforms) for a list of service providers.

##### Enable Apple Pay Capability in Xcode

After creating a merchant identifier, enable the Apple Pay capability in your Xcode project.

1. Open your project with Xcode. In the Project navigator, select the project.
2. Choose the target for the app from either the Project/Targets pop-up menu or in the Targets section of the outline view.
3. Click the Signing & Capabilities tab in the project editor.
4. In the toolbar, click the Library button (+) to open the Capabilities library and select the Apple Pay capability.
5. Within the Apple Pay capability, click the refresh button to synchronize your merchant identifiers from the Apple Developer site.
6. Select the merchant identifier to use with this app.

The screenshot below shows the Apple Pay capability without any merchant identifiers:

![A screenshot showing the Apple Pay capability without any listed merchant identifiers. Beneath the empty list of merchant identifiers is a button to add a merchant identifier, and a button to refresh identifiers from the Apple Developer site.](https://docs-assets.developer.apple.com/published/1872acfd24b98f341033640914195123/media-3737978%402x.png)

For more information, see [`Adding capabilities to your app`](https://developer.apple.com/documentation/Xcode/adding-capabilities-to-your-app).

##### Configure Apple Pay on the Web

If you’re also developing websites using [`Apple Pay on the Web`](https://developer.apple.com/documentation/apple_pay_on_the_web), you can use the same merchant ID and Payment Processing Certificate for your website. However, Apple Pay on the web requires additional setup; see [`Configuring Your Environment`](https://developer.apple.com/documentation/apple_pay_on_the_web/configuring_your_environment), [`Get Started with Apple Pay on the Web`](https://developer.apple.comhttps://developer.apple.com/videos/play/tech-talks/111381), and the [`Apple Pay Merchant Integration Guide`](https://developer.apple.comhttp://developer.apple.com/apple-pay/Apple-Pay-Merchant-Integration-Guide.pdf) for more information.

## See Also

- [Offering Apple Pay in Your App](offering-apple-pay-in-your-app.md)
  Collect payments with iPhone and Apple Watch using Apple Pay.
- [Complying with regional regulations](complying-with-regional-regulations.md)
  Check regional regulations for possible requirements for your Apple Pay-based implementation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/setting-up-apple-pay)*