# persistentContentKey(fromKeyVendorResponse:options:)

**Framework**: AVFoundation  
**Kind**: method

Obtains a persistable content key from a context.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 9.0+

## Declaration

```swift
func persistentContentKey(fromKeyVendorResponse keyVendorResponse: Data, options: [String : Any]? = nil) throws -> Data
```

#### Return Value

The persistable content key.

#### Discussion

The data returned from this method may be used to immediately satisfy an [`AVAssetResourceLoadingDataRequest`](avassetresourceloadingdatarequest.md), as well as any subsequent requests for the same key URL. The value of [`contentType`](avassetresourceloadingcontentinformationrequest/contenttype.md) must be set to [`AVStreamingKeyDeliveryPersistentContentKeyType`](avstreamingkeydeliverypersistentcontentkeytype.md) when responding with data created with this method.

## Parameters

- `keyVendorResponse`: The response returned from the key vendor as a result of a request generated from  .
- `options`: Additional information necessary to obtain the key, or   if no additional information is required.

## See Also

- [var request: URLRequest](avassetresourceloadingrequest/request.md)
  The URL request object for the resource.
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
- [let AVAssetResourceLoadingRequestStreamingContentKeyRequestRequiresPersistentKey: String](avassetresourceloadingrequeststreamingcontentkeyrequestrequirespersistentkey.md)
  Specifies whether the content key request requires a persistable key to be returned from the key vendor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/persistentcontentkey(fromkeyvendorresponse:options:))*