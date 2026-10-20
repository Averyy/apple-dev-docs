# DownloadLinks

**Framework**: Account Data Transfer  
**Kind**: dictionary  
**Role**: Object

An object that contains URLs to download someone’s account data.

**Availability**:
- Account Data Transfer 1.0+

## Declaration

```
object DownloadLinks
```

#### Overview

The URLs you get from the `assetInfo` property are valid for 15 minutes after you receive them.

## Properties

- `assetInfo` ([string]): An array of URLs to which you make `GET` requests to download someone’s account data.
- `jobStatus` (string): The result of the download request.

  **Allowed Values**: `completed`, `request_not_found`, `in_progress`, `error`, `completed_with_error`, `cancelled`
- `status` (string): The result of the operation to request download links.

  **Allowed Values**: `success`

## See Also

### Downloads
- [Get one-time request download URLs](./get-one-time-request-download-urls.md)
  Get URLs to retrieve someone’s data.
- [Get recurring request download URLs](./get-recurring-request-download-urls.md)
  Get URLs to download a snapshot of someone’s data from a recurring series.
- [object DownloadError](./downloaderror.md)
  An object that describes an error the server encounters preparing download URLs for a request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accountdatatransfer/downloadlinks)*