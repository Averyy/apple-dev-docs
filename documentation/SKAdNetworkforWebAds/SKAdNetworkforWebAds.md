# SKAdNetwork for Web Ads

**Framework**: SKAdNetwork for Web Ads  
**Kind**: module

Attribute app-install campaigns that originate on the web.

**Availability**:
- SKAdNetwork for Web Ads 1.0+

## Mentions

- [Creating an attributable ad link](creating-an-attributable-ad-link.md)

#### Overview

The [`SKAdNetwork for Web Ads`](SKAdNetworkforWebAds.md) API enables advertisers to measure the success of ad campaigns that initiate on the web, while maintaining user privacy. In iOS 16.1 and later, ad networks can use this API to get [`SKAdNetwork`](https://developer.apple.com/documentation/StoreKit/SKAdNetwork) attributions for web ad clicks in Safari that lead to app installations from the App Store.

To use the API, follow these steps:

1. Register your ad network; see [`Registering an ad network`](https://developer.apple.com/documentation/StoreKit/registering-an-ad-network).
2. Configure and display your web ad link; see [`Creating an attributable ad link`](creating-an-attributable-ad-link.md).
3. Implement an endpoint to provide a signed web ad payload that the advertised app uses to attribute app installations to your ad campaign; see [`Generating a signature for attributable web ads`](generating-a-signature-for-attributable-web-ads.md).
4. Validate any attributions you receive; see [`Verifying an install-validation postback`](https://developer.apple.com/documentation/StoreKit/verifying-an-install-validation-postback).

For more information about the ad network API, see [`SKAdNetwork`](https://developer.apple.com/documentation/StoreKit/SKAdNetwork).

> **Note**:  Ad networks can only use this API to get attributions for web ad clicks in Safari; the API doesn’t get attributions for web ad clicks in [`SFSafariViewController`](https://developer.apple.com/documentation/SafariServices/SFSafariViewController) or [`WKWebView`](https://developer.apple.com/documentation/WebKit/WKWebView).

## Topics

### Essentials
- [Creating an attributable ad link](creating-an-attributable-ad-link.md)
  Create click-through web ads that attribute App Store app installations to your ad network.
### Receiving a request for a web ad  payload
- [Get a Signed Web Ad Impression Payload](get-a-signed-skadnetwork-ad-payload-for-a-web-ad..md)
  An endpoint you provide to receive requests from devices to serve signed ad interactions.
- [object AdImpressionRequest](adimpressionrequest.md)
  The request body that devices send to fetch the web ad impression from the ad network’s server.
### Providing the web ad signature and response
- [Generating a signature for attributable web ads](generating-a-signature-for-attributable-web-ads.md)
  Initiate install-validation by providing the signed parameters for an attributable web ad.
- [object AdImpressionResponse](adimpressionresponse.md)
  The response you provide that contains a signed payload for a clicked web ad.
- [object signature](signature.md)
  The key-value pairs that ad networks use to cryptographically sign a web ad.


---

*[View on Apple Developer](https://developer.apple.com/documentation/SKAdNetworkforWebAds)*