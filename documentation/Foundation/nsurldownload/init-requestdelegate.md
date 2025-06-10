# init(request:delegate:)

**Framework**: Foundation  
**Kind**: init

Returns an initialized URL download for a URL request and begins to download the data for the request.

**Availability**:
- macOS 10.3+

## Declaration

```swift
init(request: URLRequest, delegate: (any NSURLDownloadDelegate)?)
```

#### Return Value

An initialized NSURLDownload object for `request`.

## Parameters

- `request`: The URL request to download. The   object is deep-copied as part of the initialization process. Changes made to   after this method returns do not affect the request that is used for the loading process.
- `delegate`: The   class maintains a strong reference to this delegate object.

## See Also

- [URL Loading System](url-loading-system.md)
  Interact with URLs and communicate with servers using standard Internet protocols.
- [func setDestination(String, allowOverwrite: Bool)](nsurldownload/setdestination(_:allowoverwrite:).md)
  Sets the destination path of the downloaded file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurldownload/init(request:delegate:))*