# Setting up your Get Retention Message endpoint

**Framework**: Retention Messaging API

Choose retention messages for customers in real time by implementing an endpoint on your server that responds to requests from the App Store server.

#### Overview

To receive requests from the App Store so that you can provide retention messages in real time, complete the following:

1. On your server, implement a `Get Retention Message` endpoint to the specifications described below.
2. Share your endpoint URL with Apple by using the form [`Request access to the Retention Messaging API`](https://developer.apple.comhttps://developer.apple.com/contact/request/retention-messaging-api/).

When you set up this endpoint, the App Store server delivers real-time requests when customers view a subscription detail page where they may choose to cancel the subscription. You respond to the request by choosing a retention message for the system to display to the customer. You set up the retention messages in advance. The system displays only messages where both the message and optional image have an `APPROVED` state.

Your server is responsible for parsing, interpreting, and responding to all server-to-server posts. For information about responding to requests, see [`Responding to real-time retention messaging requests`](responding-to-realtime-retention-messaging-requests.md).

##### Set Up Your Endpoint

Implement this endpoint on your server to the following specifications:

 `Get Retention Message`

 `POST https://example.com/<your URL>`

You determine the HTTPS URL on your server to receive the requests. Share this URL with Apple.

 [`RealtimeRequestBody`](realtimerequestbody.md)

The request body. For the decoded version, see [`DecodedRealtimeRequestBody`](decodedrealtimerequestbody.md).

 `200` - `OK`   [`RealtimeResponseBody`](realtimeresponsebody.md)
Your response body identifies the retention message to display to the customer.

If a request fails for any reason, the system displays a default retention message. If a default message isn’t available, the system doesn’t display a retention message. For more information about default messages, see [`Setting up retention messages`](setting-up-retention-messages.md).

##### Implement the Server Requirements

Set up secure communications with the App Store server by meeting the following requirements:

- Your domain must have a valid SSL certificate.
- Your endpoint must implement TLS 1.2.
- Your endpoint needs to respond within 700 ms; otherwise, the App Store server times out and the request fails.

## See Also

- [Responding to real-time retention messaging requests](responding-to-realtime-retention-messaging-requests.md)
  Select retention messages for customers in real time by responding to requests on your Get Retention Message endpoint.
- [object RealtimeRequestBody](realtimerequestbody.md)
  The request body the App Store server sends to your Get Retention Message endpoint.
- [object DecodedRealtimeRequestBody](decodedrealtimerequestbody.md)
  The decoded request body the App Store sends to your server to request a real-time retention message.
- [object RealtimeResponseBody](realtimeresponsebody.md)
  A response you provide to choose, in real time, a retention message the system displays to the customer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/setting-up-retention-messaging-endpoint)*