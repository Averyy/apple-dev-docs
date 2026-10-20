# downloadContentVersion

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

A string that identifies which version of the content is available for download.

**Availability**:
- iOS 6.0+ - Deprecated in 16.0
- iPadOS 6.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.14+ - Deprecated in 13.0
- tvOS - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 9.0

> **Deprecated**: Hosted content is no longer supported.

## Declaration

```swift
var downloadContentVersion: String { get }
```

```objc
@property (nonatomic, readonly) NSString * downloadContentVersion;
```

#### Discussion

The version string is formatted as a series of integers separated by periods.

## See Also

### Getting Downloadable Content Information
- [var isDownloadable: Bool](./isdownloadable.md)
  A Boolean value that indicates whether the App Store has downloadable content for this product.
- [var downloadContentLengths: [NSNumber]](./downloadcontentlengths.md)
  The lengths of the downloadable files available for this product.
- [var downloadable: Bool](./downloadable.md)
  A Boolean value that indicates whether the App Store has downloadable content for this product.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproduct/downloadcontentversion)*