# downloadContentLengths

**Framework**: StoreKit  
**Kind**: property

The lengths of the downloadable files available for this product.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS ?+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
var downloadContentLengths: [NSNumber] { get }
```

#### Discussion

The array holds [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) objects, each of which holds a `long long` value that is the size of one of the downloadable files (in bytes).

## See Also

- [var isDownloadable: Bool](skproduct/isdownloadable.md)
  A Boolean value that indicates whether the App Store has downloadable content for this product.
- [var downloadContentVersion: String](skproduct/downloadcontentversion.md)
  A string that identifies which version of the content is available for download.
- [var downloadable: Bool](skproduct/downloadable.md)
  A Boolean value that indicates whether the App Store has downloadable content for this product.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproduct/downloadcontentlengths)*