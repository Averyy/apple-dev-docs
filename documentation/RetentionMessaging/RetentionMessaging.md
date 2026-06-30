# Retention Messaging API

**Framework**: Retention Messaging API  
**Kind**: module

Provide a reason for customers to stay subscribed with a preconfigured message that you can choose in real time, appropriate to the product and locale.

**Availability**:
- Retention Messaging API 1.0+

#### Overview

The Retention Messaging API is a server-to-server service that enables you to select which message the system displays to customers when they view a subscription details page and might cancel. You upload and configure messages in advance for products and locales.

> ❗ **Important**:  To learn more about this pre-release and express interest, see [`Request access to the Retention Messaging API`](https://developer.apple.comhttps://developer.apple.com/contact/request/retention-messaging-api/).

Your messages remind customers about the features or content they have access to with the subscription, or show them alternative offers. There are four types of retention messages:

- A text-based message that can include bullet points
- A text-based message that can include bullet points, with an image
- A switch-plan message, which contains text and a suggested subscription the customer may choose to switch to
- A promotional-offer message, which contains text and a promotional offer to continue service at a discounted price, either at the same or a different tier of service

The system displays the retention message to the customer after they tap Cancel Subscription on a subscription details page. The system displays a Confirm Cancellation page where the customer can continue to cancel by tapping Cancel Subscription. They can also tap Keep Subscription, or, depending on the retention message, they can choose to redeem an offer or subscribe to a subscription you suggest.

The following four examples show text-based messages on the Confirm Cancellation screen. The first row, from left to right, shows a text-based message without an image, and a text-based message with an image:

The next row shows two text-based messages that each include an image, a header above the image, and message text, with the second example also including bullet points:

The following two examples show a switch-plan message and a promotional-offer message on the Confirm Cancellation screen:

You use the API to select retention messages for customers in two ways:

- By configuring default messages, which are text-based messages, with or without an image or bullet points, that apply to specific products and locales.
- By choosing a retention message in real time, when you respond to a server-to-server call from the App Store server. You also configure default messages, which the system uses as a fallback if real-time calls fail for any reason.

The system doesn’t display a retention message for a product in any locale that lacks a default retention message.

##### Upload Images and Messages

All retention messages start with text that you upload, and optional images. For more information, see [`Upload Image`](upload-image.md) and [`Upload Message`](upload-message.md).

Don’t upload content that is misleading or inaccurate.

##### Configure Default Retention Messages

The simplest way to use this API is to configure default messages. Start by uploading images and messages. Then, specify the messages to use as default messages. For more information, see [`Setting up retention messages`](setting-up-retention-messages.md).

Default messages can display only text-based messages with or without images or bullet points. To provide retention messages that include offers, use the real-time messaging flow.

##### Provide Real Time Messages Including Offers

The real-time messaging flow calls your server when an active subscriber views a subscription details page with a Cancel button. For example, customers might consider canceling on the Apple Account > Subscriptions page, or when viewing the subscription details page on the App Store.

The real-time call informs you about the subscription, including the original transaction ID, and the customer’s locale. You respond by selecting an appropriate preconfigured message for the system to display. You can choose from all the retention message types, including those with switch-plan or promotional offers.

Follow these steps to implement the real-time flow:

1. Upload and prepare your retention messages. For more information, see [`Setting up retention messages`](setting-up-retention-messages.md).
2. Configure a default retention message for every product in each locale. The system requires the default messages to use as a fallback if a real-time call to your server fails for any reason. For more information, see [`Configure Default Message`](configure-default-message.md).
3. Implement the `Get Retention Message` endpoint on your server, and set it up in the sandbox environment by calling the [`Configure Realtime URL`](configure-realtime-url.md) endpoint. For more information, see [`Setting up your Get Retention Message endpoint`](setting-up-retention-messaging-endpoint.md).
4. To set up your endpoint in the production environment, call the [`Initiate Performance Test`](initiate-performance-test.md) and pass the test. Then call the [`Configure Realtime URL`](configure-realtime-url.md) endpoint to set up your production URL.
5. Respond to App Store requests by selecting a retention message to display in real time. For more information, see [`Responding to real-time retention messaging requests`](responding-to-realtime-retention-messaging-requests.md).

##### System Requirements

Retention messages are visible only to devices running iOS 15.1 or later, iPadOS 15.1 or later, visionOS 1 or later, or macOS 14 or later.

Before you can configure your real-time URL for the production environment, your server needs to pass the performance test. For more information, see [`Setting up your Get Retention Message endpoint`](setting-up-retention-messaging-endpoint.md).

## Topics

### Essentials
- [Setting up retention messages](setting-up-retention-messages.md)
  Upload images and messages for retention messaging, configure default messages, and complete the setup for promotional-offer and switch-plan messages.
- [Identifying rate limits](identifying-rate-limits.md)
  Recognize the rate limits that apply to Retention Messaging API endpoints, and handle them in your code.
- [Retention Messaging API changelog](retention-messaging-changelog.md)
  Learn about new features and updates in the Retention Messaging API.
### Image configuration
- [Upload Image](upload-image.md)
  Uploads an image to use for retention messaging.
- [Delete Image](delete-image.md)
  Deletes a previously uploaded image.
- [Get Image List](get-image-list.md)
  Gets the image identifier and state for all uploaded images.
- [object GetImageListResponse](getimagelistresponse.md)
  A response that contains status information for all images.
- [object GetImageListResponseItem](getimagelistresponseitem.md)
  An image identifier and state information for an image.
### Message configuration
- [Upload Message](upload-message.md)
  Uploads a message to use for retention messaging.
- [Delete Message](delete-message.md)
  Deletes a previously uploaded message.
- [Get Message List](get-message-list.md)
  Gets the message identifier and state of all uploaded messages.
- [object UploadMessageRequestBody](uploadmessagerequestbody.md)
  The request body for uploading a message, which includes the message text and an optional image reference and bullet points.
- [object UploadMessageImage](uploadmessageimage.md)
  The definition of an image with its alternative text.
- [object GetMessageListResponse](getmessagelistresponse.md)
  A response that contains status information for all messages.
- [object GetMessageListResponseItem](getmessagelistresponseitem.md)
  A message identifier and status information for a message.
### Default message configuration
- [Configure Default Message](configure-default-message.md)
  Configures a default message for a specific product in a specific locale.
- [Get Default Message](get-default-message.md)
  Gets the default message for a specific product in a specific locale, if it’s configured.
- [Delete Default Message](delete-default-message.md)
  Deletes a default message for a product in a locale.
- [object DefaultConfigurationRequest](defaultconfigurationrequest.md)
  The request body that contains the default configuration information.
- [object DefaultConfigurationResponse](defaultconfigurationresponse.md)
  The response body that contains the default configuration information.
### Real-time retention messaging setup
- [Setting up your Get Retention Message endpoint](setting-up-retention-messaging-endpoint.md)
  Choose retention messages for customers in real time by implementing an endpoint on your server that responds to requests from the App Store server.
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
### Real-time retention messaging responses
- [Responding to real-time retention messaging requests](responding-to-realtime-retention-messaging-requests.md)
  Select retention messages for customers in real time by responding to requests on your Get Retention Message endpoint.
- [object DecodedRealtimeRequestBody](decodedrealtimerequestbody.md)
  The decoded request body the App Store sends to your server to request a real-time retention message.
- [object RealtimeResponseBody](realtimeresponsebody.md)
  A response you provide to choose, in real time, a retention message the system displays to the customer.
### Server performance testing
- [Initiate Performance Test](initiate-performance-test.md)
  Initiates a performance test of your Get Retention Message endpoint in the sandbox environment.
- [Get Performance Test Results](get-performance-test-results.md)
  Gets the results of the performance test for the specified identifier.
- [object PerformanceTestRequest](performancetestrequest.md)
  The request object you provide for a performance test that contains an original transaction identifier.
- [object PerformanceTestResponse](performancetestresponse.md)
  The performance test response object.
- [object PerformanceTestResultResponse](performancetestresultresponse.md)
  An object the API returns that describes the performance test results.
### Data types
- [Data types](data-types.md)
  Refer to these data types for request and response payloads.
### Error information
- [Error codes](error-codes.md)
  Understand the error codes that Retention Messaging API responses return.


---

*[View on Apple Developer](https://developer.apple.com/documentation/RetentionMessaging)*