# contentLength

**Framework**: AVFoundation  
**Kind**: property

The length, in bytes, of the requested resource.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var contentLength: Int64 { get set }
```

#### Discussion

Before finishing loading an [`AVAssetResourceLoadingRequest`](avassetresourceloadingrequest.md) instance, if its [`contentInformationRequest`](avassetresourceloadingrequest/contentinformationrequest.md) property is not `nil`, set the value of the `contentLength` property to the number of bytes contained by the requested resource.

## See Also

- [var allowedContentTypes: [String]?](avassetresourceloadingcontentinformationrequest/allowedcontenttypes.md)
  The types of data that are accepted as a valid response for the requested resource.
- [var contentType: String?](avassetresourceloadingcontentinformationrequest/contenttype.md)
  The UTI that specifies the type of data contained by the requested resource.
- [var isByteRangeAccessSupported: Bool](avassetresourceloadingcontentinformationrequest/isbyterangeaccesssupported.md)
  A Boolean value that indicates whether random access to arbitrary ranges of bytes of the resource is supported.
- [var renewalDate: Date?](avassetresourceloadingcontentinformationrequest/renewaldate.md)
  The date at which a new resource loading request will be issued for resources that expire, if the media system still requires it.
- [var isEntireLengthAvailableOnDemand: Bool](avassetresourceloadingcontentinformationrequest/isentirelengthavailableondemand.md)
  A Boolean value that indicates whether asset data loading can expect data immediately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingcontentinformationrequest/contentlength)*