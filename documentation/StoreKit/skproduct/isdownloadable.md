# isDownloadable

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the App Store has downloadable content for this product.

**Availability**:
- iOS 6.0+ - Deprecated in 16.0
- iPadOS 6.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.15+ - Deprecated in 13.0
- tvOS - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 9.0

> **Deprecated**: Hosted content is no longer supported.

## Declaration

```swift
var isDownloadable: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL isDownloadable;
```

#### Discussion

You can associate a set of data files with the App Store Connect record you created for a product. The value of this property is [`true`](../../Swift/true.md) if at least one file has been associated with the product.

## See Also

### Getting Downloadable Content Information
- [var downloadContentLengths: [NSNumber]](./downloadcontentlengths.md)
  The lengths of the downloadable files available for this product.
- [var downloadContentVersion: String](./downloadcontentversion.md)
  A string that identifies which version of the content is available for download.
- [var downloadable: Bool](./downloadable.md)
  A Boolean value that indicates whether the App Store has downloadable content for this product.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproduct/isdownloadable)*