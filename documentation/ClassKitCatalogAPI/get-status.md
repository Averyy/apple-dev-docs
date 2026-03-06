# Get Status

**Framework**: ClassKit Catalog API  
**Kind**: httpRequest

Fetch the status of an operation that you initiated earlier.

**Availability**:
- ClassKit 1.0+

#### Discussion

If the system can’t immediately complete a request, the ClassKit Catalog API may acknowledge that it received the request and respond with a HTTP response containing the status code `202 ACCEPTED`. In this case, the response contains a header with the name “Location”. The corresponding value is a URL that points to the [`Get Status`](get-status.md) endpoint, including a `statusId` as the last path parameter. The header item might look like this:

```http
Location: classkit-catalog.apple.com/v1/status/KGW7S5VLDDOQSYSE7DKGYBGXUU
```

Use this `statusID` to ask the server for a status update at a later time.

##### Example

**Request**:

```None
https://classkit-catalog.apple.com/v1/status/KGW7S5VLDDOQSYSE7DKGYBGXUU 
```

**Response**:

```json
{
  "statusId": "KGW7S5VLDDOQSYSE7DKGYBGXUU",
  "teamId": "2X6UPAGN5A",
  "state": "error",
  "statusCode": "400",
  "error": {
    "id": "KGW7S5VLDDOQSYSE7DKGYBGXUU",
    "code": "THUMBNAIL_NOT_REFERENCED",
    "message": "The thumbnail with 'thumbnailId': unreferenced_image.png is not referenced by any context."
  },
  "location": "classkit-catalog.apple.com/v1/status/KGW7S5VLDDOQSYSE7DKGYBGXUU"
}

```

## Endpoint

`GET https://classkit-catalog.apple.com/v1/status/{statusId}`

## Parameters

- `statusId` (string) *(required)*: The identifier of the operation for which you want to retrieve the status.

## See Also

- [object Status](status.md)
  The state of a request that the API previously accepted, but didn’t complete right away.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkitcatalogapi/get-status)*