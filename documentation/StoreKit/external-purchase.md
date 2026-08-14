# External Purchase

**Framework**: StoreKit

Enable qualifying apps to offer external purchases.

#### Overview

The External Purchase APIs allow qualifying apps to implement external purchases. External purchases allow customers to complete purchases:

- within the app, using an alternative payment service provider
- outside of the app, after linking-out of the app

If you develop a qualifying app, you may complete a request for optional entitlements that allow you to offer external purchases. For more information about whether your app qualifies, requesting an entitlement, and implementation requirements, see:

- [`Communication and promotion of offers on the App Store in the EU`](https://developer.apple.comhttps://developer.apple.com/support/communication-and-promotion-of-offers-on-the-app-store-in-the-eu/)
- [`Distributing dating apps in the Netherlands`](https://developer.apple.comhttps://developer.apple.com/support/storekit-external-entitlement/)
- [`Distributing apps in Russia that provide an external purchase link`](https://developer.apple.comhttps://developer.apple.com/contact/request/storekit-external-entitlement-ru/)
- [`Distributing apps using a third-party payment provider in South Korea`](https://developer.apple.comhttps://developer.apple.com/support/storekit-external-entitlement-kr/)
- [`Distributing music streaming apps in the EEA that provide an external purchase link`](https://developer.apple.comhttps://developer.apple.com/support/music-streaming-services-entitlement-eea/)
- [`Payment options on the App Store in Brazil`](https://developer.apple.comhttps://developer.apple.com/support/payment-options-on-the-app-store-in-brazil)
- [`Payment options on the App Store in Japan`](https://developer.apple.comhttps://developer.apple.com/support/payment-options-on-the-app-store-in-japan)

Use the API based on the entitlements your app receives and the regions where your app runs.

##### Implement External Purchases Using Alternative Payment Service Providers in the European Union Eu and South Korea

If your account receives the StoreKit External Purchase entitlement or the StoreKit External Purchase Regions entitlement, implement the following to offer external purchases within your app:

- Configure the [`com.apple.developer.storekit.external-purchase`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.storekit.external-purchase) entitlement for your app and the [`SKExternalPurchase`](https://developer.apple.com/documentation/bundleresources/information-property-list/skexternalpurchase) property list key.
- Use the [`ExternalPurchase`](externalpurchase.md) type’s [`canPresent`](externalpurchase/canpresent.md) property to determine whether external purchase is available. If the value is `false`, don’t continue to use this API. See [`canPresent`](externalpurchase/canpresent.md) for more details.
- Call the [`presentNoticeSheet()`](externalpurchase/presentnoticesheet().md) method and use the external purchase token you receive from the [`ExternalPurchase.NoticeResult.continuedWithExternalPurchaseToken(token:)`](externalpurchase/noticeresult/continuedwithexternalpurchasetoken(token:).md) result to record transactions.
- From your server, report the external purchase tokens and the transactions associated with the tokens by using the [`External Purchase Server API`](https://developer.apple.com/documentation/externalpurchaseserverapi).

##### Implement External Purchase for Apps Available in the Eu

If your account receives the StoreKit External Purchase Link entitlement or the StoreKit External Custom Purchase Link Regions entitlement, in the EU your app can use the [`ExternalPurchaseCustomLink`](externalpurchasecustomlink.md) API to implement external purchases. To use this API, complete the following steps:

- Depending on the entitlement you receive, configure the [`com.apple.developer.storekit.custom-purchase-link.allowed-regions`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.storekit.custom-purchase-link.allowed-regions) entitlement for your app, or the [`com.apple.developer.storekit.external-purchase-link`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.storekit.external-purchase-link) entitlement and the [`SKExternalPurchaseCustomLinkRegions`](https://developer.apple.com/documentation/bundleresources/information-property-list/skexternalpurchasecustomlinkregions) property list key, providing the country code for each permitted region where your app implements external purchases.
- Check the [`isEligible`](externalpurchasecustomlink/iseligible.md) property of the [`ExternalPurchaseCustomLink`](externalpurchasecustomlink.md) API to determine whether the API is available at runtime. If the value is `false`, don’t continue to use this API. For more information, see [`isEligible`](externalpurchasecustomlink/iseligible.md).
- At launch and before every potential transaction, call the [`token(for:)`](externalpurchasecustomlink/token(for:).md) function to request the external purchase tokens, using the token types `ACQUISITION` and `SERVICES`. Associate these tokens with a customer account on your server.
- Call the [`showNotice(type:)`](externalpurchasecustomlink/shownotice(type:).md) function after a deliberate customer interaction, such as tapping a button, that can lead to a potential external purchase.
- From your server, report the external purchase tokens and the transactions associated with the tokens by using the [`External Purchase Server API`](https://developer.apple.com/documentation/externalpurchaseserverapi).

##### Implement External Purchase for Apps Available in Brazil

If your account receives the StoreKit External Custom Purchase Link Regions entitlement, in Brazil your app can use the [`ExternalPurchaseCustomLink`](externalpurchasecustomlink.md) API to implement external purchases starting in iOS 26.5.  To use this API, complete the following steps:

- Configure the [`com.apple.developer.storekit.custom-purchase-link.allowed-regions`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.storekit.custom-purchase-link.allowed-regions) entitlement for your app.
- Check the [`isEligible`](externalpurchasecustomlink/iseligible.md) property of the [`ExternalPurchaseCustomLink`](externalpurchasecustomlink.md) API to determine whether the API is available at runtime. If the value is `false`, don’t continue to use this API. For more information, see  [`isEligible`](externalpurchasecustomlink/iseligible.md).
- Call the [`token(for:)`](externalpurchasecustomlink/token(for:).md) function before every potential transaction to request external purchase tokens, using the token types `IN_APP` or `LINK_OUT`. For more information, see [`token(for:)`](externalpurchasecustomlink/token(for:).md).
- Before routing customers to external purchase options, display an in-app disclosure sheet that lets people know they’ll be transacting with you and not Apple. For more information, including downloadable resources, see the “In-app disclosure sheet” section of [`Payment options on the App Store in Brazil`](https://developer.apple.comhttps://developer.apple.com/support/payment-options-on-the-app-store-in-brazil).
- Report the external purchase tokens and the transactions associated with the tokens using the [`External Purchase Server API`](https://developer.apple.com/documentation/externalpurchaseserverapi). Otherwise, report transactions as indicated in [`Payment options on the App Store in Brazil`](https://developer.apple.comhttps://developer.apple.com/support/payment-options-on-the-app-store-in-brazil).

##### Implement External Purchase for Apps Available in Japan

If your account receives the StoreKit External Custom Purchase Link Regions entitlement, in Japan your app can use the [`ExternalPurchaseCustomLink`](externalpurchasecustomlink.md) API to implement external purchases starting in iOS 26.2.  To use this API, complete the following steps:

- Configure the [`com.apple.developer.storekit.custom-purchase-link.allowed-regions`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.storekit.custom-purchase-link.allowed-regions) entitlement for your app.
- Check the [`isEligible`](externalpurchasecustomlink/iseligible.md) property of the [`ExternalPurchaseCustomLink`](externalpurchasecustomlink.md) API to determine whether the API is available at runtime. If the value is `false`, don’t continue to use this API. For more information, see  [`isEligible`](externalpurchasecustomlink/iseligible.md).
- Starting in iOS 26.4, call the [`token(for:)`](externalpurchasecustomlink/token(for:).md) function before every potential transaction to request external purchase tokens, using the token types `IN_APP` or `LINK_OUT`. For more information, see [`token(for:)`](externalpurchasecustomlink/token(for:).md).
- Before routing customers to external purchase options, display an in-app disclosure sheet that lets people know they’ll be transacting with you and not Apple. For more information, including downloadable resources, see the “In-app disclosure sheet” section of [`Payment options on the App Store in Japan`](https://developer.apple.comhttps://developer.apple.com/support/payment-options-on-the-app-store-in-japan).
- Starting in iOS 26.4, report the external purchase tokens and the transactions associated with the tokens using the [`External Purchase Server API`](https://developer.apple.com/documentation/externalpurchaseserverapi). Otherwise, report transactions as indicated in [`Payment options on the App Store in Japan`](https://developer.apple.comhttps://developer.apple.com/support/payment-options-on-the-app-store-in-japan).

##### Implement External Purchase for Music Streaming Apps in the European Economic Area Eea

If your account receives the Music Streaming Services EEA entitlement, your music streaming app can use the [`ExternalPurchaseCustomLink`](externalpurchasecustomlink.md) API to implement external purchases. To use this API, complete the following steps:

- Configure the [`com.apple.developer.storekit.external-purchase-link-streaming`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.storekit.external-purchase-link-streaming) entitlement for your app and the [`SKExternalPurchaseLinkStreamingRegions`](https://developer.apple.com/documentation/bundleresources/information-property-list/skexternalpurchaselinkstreamingregions) property list key, providing the country code for each permitted region where your app implements external purchase.
- Check the [`isEligible`](externalpurchasecustomlink/iseligible.md) property of the [`ExternalPurchaseCustomLink`](externalpurchasecustomlink.md) API to determine whether external purchase is available at runtime. If the value is `false`, don’t continue to use this API. See [`isEligible`](externalpurchasecustomlink/iseligible.md) for more details.
- At launch and before every potential transaction, call the [`token(for:)`](externalpurchasecustomlink/token(for:).md) function to request the external purchase tokens, using the token types `ACQUISITION` and `SERVICES`. Associate these tokens with a customer account on your server.
- Call the [`showNotice(type:)`](externalpurchasecustomlink/shownotice(type:).md) function after a deliberate customer interaction, such as tapping a button, and before offering external purchases.
- From your server, report the external purchase tokens and the transactions associated with the tokens by using the [`External Purchase Server API`](https://developer.apple.com/documentation/externalpurchaseserverapi).

##### Implement External Purchase Through Multiple Links for the European Economic Area Eea and Russia

If your account receives the StoreKit External Purchase Link entitlement or the StoreKit External Purchase Link Regions entitlement, in the EEA and Russia you can implement the following to offer multiple external purchase links:

- Configure the [`com.apple.developer.storekit.external-purchase-link`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.storekit.external-purchase-link) entitlement for your app.
- Configure the [`SKExternalPurchaseMultiLink`](https://developer.apple.com/documentation/bundleresources/information-property-list/skexternalpurchasemultilink) property list key, providing one or more external purchase links for each permitted country code.
- Use the [`ExternalPurchaseLink`](externalpurchaselink.md) type’s [`eligibleURLs`](externalpurchaselink/eligibleurls.md) array to determine whether one or more external purchase links are available, then select one of those eligible URLs. If the value is `nil`, see [`eligibleURLs`](externalpurchaselink/eligibleurls.md) for more information.
- Call the [`open(url:)`](externalpurchaselink/open(url:).md) method with the URL you select. StoreKit appends the external purchase token to your website’s URL. Use this token to record purchases.
- From your server, report the external purchase tokens and the transactions associated with the tokens by using the [`External Purchase Server API`](https://developer.apple.com/documentation/externalpurchaseserverapi).

##### Implement External Purchase Through Single Links for the European Economic Area Eea and Russia

If your account receives the StoreKit External Purchase Link entitlement or the StoreKit External Purchase Link Regions entitlement, implement the following to offer a single external purchase link for each country code:

- Configure the [`com.apple.developer.storekit.external-purchase-link`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.storekit.external-purchase-link) entitlement for your app.
- Configure the [`SKExternalPurchaseLink`](https://developer.apple.com/documentation/bundleresources/information-property-list/skexternalpurchaselink) property list key, providing one external purchase link for each permitted country code.
- Use the [`ExternalPurchaseLink`](externalpurchaselink.md) type’s [`canOpen`](externalpurchaselink/canopen.md) property to determine whether external purchase link is available. If the value is `false`, don’t continue to use this API. For more information, see [`canOpen`](externalpurchaselink/canopen.md).
- Call the [`open()`](externalpurchaselink/open().md) method. StoreKit appends the external purchase token to your website’s URL. Use this token to record purchases.
- From your server, report the external purchase tokens and the transactions associated with the tokens by using the [`External Purchase Server API`](https://developer.apple.com/documentation/externalpurchaseserverapi).

Your app may configure both the [`SKExternalPurchaseLink`](https://developer.apple.com/documentation/bundleresources/information-property-list/skexternalpurchaselink) and [`SKExternalPurchaseMultiLink`](https://developer.apple.com/documentation/bundleresources/information-property-list/skexternalpurchasemultilink) property list keys.

##### Record and Report External Purchase Tokens and Associated Transactions

An external purchase token is a unique string that your app or website receives when your app’s customer chooses to view your external purchase offerings. Record all tokens in your system and report them and their associated transactions using the [`External Purchase Server API`](https://developer.apple.com/documentation/externalpurchaseserverapi). For more information about tokens, see [`Receiving and decoding external purchase tokens`](receiving-and-decoding-external-purchase-tokens.md).

##### Check Api Availability

The External Purchase APIs, including [`ExternalPurchaseLink`](externalpurchaselink.md), [`ExternalPurchase`](externalpurchase.md), and [`ExternalPurchaseCustomLink`](externalpurchasecustomlink.md) provide *external purchase tokens* that you use to report transactions to Apple:

- [`ExternalPurchaseLink`](externalpurchaselink.md) and [`ExternalPurchase`](externalpurchase.md) are available starting in iOS 17.4, iPadOS 17.4, macOS 14.4, Mac Catalyst 17.4, tvOS 17.4, visionOS 1.1, and watchOS 10.4.
- [`ExternalPurchaseCustomLink`](externalpurchasecustomlink.md) is available starting in iOS 18.1, iPadOS 18.1, Mac Catalyst 18.1, and macOS 15.1; for use in Brazil, it and [`token(for:)`](externalpurchasecustomlink/token(for:).md) are available starting in iOS 26.5; for use in Japan, it’s available starting in iOS 26.2, with [`token(for:)`](externalpurchasecustomlink/token(for:).md) available starting in iOS 26.4.

For apps that run on iOS 15.4 through 17.3 and iPadOS 15.4 through 17.3, the External Purchase APIs have the following behavior:

- [`ExternalPurchase`](externalpurchase.md) and [`ExternalPurchaseLink`](externalpurchaselink.md) APIs throw errors or return `false` for compatible iPad or iPhone apps running in visionOS, on a Mac with Apple silicon, or on a Mac app built with Mac Catalyst.
- The APIs don’t provide external purchase tokens.
- The APIs are available in iOS and iPadOS only.

## Topics

### Managing external purchase tokens
- [Receiving and decoding external purchase tokens](receiving-and-decoding-external-purchase-tokens.md)
  Receive tokens for external purchases that you use to report transactions to Apple.
### Implementing alternative payment service providers in the EU and South Korea
- [enum ExternalPurchase](externalpurchase.md)
  An enumeration that enables qualifying apps to offer external purchases within the app.
- [com.apple.developer.storekit.external-purchase](../bundleresources/entitlements/com.apple.developer.storekit.external-purchase.md)
  A Boolean value that indicates whether your app can offer external purchases.
- [SKExternalPurchase](../bundleresources/information-property-list/skexternalpurchase.md)
  A string array of country codes that indicates your app supports external purchases.
### Implementing external purchases in the EU
- [enum ExternalPurchaseCustomLink](externalpurchasecustomlink.md)
  An enumeration that enables qualifying apps to offer custom links for external purchases and use alternative payment service providers.
- [ExternalPurchaseCustomLink.Token](externalpurchasecustomlink/token.md)
  A token you use with the External Purchase custom link API.
- [com.apple.developer.storekit.custom-purchase-link.allowed-regions](../bundleresources/entitlements/com.apple.developer.storekit.custom-purchase-link.allowed-regions.md)
  An entitlement that enables a qualifying app to offer external purchases within app or at a website, in specific regions.
- [com.apple.developer.storekit.external-purchase-link](../bundleresources/entitlements/com.apple.developer.storekit.external-purchase-link.md)
  A Boolean value that indicates whether your app can include a link that directs people to a website to make an external purchase.
- [SKExternalPurchaseCustomLinkRegions](../bundleresources/information-property-list/skexternalpurchasecustomlinkregions.md)
  An array of country code strings that indicate the regions where your app supports custom links for the communication and promotion of offers.
- [Testing transactions that use custom link tokens](testing-transactions-that-use-custom-link-tokens.md)
  Recognize custom link tokens that your app receives in the sandbox testing environment, and use them to test reporting transactions.
### Implementing external purchases in Japan
- [enum ExternalPurchaseCustomLink](externalpurchasecustomlink.md)
  An enumeration that enables qualifying apps to offer custom links for external purchases and use alternative payment service providers.
- [com.apple.developer.storekit.custom-purchase-link.allowed-regions](../bundleresources/entitlements/com.apple.developer.storekit.custom-purchase-link.allowed-regions.md)
  An entitlement that enables a qualifying app to offer external purchases within app or at a website, in specific regions.
### Implementing external purchases for music streaming services in the EU
- [enum ExternalPurchaseCustomLink](externalpurchasecustomlink.md)
  An enumeration that enables qualifying apps to offer custom links for external purchases and use alternative payment service providers.
- [com.apple.developer.storekit.external-purchase-link-streaming](../bundleresources/entitlements/com.apple.developer.storekit.external-purchase-link-streaming.md)
  An entitlement that grants a qualifying music-streaming app the ability to communicate and promote offers.
- [SKExternalPurchaseLinkStreamingRegions](../bundleresources/information-property-list/skexternalpurchaselinkstreamingregions.md)
  A list of country codes that indicate the regions where your music-streaming app communicates and promotes offers.
### Implementing single and multiple external purchase links in the European Economic Area (EEA) and Russia
- [enum ExternalPurchaseLink](externalpurchaselink.md)
  An enumeration that enables qualifying apps to offer external purchase links.
- [com.apple.developer.storekit.external-purchase-link](../bundleresources/entitlements/com.apple.developer.storekit.external-purchase-link.md)
  A Boolean value that indicates whether your app can include a link that directs people to a website to make an external purchase.
- [SKExternalPurchaseMultiLink](../bundleresources/information-property-list/skexternalpurchasemultilink.md)
  A dictionary that contains an array of URLs to websites where people using your app can make external purchases.
- [SKExternalPurchaseLink](../bundleresources/information-property-list/skexternalpurchaselink.md)
  A dictionary that contains URLs to websites where people using your app can make external purchases for supported regions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/external-purchase)*