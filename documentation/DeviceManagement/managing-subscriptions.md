# Managing subscriptions

**Framework**: Device Management

Administer auto-renewable subscription seats for your organization.

#### Overview

The Asset Management API provides dedicated endpoints for managing auto-renewable subscriptions separately from standard app and book assets. Unlike traditional assets that have a single pool of assigned and available seats, subscriptions maintain seat counts broken down by renewal state. Each seat is either *renewing*, meaning it automatically renews at the end of its current billing period, or *expiring*, meaning it doesn’t renew and becomes inactive when the current billing period ends.

This distinction matters when planning seat allocation. Renewing seats represent ongoing commitments, while expiring seats represent capacity that your organization loses at the end of the current billing period. The API surfaces these states across all subscription endpoints, from seat inventory queries to individual assignment records.

Subscriptions are identified by two values: a `parentAdamId` that refers to the parent app in the store, and an `adamId` that identifies the specific subscription product.

> ❗ **Important**:  Before content managers can purchase subscriptions into your managed organizational unit, your device management service must declare that it supports subscription management. Send a POST request to `/v2/subscriptions/enable` for each token you manage. Until you do, subscriptions aren’t available for purchase into the organizational unit that the token represents. You can disable subscription management later, but only while the organizational unit has no subscriptions.

#### Declare Subscription Management Support

Subscription management support is a declaration you make per token, and it applies to the organizational unit that the token represents. Use these two endpoints to state explicitly whether your device management service supports subscriptions for an organizational unit. Neither request takes a body, and both report the resulting state in `subscriptionManagement`.

Send a POST request to `/v2/subscriptions/enable` to declare that your device management service supports subscription management. Content managers can then purchase subscriptions into that organizational unit.

```javascript
curl --location --request POST 'https://vpp.itunes.apple.com/mdm/v2/subscriptions/enable' \
--header 'Authorization: Bearer {sToken}'
```

The code above results in a response like the following:

```json
{
  "mdmInfo": null,
  "subscriptionManagement": true,
  "tokenExpirationDate": "2030-11-08T22:33:22+0000",
  "uId": "2049025000431439"
}
```

> **Note**:  You can reverse an enable declaration by disabling the organizational unit, but only while it has no subscriptions. After content managers purchase subscriptions into it, disabling fails until no subscriptions remain.

Send a POST request to `/v2/subscriptions/disable` to declare that your device management service doesn’t support subscriptions for an organizational unit. Apple School Manager and Apple Business Manager use this declaration to indicate to content managers that the organizational unit doesn’t support subscriptions, rather than leaving its support status unstated.

```javascript
curl --location --request POST 'https://vpp.itunes.apple.com/mdm/v2/subscriptions/disable' \
--header 'Authorization: Bearer {sToken}'
```

The code above results in a response like the following:

```json
{
  "mdmInfo": null,
  "subscriptionManagement": false,
  "tokenExpirationDate": "2030-11-08T22:33:22+0000",
  "uId": "2049025000431439"
}
```

Disabling is a positive declaration that the organizational unit doesn’t support subscriptions. It also reverses an earlier enable request, but only while the organizational unit has no subscriptions. If any subscriptions exist there, the request fails with error `9818` (`Subscriptions exist for the organizational unit, so subscription management can't be disabled.`). For more information, see [`Handling error responses`](handling-error-responses.md).

The `subscriptionManagement` field reports the state that the server recorded for the token. Confirm that it matches the state you intended before you rely on the other subscription endpoints.

#### Retrieve Subscription Seat Counts

Send a GET request to `/v2/subscriptions` to retrieve the subscriptions your organization manages. Filter results by `parentAdamId` or `adamId`, or omit both to retrieve all subscriptions. The response breaks down seat counts by renewal state for both assigned and available seats.

```javascript
curl --location --request GET 'https://vpp.itunes.apple.com/mdm/v2/subscriptions?parentAdamId=54321' \
--header 'Authorization: Bearer {sToken}'
```

The code above results in a response like the following:

```json
{
  "subscriptions": [
    {
      "parentAdamId": 54321,
      "adamId": 12345,
      "status": "ACTIVE",
      "periodEndDate": "2027-01-15",
      "counts": {
        "assigned": {
          "renewing": 80,
          "expiring": 20
        },
        "available": {
          "renewing": 15,
          "expiring": 5
        },
        "total": {
          "renewing": 100,
          "expiring": 20
        }
      }
    }
  ],
  "nextCursor": "NjY5MjY0ODEtZTA4ZC00MmRhLTkxYjItMzdmMDI1MTVkYjQy",
  "uId": "2049025000431439",
  "tokenExpirationDate": "2030-11-08T22:33:22+0000",
  "versionId": "3b4b51d3-07f0-5711-bf45-b48df0fec669"
}
```

Each subscription includes a `status` field that reflects the current state of the subscription license:

| Value | Description |
| --- | --- |
| `ACTIVE` | The subscription is active and seats can be used and assigned. |
| `INACTIVE` | The subscription is no longer active. |
| `PAUSED` | The subscription is temporarily paused. |

The `periodEndDate` field reports the end date of the subscription’s current billing period in ISO-8601 calendar date format (`YYYY-MM-DD`). Renewing assignments roll into a new billing period on this date; expiring assignments and seats end on this date. Use this date to surface renewal reminders or upcoming capacity changes to administrators.

The `assigned` object shows how many seats currently have user assignments, broken down by the assignment’s renewal state — not the underlying license state. The `available` object shows how many seats remain unassigned. The `total` object shows the actual seat inventory your organization owns, regardless of how seats are assigned. Within each, the `renewing` count represents seats that auto-renew and the `expiring` count represents seats that don’t.

The `assigned` and `available` counts reflect assignment state, and `total` reflects license ownership. A renewing seat assigned with `renewing` set to `false` appears as `assigned.expiring`, but the underlying license remains in `total.renewing`. Use `total` for capacity planning and `assigned` for utilization tracking. The invariant is: `assigned.renewing + assigned.expiring + available.renewing + available.expiring = total.renewing + total.expiring`.

The `assigned` field appears only in the synchronous `GET /v2/subscriptions` response. `SUBSCRIPTION_COUNT` notifications include only `available` and `total`. To track assigned counts, query the `GET /v2/subscriptions` endpoint directly rather than deriving them from notifications.

This endpoint uses cursor-based pagination. Pass the `nextCursor` value as the `cursor` query parameter in subsequent requests until `nextCursor` is absent.

The response can include subscriptions that previously had seats but no longer do. These entries appear with all counts set to zero. Your device management service should handle zero-count subscriptions gracefully rather than treating them as errors.

#### Query Individual Subscription Assignments

Send a GET request to `/v2/subscriptions/assignments` to retrieve per-user assignment details. Filter results by `parentAdamId`, `adamId`, or `clientUserId`. Each assignment record includes a `renewing` Boolean value that reflects the renewal state of the assignment.

```javascript
curl --location --request GET 'https://vpp.itunes.apple.com/mdm/v2/subscriptions/assignments?adamId=12345' \
--header 'Authorization: Bearer {sToken}'
```

The code above results in a response like the following:

```json
{
  "assignments": [
    {
      "adamId": 12345,
      "clientUserId": "user-1",
      "renewing": true
    },
    {
      "adamId": 12345,
      "clientUserId": "user-2",
      "renewing": false
    }
  ],
  "nextCursor": "NjY5MjY0ODEtZTA4ZC00MmRhLTkxYjItMzdmMDI1MTVkYjQy",
  "uId": "2049025000431439",
  "tokenExpirationDate": "2030-11-08T22:33:22+0000",
  "versionId": "ab290ee7-02c1-5ba7-aa0a-652bd6e595bc"
}
```

This endpoint uses cursor-based pagination. Pass the `nextCursor` value as the `cursor` query parameter in subsequent requests until `nextCursor` is absent.

A `renewing` value of `true` means the user’s assignment auto-renews at the end of the current billing period. A value of `false` means the assignment expires at the end of its current billing period. Use this information to identify which assignments need attention before they lapse.

#### Plan Seat Allocation Based on Renewal State

The renewal state of a seat determines what happens to it when a subscription period ends or when your device management service removes an assignment.

When your device management service client disassociates a user from a *renewing* seat, that seat returns to the available pool as a renewing seat. The organization retains the seat, and your device management service can create an assignment for another user. The total number of seats the organization owns remains unchanged.

When a user holds an assignment on an *expiring* seat and the billing period ends, that seat disappears from the pool entirely. The seat doesn’t renew, so it doesn’t return to the available pool. The organization’s total seat count decreases by one.

Consider an organization with 100 subscription seats — 80 assigned as renewing, 15 assigned as expiring, and 5 available.

```json
{
  "counts": {
    "assigned": { "renewing": 80, "expiring": 15 },
    "available": { "renewing": 5, "expiring": 0 },
    "total": { "renewing": 100, "expiring": 0 }
  }
}
```

The `total` confirms that all 100 seats are renewing licenses, even though 15 are assigned in expiring mode. If your device management service disassociates 10 users from renewing seats, those 10 seats move back to the available renewing pool. The organization still has 100 total seats, now with 70 assigned renewing, 15 assigned expiring, and 15 available renewing.

When the billing period ends for the 15 expiring assignments, those assignments end and the underlying seats return to the available pool as renewing seats — because `total.renewing` remains 100. The organization retains all 100 seats.

Compare this to a scenario where the organization has marked seats for expiration (`total.expiring > 0`). When those billing periods end, the seats disappear from the pool entirely and `total.expiring` decreases. Surface `total.expiring` in your device management service so administrators can see how many seats the organization will lose at the end of the billing period.

Expose the *available* `expiring` counts in your device management service so administrators can monitor capacity that they’ll lose at the end of the billing period. Administrators can then choose to create expiring assignments from those seats before the period ends, or purchase additional seats to compensate.

#### Check Request Size Limits

The size limits for a [`ManageSubscriptionsRequest`](managesubscriptionsrequest.md) are dynamic and can change without notice, so you should sync these every 5 minutes. These limits are in [`ServiceConfigResponse.Limits`](serviceconfigresponse/limits-data.dictionary.md).

The following keys are specific to [`ManageSubscriptionsRequest`](managesubscriptionsrequest.md):

- `maxSubscriptions` - The maximum number of unique subscriptions in a manage request
- `maxSubscriptionClientUserIds` - The maximum number of unique user identifiers in a manage request

A request that exceeds either limit fails with error `9816` (`This request exceeds the maximum subscriptions limit. Change the request to stay within the specified limit.`). For more information, see [`Handling error responses`](handling-error-responses.md).

#### Associate Subscriptions with Users

To create assignments for subscription seats, send a POST request to `/v2/subscriptions/associate` with the subscription Adam IDs, client user IDs, and the desired renewal state. Set the `renewing` field to `true` to assign renewing seats to the specified users.

```javascript
curl --location --request POST 'https://vpp.itunes.apple.com/mdm/v2/subscriptions/associate' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {sToken}' \
--data-raw '{
    "adamIds": [12345],
    "clientUserIds": ["user-1", "user-2"],
    "renewing": true
}'
```

The server processes this request asynchronously and returns an `eventId`. Use the Events Status endpoint at `GET /v2/status` with that `eventId` to track the operation’s progress.

##### Assign Seats in an Expiring State

Set the `renewing` field to `false` to create assignments using expiring seats. The user receives access to the subscription for the current billing period, but the seat expires at the end of that period without renewal. This is useful when you want to provide temporary access or when you plan to reassign a seat after the current period ends.

```json
{
  "adamIds": [12345],
  "clientUserIds": ["user-3"],
  "renewing": false
}
```

An expiring seat with an assignment still counts toward your organization’s assigned seat total until the period ends. You can check the balance between renewing and expiring seats at any time through the Get Subscriptions endpoint, where the `counts` object breaks down both `assigned` and `available` totals by renewal state.

#### Disassociate Subscriptions From Users

To remove assignments, send a POST request to `/v2/subscriptions/disassociate`. The request supports a `deferred` field that controls when the disassociation takes effect. When `deferred` is `true`, the assignment remains active for the user until the end of the current billing period rather than being removed immediately.

```javascript
curl --location --request POST 'https://vpp.itunes.apple.com/mdm/v2/subscriptions/disassociate' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {sToken}' \
--data-raw '{
    "adamIds": [12345],
    "clientUserIds": ["user-1"],
    "deferred": true
}'
```

When `deferred` is `false` or omitted, the disassociation takes effect as soon as the server processes the request. Use deferred disassociation to avoid disrupting users in the middle of a billing period. The server processes this request asynchronously and returns an `eventId`. Check the operation’s status at `GET /v2/status` using that `eventId`.

#### Retrieve Subscription Administrators

The subscription administrator endpoints let your device management service control which users have administrative access to specific subscriptions. This may be required for some developers’ intended app experiences.

Each administrator record includes the `adamId` of the subscription they administer, a `clientUserId` identifying the administrator, and an `idHash` for the user. When you include user state information, the response also contains a `userStatus` field that reflects the administrator’s current association state.

Send a GET request to `/v2/subscriptions/admins` to retrieve the administrators for subscriptions your organization manages. Filter results by one or more `adamId` values to see administrators for specific subscriptions. Set the `includeUserState` query parameter to `true` to include each administrator’s user status in the response.

```javascript
curl --location --request GET 'https://vpp.itunes.apple.com/mdm/v2/subscriptions/admins?adamId=12345&includeUserState=true' \
--header 'Authorization: Bearer {sToken}'
```

The code above results in a response like the following:

```json
{
  "admins": [
    {
      "adamId": 12345,
      "clientUserId": "vpp-user",
      "idHash": "rRVS8rlBrJjRqYwL8aNGDJG2CbU=",
      "userStatus": "Associated"
    }
  ],
  "nextCursor": "NjY5MjY0ODEtZTA4ZC00MmRhLTkxYjItMzdmMDI1MTVkYjQy",
  "uId": "2049025000431439",
  "tokenExpirationDate": "2030-11-08T22:33:22+0000",
  "versionId": "f5897284-ed94-510f-8914-3b88c9c67799"
}
```

This endpoint uses cursor-based pagination. Pass the `nextCursor` value as the `cursor` query parameter in subsequent requests until `nextCursor` is absent.

#### Add Subscription Administrators

Send a POST request to `/v2/subscriptions/admins/add` to designate users as administrators for specific subscriptions. The request body requires an `adamIds` array of subscription identifiers and a `clientUserIds` array of user identifiers.

```javascript
curl --location --request POST 'https://vpp.itunes.apple.com/mdm/v2/subscriptions/admins/add' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {sToken}' \
--data-raw '{
    "adamIds": [12345],
    "clientUserIds": ["vpp-user"]
}'
```

The server processes this request synchronously and returns a confirmation response.

```json
{
  "uId": "2049025000431439",
  "tokenExpirationDate": "2030-11-08T22:33:22+0000",
  "versionId": "f5897284-ed94-510f-8914-3b88c9c67799"
}
```

#### Remove Subscription Administrators

Send a POST request to `/v2/subscriptions/admins/remove` to revoke administrator access from users for specific subscriptions. The request body requires an `adamIds` array of subscription identifiers and a `clientUserIds` array of user identifiers.

```javascript
curl --location --request POST 'https://vpp.itunes.apple.com/mdm/v2/subscriptions/admins/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {sToken}' \
--data-raw '{
    "adamIds": [12345],
    "clientUserIds": ["vpp-user"]
}'
```

The server processes this request synchronously and returns a confirmation response.

```json
{
  "uId": "2049025000431439",
  "tokenExpirationDate": "2030-11-08T22:33:22+0000",
  "versionId": "f5897284-ed94-510f-8914-3b88c9c67799"
}
```

## See Also

- [Managing assets](managing-assets.md)
  Assign and revoke app and book licenses across your organization.
- [Managing users](managing-users.md)
  Register and manage users for your organization’s managed organizational unit.
- [Setting up and assigning content](setting-up-and-assigning-content.md)
  Distribute purchased licenses to managed users through your device management service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/managing-subscriptions)*