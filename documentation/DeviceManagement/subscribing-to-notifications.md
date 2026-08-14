# Subscribing to notifications

**Framework**: Device Management

Monitor events for assets, assignments, and users in your organization.

#### Overview

Notifications make it easy to learn about changes to an organization’s assets, assignments, and users. Using notifications is the simplest way to keep track of the latest events for an organization, such as:

- Asset count events
- Asset management events
- User management events
- User-associated events

For information about subscribing to different notification types, see  [`ClientConfigRequest`](clientconfigrequest.md).

Each notification has these common fields:

| Response field | Description |
| --- | --- |
| `notificationId` | Each notification has a unique ID that you can use for deduping notifications that the server sends more than once. |
| `notificationType` | The type of notification. You can use this to determine how to deserialize the notification value. |
| `notification` | Contains the JSON object with the changed data. Each notification type has a uniquely structured notification JSON object. |
| `uId` | The ID of the organizational unit for the notification. |

Notifications resemble the following:

```json
{
    "notification": {...},
    "notificationId": "01654971-0d81-467a-9e62-bf8e15e8dabd",
    "notificationType": "ASSET_MANAGEMENT",
    "uId": "2049025000431439"
}
```

The server delivers notifications on a best-effort basis. The server attempts delivery up to three times over 1–5 minutes. An HTTP `2xx` response status from your device management service indicates a successful notification delivery.

There is a limit of 100 elements in the notification. Any request for more than 100 discrete tasks results in multiple notifications. For example, an assignment request for one `adamId` to 150 users results in at least two notifications.

If your device management service doesn’t receive a notification for an event within 5 minutes, check the event status using the [`Event Status`](events-status.md) endpoint with the `eventId` from the original request. While the returned `eventStatus` is `PENDING`, wait at least 30 seconds between subsequent status queries to avoid unnecessary load on the server. If the status remains `PENDING` after 10 minutes, retry the request.

Notifications require an HTTPS URL and an authentication token. The authentication token is in a [`bearer token format`](https://developer.apple.comhttps://tools.ietf.org/html/rfc6750). See the [`ClientConfigRequest`](clientconfigrequest.md) for more details about these parameters.

> ❗ **Important**:  The server sends a test notification of type `TEST_NOTIFICATION` when you configure notifications with [`Client Config`](client-config-4szk1.md). If delivery fails, the system rejects the configuration.

The test notification has the following format:

```json
{
    "notification": {},
    "notificationId": "792e327f-63ea-4658-9aec-f16f4327e3a8",
    "notificationType": "TEST_NOTIFICATION",
    "uId": "2049025000431439"
}
```

#### Update Asset Counts

Update total asset counts upon receiving an `ASSET_COUNT` notification type that the server sends when:

- A user buys an asset
- A user transfers an asset between organizational units
- A user refunds an asset

The notifications have the following format:

```json
{
    "notification": {
        "adamId": "408709785",
        "countDelta": -12,
        "pricingParam": "STDQ"
    },
    "notificationId": "4a7801be-53f0-42e1-9505-81c0d1dc9da3",
    "notificationType": "ASSET_COUNT",
    "uId": "2049025000431439"
}
```

The `adamId` and `pricingParam` pair represents the [`Asset`](asset.md) with the count that’s changing, and the `countDelta` represents the change amount. A positive `countDelta` indicates an increase; a negative value indicates a decrease.

#### Update Subscription Counts

Update subscription seat counts upon receiving a `SUBSCRIPTION_COUNT` notification type that the server sends when subscription inventory changes — for example, when a content manager purchases additional seats, when seats expire at the end of a billing period, or when renewing seats auto-renew.

> **Note**:  Subscription notifications represent `adamId` and `parentAdamId` as integers, and asset notifications represent `adamId` as a string. Match the type your notification endpoint expects for each family.

The notifications have the following format:

```json
{
    "notification": {
        "parentAdamId": 54321,
        "adamId": 12345,
        "counts": {
            "available": {
                "renewing": 15,
                "expiring": 5
            },
            "total": {
                "renewing": 100,
                "expiring": 20
            }
        }
    },
    "notificationId": "4a7801be-53f0-42e1-9505-81c0d1dc9da4",
    "notificationType": "SUBSCRIPTION_COUNT",
    "uId": "2049025000431439"
}
```

The notification uses a subset of the [`SubscriptionCounts`](subscriptioncounts.md) schema: the `counts` object contains only `available` and `total`. It omits `assigned`, which is only present in the synchronous `GET /v2/subscriptions` response. Use `total` to track actual seat ownership and `available` to track unassigned capacity.

#### Track Assignments

Track assignments upon receiving an `ASSET_MANAGEMENT` notification type that the server sends when it associates or disassociates an asset. The body of the notification contains a list of [`Assignment`](assignment.md) objects.

The assignment notifications for associations have the following format:

```json
{
    "notification": {
        "assignments": [
            {
                "adamId": "408709785",
                "pricingParam": "STDQ",
                "serialNumber": "97c42a74-c30e-4172-a65f-6e5a5ba3d477"
            },
            {
                "adamId": "408709785",
                "pricingParam": "STDQ",
                "serialNumber": "495622d3-76f1-4fd3-8647-3f0365159170"
            },
            {
                "adamId": "408709785",
                "pricingParam": "STDQ",
                "serialNumber": "eabcbb89-8213-4185-afb4-30cae931ea37"
            },
            ...
        ],
        "eventId": "87cbc650-16cc-4f9e-a833-e622f377a9f7",
        "result": "SUCCESS",
        "type": "ASSOCIATE"
    },
    "notificationId": "ba8bbb23-44c2-44f6-a928-eff6ba5ffac5",
    "notificationType": "ASSET_MANAGEMENT",
    "uId": "2049025000431439"
}
```

The assignment notifications for disassociations have the following format:

```json
{
    "notification": {
        "assignments": [
            {
                "adamId": "408709785",
                "clientUserId": "client-100",
                "pricingParam": "STDQ"
            }
        ],
        "eventId": "4bd7371e-6482-4933-8e97-c29f25b7f5f5",
        "result": "SUCCESS",
        "type": "DISASSOCIATE"
    },
    "notificationId": "545e1f6f-ca8b-4e6c-98fe-a7ac3ef63b29",
    "notificationType": "ASSET_MANAGEMENT",
    "uId": "2049025000431439"
}
```

The assignment notifications for revoke calls have the following format:

```json
{
    "notification": {
        "assignments": [
            {
                "adamId": "408709785",
                "clientUserId": "client-100",
                "pricingParam": "STDQ"
            },
            {
                "adamId": "329103948",
                "clientUserId": "client-100",
                "pricingParam": "STDQ"
            }

        ],
        "eventId": "7f2a9c14-3b8d-4e6a-b1c5-9d0e2f4a6b8c",
        "result": "SUCCESS",
        "type": "REVOKE"
    },
    "notificationId": "6a2f1e8b-7d4c-4a9e-b3f0-1c5d8e2a4b60",
    "notificationType": "ASSET_MANAGEMENT",
    "uId": "2049025000431439"
}

```

#### Track Subscription Assignments

Track subscription assignments upon receiving a `SUBSCRIPTION_MANAGEMENT` notification type that the server sends when it associates or disassociates a subscription. The body of the notification contains a list of [`ResponseSubscriptionAssignment`](responsesubscriptionassignment.md) objects, each with a `renewing` Boolean value that reflects the renewal state of the seat assigned to that user.

The subscription assignment notifications for associations have the following format:

```json
{
    "notification": {
        "assignments": [
            {
                "adamId": 12345,
                "clientUserId": "vpp-user",
                "renewing": true
            }
        ],
        "eventId": "c3f990d3-d8c5-41c6-8394-edb1f759a9d2",
        "result": "SUCCESS",
        "type": "ASSOCIATE"
    },
    "notificationId": "7b3c92a1-4e5f-4d8a-b6c7-9e1f2a3b4c5d",
    "notificationType": "SUBSCRIPTION_MANAGEMENT",
    "uId": "2049025000431439"
}
```

The subscription assignment notifications for disassociations have the following format:

```json
{
    "notification": {
        "assignments": [
            {
                "adamId": 12345,
                "clientUserId": "vpp-user",
                "renewing": true
            }
        ],
        "eventId": "d4ea01e4-e9d6-52d7-9405-f5c2fa6ab0e3",
        "result": "SUCCESS",
        "type": "DISASSOCIATE"
    },
    "notificationId": "8c4d03b2-5f6e-4e9b-a7d8-0f2e3b4c5d6e",
    "notificationType": "SUBSCRIPTION_MANAGEMENT",
    "uId": "2049025000431439"
}
```

When you set the `deferred` flag to `true` in a disassociation request, the notification arrives at the end of the current billing period rather than immediately. For more information about renewal state and deferred disassociation, see [`Managing subscriptions`](managing-subscriptions.md).

#### Track User Events

Track users upon receiving a `USER_MANAGEMENT` notification type that the server sends when:

- Creating a user
- Updating a user
- Retiring a user

The notifications for creating a user have the following format:

```json
{
    "notification": {
        "eventId": "e0def1f8-9158-4343-9c52-8dd32da50b9b",
        "result": "SUCCESS",
        "type": "CREATE",
        "users": [
            {
                "clientUserId": "client-100",
                "email": "client-100@apple.com",
                "inviteCode": "f551b37da07146628e8dcbe0111f0364",
                "status": "Registered"
            }
        ]
    },
    "notificationId": "4c0bbb9b-d5a6-4860-83ef-5cf362783c1e",
    "notificationType": "USER_MANAGEMENT",
    "uId": "2049025000431439"
}
```

The notifications for updating a user have the following format:

```json
{
    "notification": {
        "eventId": "e0def1f8-9158-4343-9c52-8dd32da50b9b",
        "result": "SUCCESS",
        "type": "UPDATE",
        "users": [
            {
                "clientUserId": "client-100",
                "email": "client-100@apple.com",
                "inviteCode": "f551b37da07146628e8dcbe0111f0364",
                "status": "Registered"
            }
        ]
    },
    "notificationId": "5d1ccc7c-e6b7-5971-94fa-6df473894c2f",
    "notificationType": "USER_MANAGEMENT",
    "uId": "2049025000431439"
}

```

The notifications for retiring a user have the following format:

```json
{
    "notification": {
        "eventId": "e0def1f8-9158-4343-9c52-8dd32da50b9b",
        "result": "SUCCESS",
        "type": "RETIRE",
        "users": [
            {
                "clientUserId": "client-100",
                "email": "client-100@apple.com",
                "inviteCode": "f551b37da07146628e8dcbe0111f0364",
                "status": "Retired"
            }
        ]
    },
    "notificationId": "6e2ddd8d-f7c8-6a82-a50b-7ef584a05d40",
    "notificationType": "USER_MANAGEMENT",
    "uId": "2049025000431439"
}

```

#### Track User Associations

Track users upon receiving a `USER_ASSOCIATED` notification type that the server sends when a user accepts an invitation.

The notifications have the following format:

```json
{
    "notification": {
        "associatedUsers": [
            {
                "clientUserId": "client-100",
                "email": "client-100@apple.com",
                "idHash": "leSKk3IaE2vk2KLmv2k3/200D3=",
                "inviteCode": "f551b37da07146628e8dcbe0111f0364",
                "status": "Associated"
            }
        ]
    },
    "notificationId": "90b83144-fb93-4837-9c52-0ae147bdc421",
    "notificationType": "USER_ASSOCIATED",
    "uId": "2049025000431439"
}
```

> ❗ **Important**:  Notifications are best-effort and should not be the sole mechanism for confirming request completion. Always pair notification handling with Events Status polling using the `eventId` from the original request.

## See Also

- [Using paginated endpoints](using-paginated-endpoints.md)
  Traverse large result sets with page-index and cursor-based pagination.
- [Handling error responses](handling-error-responses.md)
  Investigate and resolve service request errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/subscribing-to-notifications)*