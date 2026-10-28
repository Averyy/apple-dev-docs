# downloadContentLengths

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The lengths of the downloadable files available for this product.

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
var downloadContentLengths: [NSNumber] { get }
```

```objc
@property (nonatomic, readonly) NSArray<NSNumber *> * downloadContentLengths;
```

## Discussion

The array holds [`NSNumber`](../../Foundation/nsnumber.md) objects, each of which holds a `long long` value that is the size of one of the downloadable files (in bytes).

## See Also

### Getting Downloadable Content Information
- [var isDownloadable: Bool](./isdownloadable.md)
  A Boolean value that indicates whether the App Store has downloadable content for this product.
- [var downloadContentVersion: String](./downloadcontentversion.md)
  A string that identifies which version of the content is available for download.
- [var downloadable: Bool](./downloadable.md)
  A Boolean value that indicates whether the App Store has downloadable content for this product.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproduct/downloadcontentlengths)*