# requestsAllDataToEndOfResource

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates the entire remaining length of the resource from the offest to the end of the resource is being requested.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var requestsAllDataToEndOfResource: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL requestsAllDataToEndOfResource;
```

#### Discussion

When this property is true, you should disregard the value of requestedLength and incrementally provide as much data, starting from the requested offset, as the resource contains. Continue until all available data was successfully loaded, the request was cancelled, or an error occurs.

## See Also

### Providing data to a request
- [func respond(with: Data)](./respond%28with%29.md)
  Provides data to the loading request.
- [var requestedLength: Int](./requestedlength.md)
  The length, in bytes, of the data requested.
- [var requestedOffset: Int64](./requestedoffset.md)
  The position within the resource of the first byte requested.
- [var currentOffset: Int64](./currentoffset.md)
  The position within the resource of the next byte.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingdatarequest/requestsalldatatoendofresource)*