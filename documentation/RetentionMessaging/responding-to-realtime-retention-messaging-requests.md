# Responding to real-time retention messaging requests

**Framework**: Retention Messaging API

Select retention messages for customers in real time by responding to requests on your Get Retention Message endpoint.

#### Overview

The App Store server sends a request to your `Get Retention Message` endpoint in real time when a customer is viewing subscription details and can potentially cancel the subscription. In your response, you choose a retention message from messages you configure in advance. Use the information in the request body, [`RealtimeRequestBody`](realtimerequestbody.md), to help inform your choice. The system displays the retention message you choose to the customer. If your server response fails for any reason, the system displays a default retention message that you configure in advance.

Your server is responsible for parsing, interpreting, and responding to all server-to-server posts. For more information about the `Get Retention Message` endpoint. see [`Setting up your Get Retention Message endpoint`](setting-up-retention-messaging-endpoint.md). For more information about setting up the messages you can use in the response, see [`Setting up retention messages`](setting-up-retention-messages.md).

##### Parse the Request Body

The request body payload contains the information you use to decide which retention message to show the customer, such as the product ID, locale, and original transaction ID.

The body of the POST is a [`RealtimeRequestBody`](realtimerequestbody.md), which consists of a [`signedPayload`](signedpayload.md). The `signedPayload` is a string of three Base64URL-encoded components separated by a period. The string contains the JWS Compact Serialization of the request body, signed by the App Store in a JSON Web Signature (JWS) format. The three components of the string are a header, a payload, and a signature, in that order.

Parse the signed payload and validate the signature as follows:

- To read the header, Base64URL-decode the header component and use a [`JWSDecodedHeader`](jwsdecodedheader.md) object to access the information.
- Use the information in the header to verify the JWS signature. For more information on verifying the signature, see [`JWSDecodedHeader`](jwsdecodedheader.md).
- To read the payload, Base64URL-decode the payload component. Use a [`DecodedRealtimeRequestBody`](decodedrealtimerequestbody.md) object to read the payload information.

##### Respond to the Post

Respond to the post with a [`RealtimeResponseBody`](realtimeresponsebody.md) and a `200` status code. Your response identifies the retention message you choose to show the customer. The system displays your chosen message after the customer selects Cancel Subscription on the Apple Account > Subscriptions page.

> ❗ **Important**: Your server needs to respond quickly, within 700 ms; otherwise, the App Store server times out and the request fails.

If the request fails for any reason, the API uses the default message for the customer’s product ID and locale. If you don’t have a configured default retention message, the system doesn’t display a retention message. For more information on default messages, see [`Setting up retention messages`](setting-up-retention-messages.md).

## See Also

- [Setting up your Get Retention Message endpoint](setting-up-retention-messaging-endpoint.md)
  Choose retention messages for customers in real time by implementing an endpoint on your server that responds to requests from the App Store server.
- [object RealtimeRequestBody](realtimerequestbody.md)
  The request body the App Store server sends to your Get Retention Message endpoint.
- [object DecodedRealtimeRequestBody](decodedrealtimerequestbody.md)
  The decoded request body the App Store sends to your server to request a real-time retention message.
- [object RealtimeResponseBody](realtimeresponsebody.md)
  A response you provide to choose, in real time, a retention message the system displays to the customer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/responding-to-realtime-retention-messaging-requests)*