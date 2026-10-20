# contentInformationRequest

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, nullable) AVAssetResourceLoadingContentInformationRequest * contentInformationRequest;
```

#### Discussion

An instance of [`AVAssetResourceLoadingContentInformationRequest`](../avassetresourceloadingcontentinformationrequest.md) that you populate with information about the resource. The value of this property is `nil` if no such information is being requested.

## See Also

### Accessing the request data
- [var request: URLRequest](./request.md)
  The URL request object for the resource.
- [var requestor: AVAssetResourceLoadingRequestor](./requestor.md)
  The asset resource requestor that made the request.
- [var dataRequest: AVAssetResourceLoadingDataRequest?](./datarequest.md)
  The range of requested resource data.
- [var redirect: URLRequest?](./redirect.md)
  An URL request instance if the loading request was redirected.
- [func streamingContentKeyRequestData(forApp: Data, contentIdentifier: Data, options: [String : Any]?) throws -> Data](./streamingcontentkeyrequestdata%28forapp,contentidentifier,options%29.md)
  Obtains key request data for a specific combination of application and content.
- [func persistentContentKey(fromKeyVendorResponse: Data, options: [String : Any]?) throws -> Data](./persistentcontentkey%28fromkeyvendorresponse,options%29.md)
  Obtains a persistable content key from a context.
- [let AVAssetResourceLoadingRequestStreamingContentKeyRequestRequiresPersistentKey: String](../avassetresourceloadingrequeststreamingcontentkeyrequestrequirespersistentkey.md)
  Specifies whether the content key request requires a persistable key to be returned from the key vendor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/contentinformationrequest)*