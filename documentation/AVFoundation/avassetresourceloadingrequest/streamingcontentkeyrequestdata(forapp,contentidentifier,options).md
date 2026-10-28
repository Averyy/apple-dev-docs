# streamingContentKeyRequestData(forApp:contentIdentifier:options:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Obtains key request data for a specific combination of application and content.

**Availability**:
- iOS 7.0+ - Deprecated in 18.0
- iPadOS 7.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.9+ - Deprecated in 15.0
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Use -[AVContentKeyRequest makeStreamingContentKeyRequestDataForApp:contentIdentifier:options:completionHandler:] instead

## Declaration

```swift
func streamingContentKeyRequestData(forApp appIdentifier: Data, contentIdentifier: Data, options: [String : Any]? = nil) throws -> Data
```

```objc
- (NSData *) streamingContentKeyRequestDataForApp:(NSData *) appIdentifier contentIdentifier:(NSData *) contentIdentifier options:(NSDictionary<NSString *,id> *) options error:(NSError **) outError;
```

## Return Value

The key request data that must be transmitted to the key vendor to obtain the content key.

## Parameters

- `appIdentifier`: An opaque content identifier for the application. The value of this identifier depends on the particular system used to provide the decryption key.
- `contentIdentifier`: An opaque identifier for the content. The value of this identifier depends on the particular system used to provide the decryption key.
- `options`: Additional information necessary to obtain the key, or `nil` if no additional information is required.

## Topics

### Configuration options
- [let AVAssetResourceLoadingRequestStreamingContentKeyRequestRequiresPersistentKey: String](../avassetresourceloadingrequeststreamingcontentkeyrequestrequirespersistentkey.md)
  Specifies whether the content key request requires a persistable key to be returned from the key vendor.

## See Also

### Accessing the request data
- [var request: URLRequest](./request.md)
  The URL request object for the resource.
- [var requestor: AVAssetResourceLoadingRequestor](./requestor.md)
  The asset resource requestor that made the request.
- [var contentInformationRequest: AVAssetResourceLoadingContentInformationRequest?](./contentinformationrequest.md)
  The information for a requested resource.
- [var dataRequest: AVAssetResourceLoadingDataRequest?](./datarequest.md)
  The range of requested resource data.
- [var redirect: URLRequest?](./redirect.md)
  An URL request instance if the loading request was redirected.
- [func persistentContentKey(fromKeyVendorResponse: Data, options: [String : Any]?) throws -> Data](./persistentcontentkey%28fromkeyvendorresponse,options%29.md)
  Obtains a persistable content key from a context.
- [let AVAssetResourceLoadingRequestStreamingContentKeyRequestRequiresPersistentKey: String](../avassetresourceloadingrequeststreamingcontentkeyrequestrequirespersistentkey.md)
  Specifies whether the content key request requires a persistable key to be returned from the key vendor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/streamingcontentkeyrequestdata(forapp:contentidentifier:options:))*