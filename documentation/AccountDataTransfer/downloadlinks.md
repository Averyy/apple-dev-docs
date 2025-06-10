# DownloadLinks

**Framework**: Account Data Transfer  
**Kind**: dictionary

An object that contains URLs to download someone’s account data.

**Availability**:
- Account Data Transfer 1.0+

## Declaration

```swift
object DownloadLinks
```

#### Overview

The URLs you get from the `assetInfo` property are valid for 15 minutes after you receive them.

=======

- assetInfo: An array of URLs to which you make `GET` requests to download someone’s account data.

> **Note**: > **Note**: > **Note**: > **Note**: > **Note**: > **Note**: > **Note**: Main

- jobStatus: The result of the download request.
- status: The result of the operation to request download links.

## See Also

- [Get one-time request download URLs](get-one-time-request-download-urls.md)
  Get URLs to retrieve someone’s data.
- [Get recurring request download URLs](get-recurring-request-download-urls.md)
  Get URLs to download a snapshot of someone’s data from a recurring series.
- [object DownloadError](downloaderror.md)
  An object that describes an error the server encounters preparing download URLs for a request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accountdatatransfer/downloadlinks)*