# TN3175: Diagnosing issues with displaying the Apple Pay button on your website

**Framework**: Technotes

Diagnose common errors received while displaying the Apple Pay button on your website by identifying the underlying causes, and explore potential solutions.

#### Overview

There are two ways to display the Apple Pay button on your website— [`canMakePaymentsWithActiveCard`](https://developer.apple.comhttps://developer.apple.com/documentation/apple_pay_on_the_web/applepaysession/1778000-canmakepaymentswithactivecard) and [`canMakePayments`](https://developer.apple.comhttps://developer.apple.com/documentation/apple_pay_on_the_web/applepaysession/1778027-canmakepayments/). Use `canMakePaymentsWithActiveCard` to display the Apple Pay button on any Apple Pay supported device with at least one provisioned card in Wallet. Otherwise, use `canMakePayments` to display the Apple Pay button on any Apple Pay supported device.

To test out different Apple Pay button configurations, see [`Apple Pay on the Web Interactive Demo`](https://developer.apple.comhttps://applepaydemo.apple.com). For more information about supporting Apple Pay on your website, see [`Apple Pay on the Web`](https://developer.apple.comhttps://developer.apple.com/documentation/applepayontheweb).

It is recommended that merchants display the [`Apple Pay button using JavaScript`](https://developer.apple.comhttps://developer.apple.com/documentation/apple_pay_on_the_web/displaying_apple_pay_buttons_using_javascript). This approach provides many benefits for developers, including:

- The button’s appearance uses an Apple-approved label, font, color, and style.
- The button’s contents retain ideal proportions as you change its size.
- The button’s label is automaticlly translated into the language setting of your device.
- The button’s corner radius can be configured to match the style of your UI.
- The button contains a system-provided alternative text label for VoiceOver support.

#### Possible Reasons for Apple Pay Button Display Issues

Some common button display issues that you may encounter during your Apple Pay implementation include:

- The `canMakePaymentsWithActiveCard` method unexpectedly returns `false`.
- Apple Pay is displayed as a payment option although no cards are provisioned in Wallet.
- The Apple Pay button does nothing when tapped or clicked.

##### Issue the Canmakepaymentswithactivecard Method Unexpectedly Returns False

When you invoke the `canMakePaymentsWithActiveCard` method, it verifyies whether the device is capable of making Apple Pay payments, and the customer has at least one eligible card provisioned in Wallet. The method also verifies that the [`merchantIdentifier`](https://developer.apple.comhttps://developer.apple.com/documentation/apple_pay_on_the_web/applepayrequest/2951611-merchantidentifier) is registered for Apple Pay, has active certificates, and a verified merchant domain configured for your Apple Developer account.

If you are testing your Apple Pay integration with a device that has an active card in Wallet and still receive a `false` response from the `canMakePaymentsWithActiveCard`, there is an issue with your merchant ID configuration. Please confirm the following are correct:

- The `merchantIdentifier` passed to `canMakePaymentsWithActiveCard` is identical to the value registered for your Apple Developer account.
- The domain is registered and verified as a merchant domain for your Apple Developer account.
- The domain shown in your web browser’s address bar is identical to the merchant domain registered and verified for your Apple Developer account.
- Your devices are running iOS 10 and later, or macOS 10.12 and later. See [`Apple Pay on the web version history`](https://developer.apple.comhttps://developer.apple.com/documentation/apple_pay_on_the_web/apple_pay_on_the_web_version_history).

##### Issue Apple Pay Is Displayed As a Payment Option Although No Cards Are Provisioned in Wallet

This issue usually occurs when you have implemented the `canMakePayments` method (or no method at all), which returns `true` if the user has an Apple Pay capable device. If the customer selects the Apple Pay button in this state, you may prompt the customer to start an inline provisioning flow to add a card to their Wallet before proceeding with the payment flow. Once the card is added, the customer can automatically be brought back to your website to complete their purchase.

##### Issue the Apple Pay Button Does Nothing When Tapped or Clicked

This issue often occurs when you provide invalid values to the properties of the
[`ApplePayPaymentRequest`](https://developer.apple.comhttps://developer.apple.com/documentation/apple_pay_on_the_web/applepaypaymentrequest) after the customer taps or clicks the Apple Pay button. To resolve this issue, please confirm the following:

- The JavaScript Console shown from the [`Develop menu in Safari`](https://developer.apple.comhttps://support.apple.com/guide/safari/use-the-developer-tools-in-the-develop-menu-sfri20948/17.0/mac/14.0) has no relevant errors.
- The payment request is configured with all of the required properties.
- The payment request properties all include a value; you cannot provide an empty or `nil` value.

#### Revision History

- **2024-06-25** First published.

## See Also

- [TN3213: Moving from Multipeer Connectivity to Network framework](tn3213-moving-from-multipeer-connectivity-to-network-framework.md)
  Learn how to migrate your Multipeer Connectivity app to Network framework.
- [TN3210: Optimizing your app for iPhone Mirroring](tn3210-optimizing-your-app-for-iphone-mirroring.md)
  Test your app and improve compatibility with iPhone Mirroring.
- [TN3211: Resolving SwiftUI source incompatibilities for State and ContentBuilder](tn3211-resolving-swiftui-source-incompatibilities-for-state-and-contentbuilder.md)
  Update existing code for two foundational changes in SwiftUI built with Xcode 27.
- [TN3212: Adopting gesture recognizers for Sidecar touch support](tn3212-adopting-gesture-recognizers-for-sidecar-touch-support.md)
  Use gesture recognizers to handle Sidecar touch input and update your event-handling code for macOS 27.
- [TN3208: Preparing your app’s launch screen to meet App Store requirements](tn3208-preparing-your-apps-launch-screen-to-meet-app-store-requirements.md)
  Understand the launch screen requirement for App Store submission starting in iOS 27 and iPadOS 27.
- [TN3205: Low-latency communication with RDMA over Thunderbolt](tn3205-low-latency-communication-with-rdma-over-thunderbolt.md)
  Learn how to use RDMA over Thunderbolt to enable low-latency communication between clusters of Mac computers.
- [TN3206: Updating Apple Pay certificates](tn3206-updating-apple-pay-certificates.md)
  Learn how to create, manage, and rotate Apple Pay certificates to maintain uninterrupted payment processing.
- [TN3179: Understanding local network privacy](tn3179-understanding-local-network-privacy.md)
  Learn how local network privacy affects your software.
- [TN3190: USB audio device design considerations](tn3190-usb-audio-device-design-considerations.md)
  Learn the best techniques for designing devices that conform to the USB Audio Device Class specifications.
- [TN3194: Handling account deletions and revoking tokens for Sign in with Apple](tn3194-handling-account-deletions-and-revoking-tokens-for-sign-in-with-apple.md)
  Learn the best techniques for managing Sign in with Apple user sessions and responding to account deletion requests.
- [TN3193: Managing the on-device foundation model’s context window](tn3193-managing-the-on-device-foundation-model-s-context-window.md)
  Learn how to budget for the context window limit of Apple’s on-device foundation model and handle the error when reaching the limit.
- [TN3115: Bluetooth State Restoration app relaunch rules](tn3115-bluetooth-state-restoration-app-relaunch-rules.md)
  Learn about the conditions under which an iOS app will be relaunched by Bluetooth State Restoration.
- [TN3192: Migrating your iPad app from the deprecated UIRequiresFullScreen key](tn3192-migrating-your-app-from-the-deprecated-uirequiresfullscreen-key.md)
  Support iPad multitasking and dynamic resizing while updating your app to remove the deprecated full-screen compatibility mode.
- [TN3151: Choosing the right networking API](tn3151-choosing-the-right-networking-api.md)
  Learn which networking API is best for you.
- [TN3111: iOS Wi-Fi API overview](tn3111-ios-wifi-api-overview.md)
  Explore the various Wi-Fi APIs available on iOS and their expected use cases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3175-diagnosing-issues-with-displaying-the-apple-pay-button-on-your-website)*