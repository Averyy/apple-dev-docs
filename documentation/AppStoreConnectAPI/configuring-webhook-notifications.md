# Configuring and parsing App Store Connect webhook notifications

**Framework**: App Store Connect API

Manage the configuration, testing, and processing of App Store Connect notifications for your app.

#### Overview

A notification webhook is an endpoint that you create on your server, which receives `HTTP POST` requests from App Store Connect. The `POST` requests describe important events about your app. Your app can have many webhooks.

##### Configure Your Webhook Notifications

To invoke your webhook, App Store Connect needs to know your server’s webhook endpoint URL. To set up your webhook endpoint the first time, provide the URL to the [`Create a webhook configuration`](post-v1-webhooks.md) endpoint:

```other
POST https://api.appstoreconnect.apple.com/v1/webhooks
```

with a payload like this:

```json

{
  "data": {
    "type": "webhooks",
    "attributes": {
      "enabled": true,
      "eventTypes": [
        "APP_STORE_VERSION_APP_VERSION_STATE_UPDATED"
      ],
      "name": "APP_STORE_VERSION_STATE_APP_NAME",
      "secret": "my_secret_string",
      "url": "https://example.com"
    },
    "relationships": {
      "app": {
        "data": {
          "type": "apps",
          "id": "string"
        }
      }
    }
  }
}

```

Any time you reconfigure your web server, use the [`Modify a webhook configuration`](patch-v1-webhooks-_id_.md) endpoint to update App Store Connect. The attributes you can modify are `enabled`, `name`, `url`, `secret`, and `eventTypes`.

##### Set Up Notification Authentication

Secure your webhook by verifying that a request to your endpoint comes from App Store Connect. The security protocol for webhooks is hash-based message authentication code (HMAC), which requires that you:

- Share a secret phrase with the request sender (App Store Connect).
- Verify that each POST to your endpoint has the HMAC header and validate it with your secret.

When you register your webhook URL with App Store Connect, define the secret phrase using the secret key in [`WebhookCreateRequest.Data.Attributes`](webhookcreaterequest/data-data.dictionary/attributes-data.dictionary.md). Choose a `String` value for `secret` that’s difficult to guess.

App Store Connect creates a hash signature using the secret and includes it in each `POST`. The signature resides in the payload header as `x-apple-signature`.

Verify the signature by implementing code in your webhook endpoint that:

- Creates a hash from the payload body using your secret token.
- Compares the hash to the one App Store Connect sends in the header to ensure they match.

For example, applying `HMAC-SHA256` to the secret “This is my secret” and payload body “Hello, World!” produces this hash:

```other
7f062172b01cb00b53ca068614674a3d982a34062a0f5d37687d5e3377e54657
```

This result verifies a `POST` is authentic — the sender knows the secret — if the payload contains the header:

```other
x-apple-signature:hmacsha256=7f062172b01cb00b53ca068614674a3d982a34062a0f5d37687d5e3377e54657
```

Use an implementation of HMAC `hex digest` to generate the hash. For more information, see [`GitHub’s Validating webhook deliveries`](https://developer.apple.comhttps://docs.github.com/en/webhooks/using-webhooks/validating-webhook-deliveries).

##### Review Your Configured Webhook Notifications

Use [`Read webhook information for an app`](get-v1-apps-_id_-webhooks.md) to view a list of webhooks for an app. The response includes the unique IDs and details of your webhook configurations. Use those unique IDs with [`Read webhook information`](get-v1-webhooks-_id_.md) to read details for a specific webhook.

##### Verify Your Server Is Receiving Notifications

Once you establish your webhook configuration and your listener, you can verify you are receiving notifications by using [`Test your webhook`](post-v1-webhookpings.md), with a payload like this, where the `id` for type `webhooks` is the unique identifier found in the response from [`Create a webhook configuration`](post-v1-webhooks.md) or  [`Read webhook information for an app`](get-v1-apps-_id_-webhooks.md):

```json
{
  "data": {
    "type": "webhookPings",
    "relationships": {
      "webhook": {
        "data": {
          "type": "webhooks",
          "id": "string"
        }
      }
    }
  }
}
```

##### Read a List of Past Deliveries

You can see past notification deliveries sent from App Store Connect to your server,  by using the [`Read the deliveries for a webhook`](get-v1-webhooks-_id_-deliveries.md) endpoint.

The response looks like this:

```json
{
  "data": [
    {
      "type": "webhookDeliveries",
      "id": "string",
      "attributes": {
        "createdDate": "1970-01-01T00:00:00.000Z",
        "deliveryState": "SUCCEEDED",
        "errorMessage": "string",
        "redelivery": false,
        "sentDate": "1970-01-01T00:00:00.000Z",
        "request": {
          "url": "https://example.com"
        },
        "response": {
          "httpStatusCode": 0,
          "body": "string"
        }
      },
      "relationships": {
        "event": {
          "data": {
            "type": "webhookEvents",
            "id": "string"
          }
        }
      },
      "links": {
        "self": ""
      }
    }
  ],
  "included": [
    {
      "type": "webhookEvents",
      "id": "string",
      "attributes": {
        "eventType": "APP_STORE_VERSION_APP_VERSION_STATE_UPDATED",
        "payload": "string",
        "ping": false,
        "createdDate": "1970-01-01T00:00:00.000Z"
      },
      "links": {
        "self": ""
      }
    }
  ],
  "links": {
    "self": "",
    "first": "",
    "next": ""
  },
  "meta": {
    "paging": {
      "total": 0,
      "limit": 0
    }
  }
}

```

#### Parse Webhook Notifications

When App Store Connect sends a notification to your webhook, it does so in the form of an HTTP POST. When you receive a notification, check its type to process it accordingly. The action you perform depends on the notification type. Each type has a specific dataset, or schema, composed of attributes that drive the different action you take. There are several types of webhook events; for more information about these events, see [`Understanding webhook events`](webhook-events.md).

##### Process a Specific Notification

This example uses the notification type `appStoreVersionAppVersionStateUpdated`. The attributes include the `version`, states, and a `timestamp` that shows when the state change. The payload includes a relationship to the `appStoreVersions id`. Use this information to read more about your app’s version using [`Read App Store Version Information`](get-v1-appstoreversions-_id_.md).

```json
{
  "data": {
    "type": "appStoreVersionAppVersionStateUpdated",
    "id": "7c813492-9516-4c79-903e-224effdd57ac",
    "version": 1,
    "attributes": {
      "newValue": "READY_FOR_REVIEW",
      "oldValue": "PREPARE_FOR_SUBMISSION",
      "timestamp": "2025-04-16T05:00:52.745Z"
    },
    "relationships": {
      "instance": {
        "data": {
          "type": "appStoreVersions",
          "id": "ad7e6298-2570-4ca6-b3cc-f81788e40bdc"
        }
      }
    }
  }
}
```

## See Also

- [Understanding webhook events](webhook-events.md)
  Learn the events that describe payloads and the notifications the system sends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/configuring-webhook-notifications)*