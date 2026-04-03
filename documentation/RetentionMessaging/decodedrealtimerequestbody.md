# DecodedRealtimeRequestBody

**Framework**: Retention Messaging API  
**Kind**: dictionary

The decoded request body the App Store sends to your server to request a real-time retention message.

**Availability**:
- Retention Messaging API 1.0+

## Declaration

```swift
object DecodedRealtimeRequestBody
```

## Mentions

- [Responding to real-time retention messaging requests](responding-to-realtime-retention-messaging-requests.md)
- [Retention Messaging API changelog](retention-messaging-changelog.md)
- [Setting up your Get Retention Message endpoint](setting-up-retention-messaging-endpoint.md)

#### Discussion

The App Store server sends a request to your `Get Retention Message` endpoint that includes a [`RealtimeRequestBody`](realtimerequestbody.md). The `DecodedRealtimeRequestBody` is the decoded version of that request body.

The `DecodedRealtimeRequestBody` provides information you can use to select a retention message for display. The request includes the customer’s original transaction identifier, the product identifier, and their locale. Consider this information, along with your business logic, to choose the best retention message for the customer.

> ❗ **Important**: Always check that the `appAppleId` in the request matches your app’s `appAppleId`. If it doesn’t match, don’t respond to the request.

For more information, see [`Responding to real-time retention messaging requests`](responding-to-realtime-retention-messaging-requests.md).

## Properties

- `originalTransactionId` (originalTransactionId) *(required)*: The original transaction identifier of the customer’s subscription.
- `appAppleId` (appAppleId) *(required)*: The unique identifier of the app in the App Store.
- `productId` (productId) *(required)*: The unique identifier of the auto-renewable subscription.
- `userLocale` (locale) *(required)*: The device’s locale.
- `requestIdentifier` (requestIdentifier) *(required)*: A UUID the App Store server creates to uniquely identify each request.
- `environment` (environment) *(required)*: The server environment, either sandbox or production.
- `signedDate` (signedDate) *(required)*: The UNIX time, in milliseconds, that the App Store signed the JSON Web Signature (JWS) data.

## See Also

- [Responding to real-time retention messaging requests](responding-to-realtime-retention-messaging-requests.md)
  Select retention messages for customers in real time by responding to requests on your Get Retention Message endpoint.
- [object RealtimeResponseBody](realtimeresponsebody.md)
  A response you provide to choose, in real time, a retention message the system displays to the customer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/decodedrealtimerequestbody)*