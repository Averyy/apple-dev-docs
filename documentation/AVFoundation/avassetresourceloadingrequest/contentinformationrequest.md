# contentInformationRequest

**Framework**: AVFoundation  
**Kind**: property

The information for a requested resource.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var contentInformationRequest: AVAssetResourceLoadingContentInformationRequest? { get }
```

#### Discussion

An instance of [`AVAssetResourceLoadingContentInformationRequest`](avassetresourceloadingcontentinformationrequest.md) that you populate with information about the resource. The value of this property is `nil` if no such information is being requested.

## See Also

- [var request: URLRequest](avassetresourceloadingrequest/request.md)
  The URL request object for the resource.
- [var requestor: AVAssetResourceLoadingRequestor](avassetresourceloadingrequest/requestor.md)
  The asset resource requestor that made the request.
- [var dataRequest: AVAssetResourceLoadingDataRequest?](avassetresourceloadingrequest/datarequest.md)
  The range of requested resource data.
- [var redirect: URLRequest?](avassetresourceloadingrequest/redirect.md)
  An URL request instance if the loading request was redirected.
- [func streamingContentKeyRequestData(forApp: Data, contentIdentifier: Data, options: [String : Any]?) throws -> Data](avassetresourceloadingrequest/streamingcontentkeyrequestdata(forapp:contentidentifier:options:).md)
  Obtains key request data for a specific combination of application and content.
- [func persistentContentKey(fromKeyVendorResponse: Data, options: [String : Any]?) throws -> Data](avassetresourceloadingrequest/persistentcontentkey(fromkeyvendorresponse:options:).md)
  Obtains a persistable content key from a context.
- [let AVAssetResourceLoadingRequestStreamingContentKeyRequestRequiresPersistentKey: String](avassetresourceloadingrequeststreamingcontentkeyrequestrequirespersistentkey.md)
  Specifies whether the content key request requires a persistable key to be returned from the key vendor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/contentinformationrequest)*