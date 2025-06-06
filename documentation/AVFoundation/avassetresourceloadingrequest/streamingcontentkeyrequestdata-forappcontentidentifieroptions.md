# streamingContentKeyRequestData(forApp:contentIdentifier:options:)

**Framework**: AVFoundation  
**Kind**: method

Obtains key request data for a specific combination of application and content.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+

## Declaration

```swift
func streamingContentKeyRequestData(forApp appIdentifier: Data, contentIdentifier: Data, options: [String : Any]? = nil) throws -> Data
```

#### Return Value

The key request data that must be transmitted to the key vendor to obtain the content key.

## Parameters

- `appIdentifier`: An opaque content identifier for the application. The value of this identifier depends on the particular system used to provide the decryption key.
- `contentIdentifier`: An opaque identifier for the content. The value of this identifier depends on the particular system used to provide the decryption key.
- `options`: Additional information necessary to obtain the key, or   if no additional information is required.

## Topics

### Configuration Options
- [let AVAssetResourceLoadingRequestStreamingContentKeyRequestRequiresPersistentKey: String](avassetresourceloadingrequeststreamingcontentkeyrequestrequirespersistentkey.md)
  Specifies whether the content key request requires a persistable key to be returned from the key vendor.

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
- [func persistentContentKey(fromKeyVendorResponse: Data, options: [String : Any]?) throws -> Data](avassetresourceloadingrequest/persistentcontentkey(fromkeyvendorresponse:options:).md)
  Obtains a persistable content key from a context.
- [let AVAssetResourceLoadingRequestStreamingContentKeyRequestRequiresPersistentKey: String](avassetresourceloadingrequeststreamingcontentkeyrequestrequirespersistentkey.md)
  Specifies whether the content key request requires a persistable key to be returned from the key vendor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/streamingcontentkeyrequestdata(forapp:contentidentifier:options:))*