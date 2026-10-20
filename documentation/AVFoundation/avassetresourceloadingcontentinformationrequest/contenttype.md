# contentType

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The UTI that specifies the type of data contained by the requested resource.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var contentType: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * contentType;
```

#### Discussion

Before finishing loading an [`AVAssetResourceLoadingRequest`](../avassetresourceloadingrequest.md) instance, if its [`contentInformationRequest`](../avassetresourceloadingrequest/contentinformationrequest.md) property is  not `nil`, set the value of this property to a UTI indicating the type of data contained by the requested resource.

When responding to an `AVAssetResourceLoadingRequest` for a FairPlay Streaming key, only set `contentType` to [`AVStreamingKeyDeliveryContentKeyType`](../avstreamingkeydeliverycontentkeytype.md), [`AVStreamingKeyDeliveryPersistentContentKeyType`](../avstreamingkeydeliverypersistentcontentkeytype.md), or `nil`. The value of contentType must be contained in the [`allowedContentTypes`](./allowedcontenttypes.md) property or `nil`.

## See Also

### Configuring content information
- [var allowedContentTypes: [String]?](./allowedcontenttypes.md)
  The types of data that are accepted as a valid response for the requested resource.
- [var contentLength: Int64](./contentlength.md)
  The length, in bytes, of the requested resource.
- [var isByteRangeAccessSupported: Bool](./isbyterangeaccesssupported.md)
  A Boolean value that indicates whether random access to arbitrary ranges of bytes of the resource is supported.
- [var renewalDate: Date?](./renewaldate.md)
  The date at which a new resource loading request will be issued for resources that expire, if the media system still requires it.
- [var isEntireLengthAvailableOnDemand: Bool](./isentirelengthavailableondemand.md)
  A Boolean value that indicates whether asset data loading can expect data immediately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingcontentinformationrequest/contenttype)*