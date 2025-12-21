# isByteRangeAccessSupported

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether random access to arbitrary ranges of bytes of the resource is supported.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var isByteRangeAccessSupported: Bool { get set }
```

#### Discussion

Before finishing loading an [`AVAssetResourceLoadingRequest`](avassetresourceloadingrequest.md) instance, if its [`contentInformationRequest`](avassetresourceloadingrequest/contentinformationrequest.md) property is not `nil`, set the value of this property to [`true`](https://developer.apple.com/documentation/Swift/true) if it supports random access to arbitrary ranges of bytes of the resource.

If this property is not [`true`](https://developer.apple.com/documentation/Swift/true) for resources that must be loaded incrementally, loading of the resource may fail. Such resources include anything that contains media data.

If byte range access is supported  portions of the resource can be requested more than once.

## See Also

- [var allowedContentTypes: [String]?](avassetresourceloadingcontentinformationrequest/allowedcontenttypes.md)
  The types of data that are accepted as a valid response for the requested resource.
- [var contentType: String?](avassetresourceloadingcontentinformationrequest/contenttype.md)
  The UTI that specifies the type of data contained by the requested resource.
- [var contentLength: Int64](avassetresourceloadingcontentinformationrequest/contentlength.md)
  The length, in bytes, of the requested resource.
- [var renewalDate: Date?](avassetresourceloadingcontentinformationrequest/renewaldate.md)
  The date at which a new resource loading request will be issued for resources that expire, if the media system still requires it.
- [var isEntireLengthAvailableOnDemand: Bool](avassetresourceloadingcontentinformationrequest/isentirelengthavailableondemand.md)
  A Boolean value that indicates whether asset data loading can expect data immediately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingcontentinformationrequest/isbyterangeaccesssupported)*