# dataRequest

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, nullable) AVAssetResourceLoadingDataRequest * dataRequest;
```

## Discussion

An instance of [`AVAssetResourceLoadingDataRequest`](../avassetresourceloadingdatarequest.md) that indicates the range of resource data that’s being requested. The value of this property is `nil` if no data is being requested.

If the loading request’s [`contentInformationRequest`](./contentinformationrequest.md) isn’t `nil`, set that request’s properties before you respond to any data request.

## See Also

### Accessing the request data
- [var request: URLRequest](./request.md)
  The URL request object for the resource.
- [var requestor: AVAssetResourceLoadingRequestor](./requestor.md)
  The asset resource requestor that made the request.
- [var contentInformationRequest: AVAssetResourceLoadingContentInformationRequest?](./contentinformationrequest.md)
  The information for a requested resource.
- [var redirect: URLRequest?](./redirect.md)
  An URL request instance if the loading request was redirected.
- [func streamingContentKeyRequestData(forApp: Data, contentIdentifier: Data, options: [String : Any]?) throws -> Data](./streamingcontentkeyrequestdata%28forapp,contentidentifier,options%29.md)
  Obtains key request data for a specific combination of application and content.
- [func persistentContentKey(fromKeyVendorResponse: Data, options: [String : Any]?) throws -> Data](./persistentcontentkey%28fromkeyvendorresponse,options%29.md)
  Obtains a persistable content key from a context.
- [let AVAssetResourceLoadingRequestStreamingContentKeyRequestRequiresPersistentKey: String](../avassetresourceloadingrequeststreamingcontentkeyrequestrequirespersistentkey.md)
  Specifies whether the content key request requires a persistable key to be returned from the key vendor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/datarequest)*