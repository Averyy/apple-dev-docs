# request

**Framework**: AVFoundation  
**Kind**: property

The URL request object for the resource.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var request: URLRequest { get }
```

#### Discussion

Use the value in this property to identify the requested resource and to formulate an appropriate response object.

## See Also

- [var requestor: AVAssetResourceLoadingRequestor](avassetresourceloadingrequest/requestor.md)
  The asset resource requestor that made the request.
- [var contentInformationRequest: AVAssetResourceLoadingContentInformationRequest?](avassetresourceloadingrequest/contentinformationrequest.md)
  The information for a requested resource.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/request)*