# DownloadError

**Framework**: App Data Transfer  
**Kind**: dictionary

An object that describes an error the server encounters while preparing download URLs for a request.

**Availability**:
- App Data Transfer 1.0+

## Declaration

```swift
object DownloadError
```

#### Overview

The `statusMessage` field has one of these values:

- **`invalid_request_status`**: The download request isn’t complete and you need to request the download URLs again after `statusCheckDelay` seconds.
- **`request_not_found`**: The request ID you provided isn’t recognized.

## Properties

- `statusCheckDelay` (integer): The number of seconds to wait before re-requesting the status.
- `status` (string): The outcome of the operation.
- `statusMessage` (string): The reason the server encountered an error.

## See Also

- [Get one-time request download URLs](get-one-time-request-download-urls.md)
  Get URLs to retrieve someone’s data.
- [Get recurring request download URLs](get-recurring-request-download-urls.md)
  Get URLs to download a snapshot of someone’s data specific to your app from a recurring series.
- [object DownloadLinks](downloadlinks.md)
  An object that contains URLs to download someone’s data specific to your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appdatatransfer/downloaderror)*