# Get one-time request download URLs

**Framework**: Account Data Transfer  
**Kind**: httpRequest

Get URLs to retrieve someone’s data.

**Availability**:
- Account Data Transfer 1.0+

#### Overview

**Request**:

```None
% curl -X GET \
  -H "Authorization: Bearer [ACCESS_TOKEN]" \
  -H "X-Apple-Transaction-Id: E3857B28-7FC4-41C8-AC54-08E121E26F59" \
  -H "Accept: application/json" \
  https://accountdatatransfer.apple.com/api/transfer/accountdata/fetch/11619695-72C0-4FFD-858A-1E152DCF0838
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

`GET https://accountdatatransfer.apple.com/api/transfer/accountdata/fetch/{requestId}`

## Parameters

- `requestId` (string) *(required)*: A UUID that identifies the one-time request.

## See Also

- [Get recurring request download URLs](get-recurring-request-download-urls.md)
  Get URLs to download a snapshot of someone’s data from a recurring series.
- [object DownloadLinks](downloadlinks.md)
  An object that contains URLs to download someone’s account data.
- [object DownloadError](downloaderror.md)
  An object that describes an error the server encounters preparing download URLs for a request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accountdatatransfer/get-one-time-request-download-urls)*