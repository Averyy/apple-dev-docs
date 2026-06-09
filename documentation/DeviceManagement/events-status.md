# Event Status

**Framework**: Device Management  
**Kind**: httpRequest

Retrieve the status of an asynchronous event.

**Availability**:
- VPP License Management 2.0+

## Mentions

- [Handling error responses](handling-error-responses.md)
- [Managing assets](managing-assets.md)
- [Managing users](managing-users.md)
- [Subscribing to notifications](subscribing-to-notifications.md)

#### Discussion

##### Example Request and Response

**Request**:

```None
?eventId=1905643d-1afb-4c2d-ad74-1b268e92c880
```

**Response**:

```json
{
    "eventStatus": "COMPLETE",
    "eventType": "ASSOCIATE",
    "numCompleted": 4000,
    "numRequested": 4000,
    "tokenExpirationDate": "2030-11-08T22:33:22+0000",
    "uId": "2049025000431439"
}
```

## Topics

### Response
- [object StatusResponse](statusresponse.md)
  Status of an asynchronous event, including event type, current status, completion counts, and any failure details.
- [object ErrorResponse](errorresponse.md)
  The response that contains the error that occurs.

## Endpoint

`GET https://vpp.itunes.apple.com/mdm/v2/status`

## Parameters

- `eventId` (string): The unique identifier for the asynchronous event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/events-status)*