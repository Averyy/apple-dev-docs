# Get Subscriptions

**Framework**: Device Management  
**Kind**: httpRequest

Get the subscriptions that your organization manages.

## Mentions

- [Getting started with the management API](getting-started-with-the-management-api.md)

#### Discussion

##### Example Request and Response

**Request**:

```None
?parentAdamId=54321&adamId=12345
```

**Response**:

```json
{
    "subscriptions": [
        {
            "parentAdamId": 54321,
            "adamId": 12345,
            "counts": {
                "assigned": {
                    "renewing": 0,
                    "expiring": 0
                },
                "available": {
                    "renewing": 0,
                    "expiring": 0
                },
                "total": {
                    "renewing": 0,
                    "expiring": 0
                }
            }
        }
    ],
    "nextCursor": "NjY5MjY0ODEtZTA4ZC00MmRhLTkxYjItMzdmMDI1MTVkYjQy",
    "uId": "2049025000431439",
    "tokenExpirationDate": "2030-11-08T22:33:22+0000",
    "versionId": "7760f54d-fd4a-4bad-b768-bc1cbb28af9a"
}
```

## Topics

### Response
- [object GetSubscriptionsResponse](getsubscriptionsresponse.md)
  The response that contains the requested subscriptions.
- [object ErrorResponse](errorresponse.md)
  The response that contains the error that occurs.
### Content Metadata
- [Managing subscriptions](managing-subscriptions.md)
  Administer auto-renewable subscription seats for your organization.

## Endpoint

`GET https://vpp.itunes.apple.com/mdm/v2/subscriptions`

## Parameters

- `parentAdamId` ([int64]): The filter for subscriptions by parent Adam ID.
- `adamId` ([int64]): The filter for subscriptions by Adam ID.
- `cursor` (string): The cursor for pagination to fetch the next page of results.

## See Also

- [Enable Subscriptions](enable-subscriptions.md)
  Declare that your device management service supports subscription management.
- [Disable Subscriptions](disable-subscriptions.md)
  Declare that your device management service doesn’t support subscription management.
- [Get Subscription Assignments](get-subscription-assignments.md)
  Get the subscription assignments for users in your organization.
- [Associate Subscriptions](associate-subscriptions.md)
  Associate subscriptions with client user IDs.
- [Disassociate Subscriptions](disassociate-subscriptions.md)
  Disassociate subscriptions from client user IDs.
- [Get Subscription Administrators](get-subscription-administrators.md)
  Get the administrators for subscriptions that your organization manages.
- [Add Subscription Administrators](add-subscription-administrators.md)
  Add administrators for subscriptions.
- [Remove Subscription Administrators](remove-subscription-administrators.md)
  Remove administrators from subscriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/get-subscriptions)*