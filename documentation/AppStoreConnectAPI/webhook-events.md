# Understanding webhook events

**Framework**: App Store Connect API

Learn the events that describe payloads and the notifications the system sends.

**Availability**:
- App Store Connect API 4.0+

#### Overview

Webhooks give you real-time, event-driven notifications via HTTP about payloads, so you can act on these events in an automated way. If enabled, you get notification from webhooks when one of the events you specify occurs. Use the webhook information to make subsequent calls to App Store Connect API to retrieve data.

Webhook events describe the payloads that the systems sends to your listening server based on your configurations when using [`Create a webhook configuration`](post-v1-webhooks.md). To read a list of possible webhook event types, see [`WebhookEventType`](webhookeventtype.md).

To learn more about setting up, testing, and parsing webhook configurations, see [`Configuring and parsing App Store Connect API webhook notifications`](configuring-webhook-notifications.md).

#### Learn Webhook Event Types

Here are three types of webhook event types; each includes different information, based on whether the systems notifies you about app status changes or beta-tester feedback crashes or screenshots.

## See Also

- [Configuring and parsing App Store Connect API webhook notifications](configuring-webhook-notifications.md)
  Manage the configuration, testing, and processing of App Store Connect API notifications for your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/webhook-events)*