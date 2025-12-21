# Data types

**Framework**: Retention Messaging API

Refer to these data types for request and response payloads.

## Topics

### Images
- [type imageIdentifier](imageidentifier.md)
  A unique identifier for an image that you provide when you upload the image.
- [type imageState](imagestate.md)
  The approval state of an image.
- [type altText](alttext.md)
  The alternative text for a corresponding image.
### Messages
- [type messageIdentifier](messageidentifier.md)
  A unique identifier for a message, which you provide when you upload the message.
- [type messageState](messagestate.md)
  The approval state of the message.
- [type body](body.md)
  The body text you provide for a message.
- [type header](header.md)
  The header text you provide for a message.
### Default message configuration
- [type locale](locale.md)
  A string that represents a locale short code.
- [type productId](productid.md)
  A unique identifier for a product, which you create in App Store Connect.
### Real-time request body
- [type signedPayload](signedpayload.md)
  The payload in a JSON Web Signature (JWS) format, signed by the App Store.
- [type originalTransactionId](originaltransactionid.md)
  The original transaction identifier of an In-App Purchase.
- [type appAppleId](appappleid.md)
  The unique identifier of an app in the App Store.
- [type requestIdentifier](requestidentifier.md)
  A unique identifier the App Store server creates for its requests.
- [type signedDate](signeddate.md)
  The UNIX time, in milliseconds, that the App Store signed the JSON Web Signature data.
- [type environment](environment.md)
  The server environment, either sandbox or production.
### Real-time request header
- [object JWSDecodedHeader](jwsdecodedheader.md)
  A decoded JSON Web Signature (JWS) header.
- [type alg](alg.md)
  An algorithm you use to sign a JSON Web Signature (JWS).
- [type x5c](x5c.md)
  A JSON Web Signature (JWS) header parameter that contains the certificate chain that corresponds to the key you use to digitally sign the JWS.
### Real-time response body
- [object message](message.md)
  A message identifier you provide in a real-time response to your Get Retention Message endpoint.
- [object alternateProduct](alternateproduct.md)
  A switch-plan message and product ID you provide in a real-time response to your Get Retention Message endpoint.
- [object promotionalOffer](promotionaloffer.md)
  A promotional offer and message you provide in a real-time response to your Get Retention Message endpoint.
- [object advancedCommerceInfo](advancedcommerceinfo.md)
  A response object you provide to present an offer or switch-plan recommendation message.
### Advanced commerce information
- [type advancedCommerceData](advancedcommercedata.md)
  A Base64-encoded JSON object which contains a JWS with information describing an offer or switch-plan recommendation.
### Performance testing
- [object PerformanceTestConfig](performancetestconfig.md)
  An object that enumerates the test configuration parameters.
- [object PerformanceTestRequest](performancetestrequest.md)
  The object you provide to a performance test request that contains the test’s transaction identifier.
- [object PerformanceTestResponse](performancetestresponse.md)
  The performance test response object.
- [object PerformanceTestResponseTimes](performancetestresponsetimes.md)
  An object that describes test response times.
- [object PerformanceTestResultResponse](performancetestresultresponse.md)
  An object the API returns that describes the performance test results.
- [type PerformanceTestStatus](performanceteststatus.md)
  The status of the performance test.
- [object Failures](failures.md)
  A map of server-to-server notification failure reasons and counts that represent the number of failures during a performance test.
- [type sendAttemptResult](sendattemptresult.md)
  The success or error information the App Store server records when it attempts to send an App Store server notification to your server.
- [type requestId](requestid.md)
  The identifier of the performance test request.
### Promotional offer signature V2
- [type promotionalOfferSignatureV2](promotionaloffersignaturev2.md)
  The promotional-offer signature you generate in a JSON Web Signature (JWS) format.
### Promotional offer signature V1
- [object promotionalOfferSignatureV1](promotionaloffersignaturev1.md)
  The promotional offer signature you generate using an earlier signature version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/data-types)*