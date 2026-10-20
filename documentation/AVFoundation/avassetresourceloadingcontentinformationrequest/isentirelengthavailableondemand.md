# isEntireLengthAvailableOnDemand

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether asset data loading can expect data immediately.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var isEntireLengthAvailableOnDemand: Bool { get set }
```

```objc
@property (nonatomic, getter=isEntireLengthAvailableOnDemand) BOOL entireLengthAvailableOnDemand;
```

#### Discussion

Before you finish loading an [`AVAssetResourceLoadingRequest`](../avassetresourceloadingrequest.md), if its [`contentInformationRequest`](../avassetresourceloadingrequest/contentinformationrequest.md) isn’t `nil`, set the value to [`true`](../../Swift/true.md) to indicate that all asset data is available. This may be [`true`](../../Swift/true.md) because the data is fully cached, or because the custom URL scheme ultimately refers to files on local storage, which allows for significant data flow optimizations.

For backward compatibility, this property defaults to [`false`](../../Swift/false.md).

## See Also

### Configuring content information
- [var allowedContentTypes: [String]?](./allowedcontenttypes.md)
  The types of data that are accepted as a valid response for the requested resource.
- [var contentType: String?](./contenttype.md)
  The UTI that specifies the type of data contained by the requested resource.
- [var contentLength: Int64](./contentlength.md)
  The length, in bytes, of the requested resource.
- [var isByteRangeAccessSupported: Bool](./isbyterangeaccesssupported.md)
  A Boolean value that indicates whether random access to arbitrary ranges of bytes of the resource is supported.
- [var renewalDate: Date?](./renewaldate.md)
  The date at which a new resource loading request will be issued for resources that expire, if the media system still requires it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingcontentinformationrequest/isentirelengthavailableondemand)*