# Get recurring request download URLs

**Framework**: App Data Transfer  
**Kind**: httpRequest

Get URLs to download a snapshot of someone’s data specific to your app from a recurring series.

**Availability**:
- App Data Transfer 1.0+

#### Overview

**Request**:

```None
% curl -X GET \
  -H "Authorization: Bearer [ACCESS_TOKEN]" \
  -H "X-Apple-Transaction-Id: E3857B28-7FC4-41C8-AC54-08E121E26F59" \
  -H "Accept: application/json" \
  https://appdatatransfer.apple.com/api/transfer/appdata/fetch/EABD06C0-9210-47FF-83C4-318CF8520644/7BBBD45D-638B-4DB5-8B02-F23FDB15EDA7
```

**Response**:

```None
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

`GET https://appdatatransfer.apple.com/api/transfer/appdata/fetch/{parentRequestId}/{requestId}`

## Parameters

- `requestId` (string) *(required)*: A UUID that identifies the individual download request in the recurring sequence.
- `parentRequestId` (string) *(required)*: A UUID that identifies the recurring sequence of download requests.

## See Also

- [Get one-time request download URLs](get-one-time-request-download-urls.md)
  Get URLs to retrieve someone’s data.
- [object DownloadLinks](downloadlinks.md)
  An object that contains URLs to download someone’s data specific to your app.
- [object DownloadError](downloaderror.md)
  An object that describes an error the server encounters while preparing download URLs for a request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appdatatransfer/get-recurring-request-download-urls)*