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

- A text-based message
- A text-based message with an image
- A switch-plan message, which contains text and a suggested subscription the customer may choose to switch to
- A promotional-offer message, which contains text and a promotional offer to continue service at a discounted price, either at the same or a different tier of service

The system displays the retention message to the customer after they tap Cancel Subscription on a subscription details page. The system displays a Confirm Cancellation page where the customer can continue to cancel by tapping Cancel Subscription. They can also tap Don’t Cancel, or, depending on the retention message, they can choose to redeem an offer or subscribe to a subscription you suggest.

The following two examples show a text-based message and a text-based message with an image on the cancel confirmation screen:

The following two examples show a switch-plan message and a promotional-offer message on the cancel confirmation screen:

You use the API to select retention messages for customers in two ways:

- By configuring default messages, which are text-based messages, with or without an image, that apply to specific products and locales.
- By choosing a retention message in real time, when you respond to a server-to-server call from the App Store server. You also configure default messages, which the system uses as a fallback if real-time calls fail for any reason.

##### Upload Images and Messages

All retention messages start with text that you upload, and optional images. For more information, see [`Upload Image`](upload-image.md) and [`Upload Message`](upload-message.md).

Don’t upload content that is misleading or inaccurate.

##### Configure Default Retention Messages

The simplest way to use this API is to configure default messages. Start by uploading images and messages. Then, specify the messages to use as default messages. For more information, see [`Setting up retention messages`](setting-up-retention-messages.md).

The default messaging option supports only text-based messages with or without an image. For retention messages that include offers, use the real-time messaging flow.

##### Provide Real Time Messages Including Offers

The real-time messaging flow calls your server when an active subscriber views a subscription details page with a Cancel button. For example, customers might consider canceling on the Apple Account > Subscriptions page, or when viewing the subscription details page on the App Store.

The real-time call informs you about the subscription, including the original transaction ID, and the customer’s locale. You respond by selecting an appropriate preconfigured message for the system to display. You can choose from all the retention message types, including those with switch-plan or promotional offers.

Follow these steps to implement the real-time flow:

1. Upload and prepare your retention messages. For more information, see [`Setting up retention messages`](setting-up-retention-messages.md).
2. Configure a default retention message for every product in each locale. The system requires the default messages to use as a fallback if a real-time call to your server fails for any reason. For more information, see [`Configure Default Message`](configure-default-message.md).
3. Implement the `Get Retention Message` endpoint on your server. For more information, see [`Setting up your Get Retention Message endpoint`](setting-up-retention-messaging-endpoint.md).
4. Respond to App Store requests by selecting a retention message to display in real-time. For more information, see [`Responding to real-time retention messaging requests`](responding-to-realtime-retention-messaging-requests.md).

##### System Requirements

Retention messages are visible only to devices running iOS 15.1 or later, iPadOS 15.1 or later, visionOS 1 or later, or macOS 14 or later.

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
  Upload an image to use for retention messaging.
- [Delete Image](delete-image.md)
  Delete a previously uploaded image.
- [Get Image List](get-image-list.md)
  Get the image identifier and state for all uploaded images.
- [object GetImageListResponse](getimagelistresponse.md)
  A response that contains status information for all images.
- [object GetImageListResponseItem](getimagelistresponseitem.md)
  An image identifier and state information for an image.
### Message configuration
- [Upload Message](upload-message.md)
  Upload a message to use for retention messaging.
- [Delete Message](delete-message.md)
  Delete a previously uploaded message.
- [Get Message List](get-message-list.md)
  Get the message identifier and state of all uploaded messages.
- [object UploadMessageRequestBody](uploadmessagerequestbody.md)
  The request body for uploading a message, which includes the message text and an optional image reference.
- [object UploadMessageImage](uploadmessageimage.md)
  The definition of an image with its alternative text.
- [object GetMessageListResponse](getmessagelistresponse.md)
  A response that contains status information for all messages.
- [object GetMessageListResponseItem](getmessagelistresponseitem.md)
  A message identifier and status information for a message.
### Default message configuration
- [Configure Default Message](configure-default-message.md)
  Configure a default message for a specific product in a specific locale.
- [Delete Default Message](delete-default-message.md)
  Delete a default message for a product in a locale.
- [object DefaultConfigurationRequest](defaultconfigurationrequest.md)
  The request body that contains the default configuration information.
### Real-time retention messaging
- [Setting up your Get Retention Message endpoint](setting-up-retention-messaging-endpoint.md)
  Choose retention messages for customers in real time by implementing an endpoint on your server that responds to requests from the App Store server.
- [Responding to real-time retention messaging requests](responding-to-realtime-retention-messaging-requests.md)
  Select retention messages for customers in real time by responding to requests on your Get Retention Message endpoint.
- [object RealtimeRequestBody](realtimerequestbody.md)
  The request body the App Store server sends to your Get Retention Message endpoint.
- [object DecodedRealtimeRequestBody](decodedrealtimerequestbody.md)
  The decoded request body the App Store sends to your server to request a real-time retention message.
- [object RealtimeResponseBody](realtimeresponsebody.md)
  A response you provide to choose, in real time, a retention message the system displays to the customer.
### Server performance testing
- [Initiate Performance Test](initiate-performance-test.md)
  Initiates a performance test
- [Get Performance Test Results](get-performance-test-results.md)
  Gets the results of the performance test for the specified identifier.
### Data types
- [Data types](data-types.md)
  Refer to these data types for request and response payloads.
### Error information
- [Error codes](error-codes.md)
  Understand the error codes that Retention Messaging API responses return.


---

*[View on Apple Developer](https://developer.apple.com/documentation/RetentionMessaging)*