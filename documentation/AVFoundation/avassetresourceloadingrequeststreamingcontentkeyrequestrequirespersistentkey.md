# AVAssetResourceLoadingRequestStreamingContentKeyRequestRequiresPersistentKey

**Framework**: AVFoundation  
**Kind**: var  
**Role**: Global Variable

Specifies whether the content key request requires a persistable key to be returned from the key vendor.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.14+ - Deprecated in 15.0
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Use -[AVPersistableContentKeyRequest persistableContentKeyFromKeyVendorResponse:options:error:] instead

## Declaration

```swift
let AVAssetResourceLoadingRequestStreamingContentKeyRequestRequiresPersistentKey: String
```

```c
extern NSString * const AVAssetResourceLoadingRequestStreamingContentKeyRequestRequiresPersistentKey;
```

## See Also

### Accessing the request data
- [var request: URLRequest](./avassetresourceloadingrequest/request.md)
  The URL request object for the resource.
- [var requestor: AVAssetResourceLoadingRequestor](./avassetresourceloadingrequest/requestor.md)
  The asset resource requestor that made the request.
- [var contentInformationRequest: AVAssetResourceLoadingContentInformationRequest?](./avassetresourceloadingrequest/contentinformationrequest.md)
  The information for a requested resource.
- [var dataRequest: AVAssetResourceLoadingDataRequest?](./avassetresourceloadingrequest/datarequest.md)
  The range of requested resource data.
- [var redirect: URLRequest?](./avassetresourceloadingrequest/redirect.md)
  An URL request instance if the loading request was redirected.
- [func streamingContentKeyRequestData(forApp: Data, contentIdentifier: Data, options: [String : Any]?) throws -> Data](./avassetresourceloadingrequest/streamingcontentkeyrequestdata%28forapp,contentidentifier,options%29.md)
  Obtains key request data for a specific combination of application and content.
- [func persistentContentKey(fromKeyVendorResponse: Data, options: [String : Any]?) throws -> Data](./avassetresourceloadingrequest/persistentcontentkey%28fromkeyvendorresponse,options%29.md)
  Obtains a persistable content key from a context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequeststreamingcontentkeyrequestrequirespersistentkey)*