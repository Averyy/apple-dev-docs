# allowedContentTypes

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The types of data that are accepted as a valid response for the requested resource.

**Availability**:
- iOS 11.2+
- iPadOS 11.2+
- Mac Catalyst 13.1+
- macOS 10.13.2+
- tvOS 11.2+
- visionOS 1.0+

## Declaration

```swift
var allowedContentTypes: [String]? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSArray<NSString *> * allowedContentTypes;
```

#### Discussion

This property contains an array of file format UTIs. When `allowedContentTypes` is non-nil, the value of [`contentType`](./contenttype.md) must be set to a value contained in `allowedContentTypes` or `nil`.

## See Also

### Configuring content information
- [var contentType: String?](./contenttype.md)
  The UTI that specifies the type of data contained by the requested resource.
- [var contentLength: Int64](./contentlength.md)
  The length, in bytes, of the requested resource.
- [var isByteRangeAccessSupported: Bool](./isbyterangeaccesssupported.md)
  A Boolean value that indicates whether random access to arbitrary ranges of bytes of the resource is supported.
- [var renewalDate: Date?](./renewaldate.md)
  The date at which a new resource loading request will be issued for resources that expire, if the media system still requires it.
- [var isEntireLengthAvailableOnDemand: Bool](./isentirelengthavailableondemand.md)
  A Boolean value that indicates whether asset data loading can expect data immediately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingcontentinformationrequest/allowedcontenttypes)*