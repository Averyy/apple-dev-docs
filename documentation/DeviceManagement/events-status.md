# Event Status

**Framework**: Device Management  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Retrieve the status of an asynchronous event.

**Availability**:
- VPP License Management 2.0+

## Mentions

- [Handling error responses](./handling-error-responses.md)
- [Managing assets](./managing-assets.md)
- [Managing users](./managing-users.md)
- [Subscribing to notifications](./subscribing-to-notifications.md)

## Discussion

### Example Request and Response

**Request**:

```
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
- [object StatusResponse](./statusresponse.md)
  The status of an asynchronous event.
- [object ErrorResponse](./errorresponse.md)
  The response that contains the error that occurs.

## Endpoint

`GET https://vpp.itunes.apple.com/mdm/v2/status`

## Parameters

### Query Parameters

- `eventId` (string): The unique identifier for the asynchronous event.

## Responses

- `200` OK (`StatusResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`): The provided token is invalid. It may either be missing or expired.
- `500` Internal Server Error (`ErrorResponse`, `application/json`): An internal server error occurred. Try again later.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/events-status)*