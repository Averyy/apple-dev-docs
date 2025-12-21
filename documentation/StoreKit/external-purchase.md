# External Purchase

**Framework**: StoreKit

Enable qualifying apps to offer external purchases.

#### Overview

If you develop a qualifying app, you may complete a request for optional entitlements that allow you to offer external purchases. For more information about whether your app qualifies, requesting an entitlement, and implementation requirements, see:

- [`Communication and promotion of offers on the App Store in the EU`](https://developer.apple.comhttps://developer.apple.com/support/communication-and-promotion-of-offers-on-the-app-store-in-the-eu/)
- [`Distributing dating apps in the Netherlands`](https://developer.apple.comhttps://developer.apple.com/support/storekit-external-entitlement/)
- [`Distributing apps in Russia that provide an external purchase link`](https://developer.apple.comhttps://developer.apple.com/contact/request/storekit-external-entitlement-ru/)
- [`Distributing apps using a third-party payment provider in South Korea`](https://developer.apple.comhttps://developer.apple.com/support/storekit-external-entitlement-kr/)
- [`Distributing music streaming apps in the EEA that provide an external purchase link`](https://developer.apple.comhttps://developer.apple.com/support/music-streaming-services-entitlement-eea/)

##### Offer External Purchases Using Alternative Payment Service Providers

If your account receives the StoreKit External Purchase entitlement or the StoreKit External Purchase Regions entitlement, implement the following to offer external purchases within your app:

- Depending on the entitlement you receive, configure the doc://com.apple.documentation/documentation/bundleresources/entitlements/com.apple.developer.storekit.external-purchase.allowed-regions entitlement for your app, or the [`com.apple.developer.storekit.external-purchase`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.storekit.external-purchase) entitlement and the [`SKExternalPurchase`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SKExternalPurchase) property list key.
- Use the [`ExternalPurchase`](externalpurchase.md) type’s [`canPresent`](externalpurchase/canpresent.md) property to determine whether external purchase is available.
- Call the [`presentNoticeSheet()`](externalpurchase/presentnoticesheet().md) method and use the external purchase token you receive from the [`ExternalPurchase.NoticeResult.continuedWithExternalPurchaseToken(token:)`](externalpurchase/noticeresult/continuedwithexternalpurchasetoken(token:).md) result to record transactions.
- From your server, report the external purchase tokens and the transactions associated with the tokens by using the [`External Purchase Server API`](https://developer.apple.com/documentation/ExternalPurchaseServerAPI).

##### Communicate and Promote Offers

If your account receives the StoreKit External Purchase Link entitlement or the StoreKit External Custom Purchase Link Regions entitlement, your app can communicate and promote offers for digital goods or services available for purchase or download, in a distribution channel of your choice. Implement the following:

- Depending on the entitlement you receive, configure the [`com.apple.developer.storekit.custom-purchase-link.allowed-regions`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.storekit.custom-purchase-link.allowed-regions) entitlement for your app, or the [`com.apple.developer.storekit.external-purchase-link`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.storekit.external-purchase-link) entitlement and the [`SKExternalPurchaseCustomLinkRegions`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SKExternalPurchaseCustomLinkRegions) property list key, providing the country code for each permitted region where your app communicates and promotes offers.
- Check the [`isEligible`](externalpurchasecustomlink/iseligible.md) property of the [`ExternalPurchaseCustomLink`](externalpurchasecustomlink.md) API to determine whether the API is available at runtime.
- At launch and before every potential transaction, call the [`token(for:)`](externalpurchasecustomlink/token(for:).md) function to request the external purchase tokens, using the token types `ACQUISITION` and `SERVICES`. Associate these tokens with a customer account on your server.
- Call the [`showNotice(type:)`](externalpurchasecustomlink/shownotice(type:).md) function after a deliberate customer interaction, such as tapping a button, and before communicating and promoting offers.
- From your server, report the external purchase tokens and the transactions associated with the tokens by using the [`External Purchase Server API`](https://developer.apple.com/documentation/ExternalPurchaseServerAPI).

##### Communicate and Promote Offers for Music Streaming Apps

If your account receives the Music Streaming Services (EEA) entitlement or the StoreKit External Purchase Link Regions For Music Streaming entitlement, your music-streaming app can use the [`ExternalPurchaseCustomLink`](externalpurchasecustomlink.md) API to communicate and promote offers for music streaming services. Custom links can be to a distribution channel of your choice. Implement the following:

- Depending on the entitlement you receive, configure the doc://com.apple.documentation/documentation/bundleresources/entitlements/com.apple.developer.storekit.external-purchase-link-streaming.allowed-regions entitlement for your app, or the [`com.apple.developer.storekit.external-purchase-link-streaming`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.storekit.external-purchase-link-streaming) entitlement and the [`SKExternalPurchaseLinkStreamingRegions`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SKExternalPurchaseLinkStreamingRegions) property list key, providing the country code for each permitted region where your app communicates and promotes offers for music streaming.
- Check the [`isEligible`](externalpurchasecustomlink/iseligible.md) property of the [`ExternalPurchaseCustomLink`](externalpurchasecustomlink.md) API to determine whether external purchase is available at runtime.
- At launch and before every potential transaction, call the [`token(for:)`](externalpurchasecustomlink/token(for:).md) function to request the external purchase tokens, using the token types `ACQUISITION` and `SERVICES`. Associate these tokens with a customer account on your server.
- Call the [`showNotice(type:)`](externalpurchasecustomlink/shownotice(type:).md) function after a deliberate customer interaction, such as tapping a button, and before communicating and promoting offers.
- From your server, report the external purchase tokens and the transactions associated with the tokens by using the [`External Purchase Server API`](https://developer.apple.com/documentation/ExternalPurchaseServerAPI).

##### Offer External Purchase Link Outs

If your account receives the StoreKit External Purchase Link entitlement or the StoreKit External Purchase Link Regions entitlement, implement the following to offer multiple external purchase links:

- Depending on the entitlement you receive, configure the doc://com.apple.documentation/documentation/bundleresources/entitlements/com.apple.developer.storekit.external-purchase-link.allowed-regions entitlement for your app, or the [`com.apple.developer.storekit.external-purchase-link`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.storekit.external-purchase-link).
- Configure the [`SKExternalPurchaseMultiLink`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SKExternalPurchaseMultiLink) property list key, providing one or more external purchase links for each permitted country code.
- Use the [`ExternalPurchaseLink`](externalpurchaselink.md) type’s [`eligibleURLs`](externalpurchaselink/eligibleurls.md) array to determine whether one or more external purchase links are available, then select one of those eligible URLs.
- Call the [`open(url:)`](externalpurchaselink/open(url:).md) method with the URL you select. StoreKit appends the external purchase token to your website’s URL. Use this token to record purchases.
- From your server, report the external purchase tokens and the transactions associated with the tokens by using the [`External Purchase Server API`](https://developer.apple.com/documentation/ExternalPurchaseServerAPI).

##### Offer a Single External Purchase Link Out for Each Country Code

If your account receives the StoreKit External Purchase Link entitlement or the StoreKit External Purchase Link Regions entitlement, implement the following to offer a single external purchase link for each country code:

- Depending on the entitlement your app receives, configure the  doc://com.apple.documentation/documentation/bundleresources/entitlements/com.apple.developer.storekit.external-purchase-link.allowed-regions entitlement for your app, or the [`com.apple.developer.storekit.external-purchase-link`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.storekit.external-purchase-link) entitlement.
- Configure the [`SKExternalPurchaseLink`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SKExternalPurchaseLink) property list key, providing one external purchase link for each permitted country code.
- Use the [`ExternalPurchaseLink`](externalpurchaselink.md) type’s [`canOpen`](externalpurchaselink/canopen.md) property to determine whether external purchase link is available.
- Call the [`open()`](externalpurchaselink/open().md) method. StoreKit appends the external purchase token to your website’s URL. Use this token to record purchases.
- From your server, report the external purchase tokens and the transactions associated with the tokens by using the [`External Purchase Server API`](https://developer.apple.com/documentation/ExternalPurchaseServerAPI).

Your app may configure both the [`SKExternalPurchaseLink`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SKExternalPurchaseLink) and [`SKExternalPurchaseMultiLink`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SKExternalPurchaseMultiLink) property list keys.

##### Record and Report External Purchase Tokens and Associated Transactions

An external purchase token is a unique string that your app or website receives when your app’s customer chooses to view your external purchase offerings. Record all tokens in your system and report them and their associated transactions using the [`External Purchase Server API`](https://developer.apple.com/documentation/ExternalPurchaseServerAPI). For more information about tokens, see [`Receiving and decoding external purchase tokens`](receiving-and-decoding-external-purchase-tokens.md).

##### Check Api Availability

The External Purchase APIs, including [`ExternalPurchaseLink`](externalpurchaselink.md), [`ExternalPurchase`](externalpurchase.md), and [`ExternalPurchaseCustomLink`](externalpurchasecustomlink.md) provide  that you use to report transactions to Apple. [`ExternalPurchaseLink`](externalpurchaselink.md) and [`ExternalPurchase`](externalpurchase.md) are available starting in iOS 17.4, iPadOS 17.4, macOS 14.4, Mac Catalyst 17.4, tvOS 17.4, visionOS 1.1, and watchOS 10.4. [`ExternalPurchaseCustomLink`](externalpurchasecustomlink.md) is available starting in iOS 18.1, iPadOS 18.1, Mac Catalyst 18.1, and macOS 15.1.

For apps that run on iOS 15.4 through 17.3 and iPadOS 15.4 through 17.3, the External Purchase APIs have the following behavior:

- [`ExternalPurchase`](externalpurchase.md) and [`ExternalPurchaseLink`](externalpurchaselink.md) APIs throw errors or return `false` for compatible iPad or iPhone apps running in visionOS, on a Mac with Apple silicon, or on a Mac app built with Mac Catalyst.
- The APIs don’t provide external purchase tokens.
- The APIs are available in iOS and iPadOS only.

## Topics

### Offering external purchases
- [enum ExternalPurchase](externalpurchase.md)
  A value that enables qualifying apps to offer external purchases within the app.
- [com.apple.developer.storekit.external-purchase](../BundleResources/Entitlements/com.apple.developer.storekit.external-purchase.md)
  A Boolean value that indicates whether your app can offer external purchases.
- [SKExternalPurchase](../BundleResources/Information-Property-List/SKExternalPurchase.md)
  A string array of country codes that indicates your app supports external purchases.
### Communicating and promoting offers
- [enum ExternalPurchaseCustomLink](externalpurchasecustomlink.md)
  A value that enables qualifying apps to offer custom links for external purchases and use alternative payment service providers.
- [ExternalPurchaseCustomLink.Token](externalpurchasecustomlink/token.md)
  A token you use with the External Purchase custom link API.
- [com.apple.developer.storekit.custom-purchase-link.allowed-regions](../BundleResources/Entitlements/com.apple.developer.storekit.custom-purchase-link.allowed-regions.md)
  An entitlement that enables a qualifying app to offer external purchases within app or at a website, in specific regions.
- [com.apple.developer.storekit.external-purchase-link](../BundleResources/Entitlements/com.apple.developer.storekit.external-purchase-link.md)
  A Boolean value that indicates whether your app can include a link that directs people to a website to make an external purchase.
- [SKExternalPurchaseCustomLinkRegions](../BundleResources/Information-Property-List/SKExternalPurchaseCustomLinkRegions.md)
  An array of country code strings that indicate the regions where your app supports custom links for the communication and promotion of offers.
- [Testing transactions that use custom link tokens](testing-transactions-that-use-custom-link-tokens.md)
  Recognize custom link tokens that your app receives in the sandbox testing environment, and use them to test reporting transactions.
### Communicating and promoting offers for music streaming services
- [enum ExternalPurchaseCustomLink](externalpurchasecustomlink.md)
  A value that enables qualifying apps to offer custom links for external purchases and use alternative payment service providers.
- [com.apple.developer.storekit.external-purchase-link-streaming](../BundleResources/Entitlements/com.apple.developer.storekit.external-purchase-link-streaming.md)
  An entitlement that grants a qualifying music-streaming app the ability to communicate and promote offers.
- [SKExternalPurchaseLinkStreamingRegions](../BundleResources/Information-Property-List/SKExternalPurchaseLinkStreamingRegions.md)
  A list of country codes that indicate the regions where your music-streaming app communicates and promotes offers.
### Offering external purchase links
- [enum ExternalPurchaseLink](externalpurchaselink.md)
  A value that enables qualifying apps to offer external purchase links.
- [com.apple.developer.storekit.external-purchase-link](../BundleResources/Entitlements/com.apple.developer.storekit.external-purchase-link.md)
  A Boolean value that indicates whether your app can include a link that directs people to a website to make an external purchase.
- [SKExternalPurchaseMultiLink](../BundleResources/Information-Property-List/SKExternalPurchaseMultiLink.md)
  A dictionary that contains an array of URLs to websites where people using your app can make external purchases.
- [SKExternalPurchaseLink](../BundleResources/Information-Property-List/SKExternalPurchaseLink.md)
  A dictionary that contains URLs to websites where people using your app can make external purchases for supported regions.
### Managing external purchase tokens
- [Receiving and decoding external purchase tokens](receiving-and-decoding-external-purchase-tokens.md)
  Receive tokens for external purchases that you use to report transactions to Apple.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/external-purchase)*