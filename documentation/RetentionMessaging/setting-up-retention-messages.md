# Setting up retention messages

**Framework**: Retention Messaging API

Upload images and messages for retention messaging, configure default messages, and complete the setup for promotional-offer and switch-plan messages.

#### Overview

The Retention Messaging API uses images and text that you upload and configure in advance to display retention messages to your customers. There are four types of retention messages:

- A text-based message
- A text-based message with an image
- A switch-plan message, which contains text and a suggested subscription the customer may choose to switch to
- A promotional-offer message, which contains text and a promotional offer to continue service at a discounted price, either at the same or a different tier of service

There are two ways to use the Retention Messaging API. The simplest way is to set up default messages for the system to use automatically. The other way is to choose a retention message in real time when the App Store server calls your `Get Retention Message` endpoint. For the simplest implementation, follow the instructions to upload images and messages, and configure default messages. The system supports only text-based messages, with or without images, as default messages. Promotional-offer and switch-plan retention messages aren’t available as default messages.

To use this API to choose any retention message type in real time, implement the `Get Retention Message` endpoint on your server. For more information, see [`Setting up your Get Retention Message endpoint`](setting-up-retention-messaging-endpoint.md). To use promotional-offer and switch-plan messages, upload messages without images and follow the additional setup instructions below.

##### Upload Images and Messages

All retention message types include text. For text-based messages with images, upload the images first.

Follow these steps to upload messages:

1. Call [`Upload Image`](upload-image.md) to upload images. Images are optional. Use them only for text-based messages with images.
2. Call [`Upload Message`](upload-message.md) to upload messages. Messages have header text and body text. For text-based messages with images, include the [`UploadMessageImage`](uploadmessageimage.md) when you upload the message. Don’t include images for messages you plan to use for switch-plan and promotional-offer messaging.

> ❗ **Important**: Don’t upload content that is misleading or inaccurate.

The system automatically sends your uploaded images and messages to Apple to check. You can associate images with messages at any time; however, the system only displays images and messages to customers that are in an `APPROVED` state.

##### Retrieve Identifiers and States of Images and Messages

Apple checks the images and messages that you upload, and sets their states. Call [`Get Image List`](get-image-list.md) and [`Get Message List`](get-message-list.md) to get the identifier and current state of images and messages.

You can start using a message and image when its [`messageState`](messagestate.md) or [`imageState`](imagestate.md), respectively, is `APPROVED`. Use these messages when you configure default messages and in real-time responses to your `Get Retention Message` endpoint.

> 💡 **Tip**: Keep a record of the images and messages on your system, including their identifiers, their purpose, and their state.

##### Configure Default Messages

Call [`Configure Default Message`](configure-default-message.md) to set up default messages. Only text-based messages, with or without images, can be default messages. You can configure a default message for every auto-renewable subscription in every locale for your app.

The system uses a default message in the following cases:

- If you configure only default messages
- If the App Store server fails to receive a response from your `Get Retention Message` endpoint for any reason

##### Optionally Prepare to Respond in Real Time

To use promotional-offer or switch-plan messages, and to choose any retention message in real time, you need to implement the `Get Retention Message` endpoint. For more information, see [`Setting up your Get Retention Message endpoint`](setting-up-retention-messaging-endpoint.md) and [`Responding to real-time retention messaging requests`](responding-to-realtime-retention-messaging-requests.md).

When you respond in real time, you can best select a retention message that suits the customer and your business needs.

##### Prepare to Use Promotional Offer Retention Messages

A promotional-offer message includes text and a promotional offer that you configure in App Store Connect. When you respond with a promotional-offer message, your server signs the offer.

Complete the following setup:

1. Set up promotional offers in App Store Connect and get the offer identifier. For more information, see [`Set up promotional offers for auto-renewable subscriptions`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-promotional-offers-for-auto-renewable-subscriptions).
2. Call [`Upload Message`](upload-message.md) to upload the text for your promotional-offer message. Don’t include an image.

When you respond to your `Get Retention Message` endpoint in real time, provide the promotional-offer signature and message identifier in the [`promotionalOffer`](promotionaloffer.md) field of [`RealtimeResponseBody`](realtimeresponsebody.md). Use only messages that have an `APPROVED` message state.

For information about signing the promotional offer, see [`promotionalOffer`](promotionaloffer.md).

##### Prepare to Use Switch Plan Retention Messages

A switch-plan message includes text and a suggested auto-renewable subscription. The suggested subscription needs to be in the same subscription group as the current subscription. For more information about subscription groups, see [`Offer auto-renewable subscription`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-subscriptions/offer-auto-renewable-subscriptions).

To set up switch-plan messages:

1. Call [`Upload Message`](upload-message.md) to upload the text for your switch-plan message. Don’t include an image.
2. Be prepared to identify a suitable auto-renewable subscription in the same subscription group for a customer to switch to.

When you respond to your `Get Retention Message` endpoint in real time, provide the switch-plan message and the suggested product identifier in the [`alternateProduct`](alternateproduct.md) field of [`RealtimeResponseBody`](realtimeresponsebody.md). Use only messages that have an `APPROVED` message state.

## See Also

- [Identifying rate limits](identifying-rate-limits.md)
  Recognize the rate limits that apply to Retention Messaging API endpoints, and handle them in your code.
- [Retention Messaging API changelog](retention-messaging-changelog.md)
  Learn about new features and updates in the Retention Messaging API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/setting-up-retention-messages)*