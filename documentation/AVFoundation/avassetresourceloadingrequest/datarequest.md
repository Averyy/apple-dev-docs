# dataRequest

**Framework**: AVFoundation  
**Kind**: property

The range of requested resource data.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var dataRequest: AVAssetResourceLoadingDataRequest? { get }
```

#### Discussion

An instance of [`AVAssetResourceLoadingDataRequest`](avassetresourceloadingdatarequest.md) that indicates the range of resource data that’s being requested. The value of this property is `nil` if no data is being requested.

## See Also

- [var request: URLRequest](avassetresourceloadingrequest/request.md)
  The URL request object for the resource.
- [var requestor: AVAssetResourceLoadingRequestor](avassetresourceloadingrequest/requestor.md)
  The asset resource requestor that made the request.
- [var contentInformationRequest: AVAssetResourceLoadingContentInformationRequest?](avassetresourceloadingrequest/contentinformationrequest.md)
  The information for a requested resource.
- [var redirect: URLRequest?](avassetresourceloadingrequest/redirect.md)
  An URL request instance if the loading request was redirected.
- [func streamingContentKeyRequestData(forApp: Data, contentIdentifier: Data, options: [String : Any]?) throws -> Data](avassetresourceloadingrequest/streamingcontentkeyrequestdata(forapp:contentidentifier:options:).md)
  Obtains key request data for a specific combination of application and content.
- [func persistentContentKey(fromKeyVendorResponse: Data, options: [String : Any]?) throws -> Data](avassetresourceloadingrequest/persistentcontentkey(fromkeyvendorresponse:options:).md)
  Obtains a persistable content key from a context.
- [let AVAssetResourceLoadingRequestStreamingContentKeyRequestRequiresPersistentKey: String](avassetresourceloadingrequeststreamingcontentkeyrequestrequirespersistentkey.md)
  Specifies whether the content key request requires a persistable key to be returned from the key vendor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/datarequest)*