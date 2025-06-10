# Creating an attributable ad link

**Framework**: SKAdNetwork for Web Ads

Create click-through web ads that attribute App Store app installations to your ad network.

#### Overview

The web provides a broad platform for advertising apps to a wide audience. In iOS 16.1 and later, ad networks can use the [`SKAdNetwork for Web Ads`](SKAdNetworkforWebAds.md) API to get [`SKAdNetwork`](https://developer.apple.com/documentation/StoreKit/SKAdNetwork) attributions for App Store app installations that originate from web ads in Safari.

##### Register an Ad Network

Before creating an attributable ad link, you need to register your ad network with Apple. For information, see [`Registering an ad network`](https://developer.apple.com/documentation/StoreKit/registering-an-ad-network).

##### Create a Link with the Expected Format

To receive app-installation attribution from a web ad, provide a specialized link that directs a person to download the advertised app from the App Store. The link needs to be in the following format:

```xml
<a href="https://apps.apple.com/app/id{itunes_item_id}" 
attributionDestination="https://example.com" 
attributionSourceNonce="t8naKxXHTzuTJhNfljADPQ">
</a>
```

Provide the following values to retrieve the full [`SKAdNetwork`](https://developer.apple.com/documentation/StoreKit/SKAdNetwork) attribution information when a person clicks the ad:

The `attributionSourceNonce` in a web ad link, the `source_nonce` in an [`AdImpressionRequest`](adimpressionrequest.md), and the `nonce` in an [`AdImpressionResponse`](adimpressionresponse.md) all represent the same UUID, but the encoding varies.

To generate an `attributionSourceNonce` for a web ad, Base64URL-encode the raw bytes of the UUID. Don’t encode a string representation of the UUID or lowercase the encoded UUID. The device uses the same encoding as `attributionSourceNonce` for the `source_nonce` value in the [`AdImpressionRequest`](adimpressionrequest.md). However, you use the dash-separated string representation of the UUID for the `nonce` value in an [`AdImpressionResponse`](adimpressionresponse.md).

##### Use the Link in a Web Ad

Add the link to an advertisement or an app promotion on the webpage where you want people to encounter it. You can cover the entire advertisement with the link or include it as a pure hyperlink to the App Store.

##### Implement the Signed Web Ad Impression Endpoint

When a person clicks the web ad, their device generates an [`AdImpressionRequest`](adimpressionrequest.md) using the information from the web ad link. The device then sends a request to the [`Get a Signed Web Ad Impression Payload`](get-a-signed-skadnetwork-ad-payload-for-a-web-ad..md) endpoint with the ad-impression request in the request body.

> ❗ **Important**:  The device doesn’t follow an HTTP redirect when it sends the request to the [`Get a Signed Web Ad Impression Payload`](get-a-signed-skadnetwork-ad-payload-for-a-web-ad..md) endpoint at the `attributionDestination` URL.

On your server, implement the [`Get a Signed Web Ad Impression Payload`](get-a-signed-skadnetwork-ad-payload-for-a-web-ad..md) endpoint to return an [`AdImpressionResponse`](adimpressionresponse.md). For an example of the response format, see [`AdImpressionResponse`](adimpressionresponse.md).

For more information about generating the signature in your response, see [`Generating a signature for attributable web ads`](generating-a-signature-for-attributable-web-ads.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/skadnetworkforwebads/creating-an-attributable-ad-link)*