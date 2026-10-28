# Get one-time request download URLs

**Framework**: App Data Transfer  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get URLs to retrieve someone’s data.

**Availability**:
- App Data Transfer 1.0+

## Overview

**Request**:

```
% curl -X GET \
  -H "Authorization: Bearer [ACCESS_TOKEN]" \
  -H "X-Apple-Transaction-Id: E3857B28-7FC4-41C8-AC54-08E121E26F59" \
  -H "Accept: application/json" \
  https://appdatatransfer.apple.com/api/transfer/appdata/fetch/11619695-72C0-4FFD-858A-1E152DCF0838
```

**Response**:

```
{
  "assetInfo": [
    "https://assets.example.com/1.zip",
    "https://assets.example.com/2.zip"
  ],
  "jobStatus": "completed",
  "status": "success",
}
```

## Endpoint

`GET https://appdatatransfer.apple.com/api/transfer/appdata/fetch/{requestId}`

## Parameters

### Path Parameters

- `requestId` (string) *(required)*: A UUID that identifies the one-time request.

## Responses

- `200` OK (`DownloadLinks`, `application/json`)
- `400` Bad Request (`DownloadError`, `application/json`)
- `401` Unauthorized
- `403` Forbidden
- `500` Internal Server Error

## See Also

### Downloads
- [Get recurring request download URLs](./get-recurring-request-download-urls.md)
  Get URLs to download a snapshot of someone’s data specific to your app from a recurring series.
- [object DownloadLinks](./downloadlinks.md)
  An object that contains URLs to download someone’s data specific to your app.
- [object DownloadError](./downloaderror.md)
  An object that describes an error the server encounters while preparing download URLs for a request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appdatatransfer/get-one-time-request-download-urls)*