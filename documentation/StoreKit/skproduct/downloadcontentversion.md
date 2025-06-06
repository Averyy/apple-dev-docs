# downloadContentVersion

**Framework**: StoreKit  
**Kind**: property

A string that identifies which version of the content is available for download.

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
var downloadContentVersion: String { get }
```

#### Discussion

The version string is formatted as a series of integers separated by periods.

## See Also

- [var isDownloadable: Bool](skproduct/isdownloadable.md)
  A Boolean value that indicates whether the App Store has downloadable content for this product.
- [var downloadContentLengths: [NSNumber]](skproduct/downloadcontentlengths.md)
  The lengths of the downloadable files available for this product.
- [var downloadable: Bool](skproduct/downloadable.md)
  A Boolean value that indicates whether the App Store has downloadable content for this product.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproduct/downloadcontentversion)*