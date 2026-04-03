# Setting up your Get Retention Message endpoint

**Framework**: Retention Messaging API

Choose retention messages for customers in real time by implementing an endpoint on your server that responds to requests from the App Store server.

#### Overview

To receive requests from the App Store so that you can provide retention messages in real time, complete the following:

1. On your server, implement a `Get Retention Message` endpoint to the specifications described below.
2. Configure your endpoint for the sandbox environment by calling the [`Configure Realtime URL`](configure-realtime-url.md) endpoint.
3. Call the [`Initiate Performance Test`](initiate-performance-test.md), which runs in the sandbox environment. Your server needs to pass the test before you can configure your endpoint for the production environment.
4. Configure your endpoint for the production environment by calling the [`Configure Realtime URL`](configure-realtime-url.md) endpoint.

After you set up the `Get Retention Message` endpoint, the App Store server delivers real-time requests when customers view a subscription detail page where they may choose to cancel the subscription. You respond to the request by choosing a retention message for the system to display to the customer. You set up the retention messages in advance. The system only displays messages that have an `APPROVED` state. If the message includes an image, the image also needs to have an `APPROVED` state.

Your server is responsible for parsing, interpreting, and responding to all server-to-server posts. For information about responding to requests, see [`Responding to real-time retention messaging requests`](responding-to-realtime-retention-messaging-requests.md).

##### Implement Your Endpoint

Implement this endpoint on your server to the following specifications:

**Endpoint reference name:** `Get Retention Message`

**URL:** `POST https://example.com/<your URL>`

You determine the HTTPS URL(s) on your server to receive the requests for the sandbox and production environments. Share your URLs with Apple by calling the [`Configure Realtime URL`](configure-realtime-url.md) endpoint.

**HTTP body:** [`RealtimeRequestBody`](realtimerequestbody.md)

The request body. For the decoded version, see [`DecodedRealtimeRequestBody`](decodedrealtimerequestbody.md).

**Response codes:** `200` - `OK`   [`RealtimeResponseBody`](realtimeresponsebody.md)
Your response body identifies the retention message to display to the customer.

If a request fails for any reason, the system displays a default retention message. If a default message isn’t available, the system doesn’t display a retention message. For more information about default messages, see [`Setting up retention messages`](setting-up-retention-messages.md).

##### Implement the Server Requirements

Set up secure communications with the App Store server by meeting the following requirements:

- Your domain must have a valid SSL certificate.
- Your endpoint must implement TLS 1.2.
- Your endpoint needs to respond within 700 ms in the production environment; otherwise, the App Store server times out and the request fails.

##### Configure Your Endpoint for Real Time Use

To configure your `Get Retention Message` endpoint with this API’s server, call the [`Configure Realtime URL`](configure-realtime-url.md) endpoint. Set up the endpoint in the sandbox environment first.

> **Note**: Your server must pass the performance test in the sandbox environment before you can configure your real-time endpoint for the production environment. For more information, including response-time requirements in the sandbox environment, see [`Initiate Performance Test`](initiate-performance-test.md).

To check the URL you configured, call the [`Get Realtime URL`](get-realtime-url.md) endpoint.

To remove your endpoint from real-time use, call the [`Delete Realtime URL`](delete-realtime-url.md) endpoint.

## See Also

- [Configure Realtime URL](configure-realtime-url.md)
  Configures the URL for your Get Retention Message endpoint in the sandbox and production environments.
- [Get Realtime URL](get-realtime-url.md)
  Gets the URL for real-time messages that points to your Get Retention Message endpoint, which you previously configured.
- [Delete Realtime URL](delete-realtime-url.md)
  Deletes the URL for your Get Retention Message endpoint, in the sandbox or production environments.
- [object RealtimeUrlRequest](realtimeurlrequest.md)
  The request body for configuring the URL of your Get Retention Message endpoint.
- [object RealtimeRequestBody](realtimerequestbody.md)
  The request body the App Store server sends to your Get Retention Message endpoint.
- [object RealtimeUrlResponse](realtimeurlresponse.md)
  The response body that contains the URL for your Get Retention Message endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/setting-up-retention-messaging-endpoint)*