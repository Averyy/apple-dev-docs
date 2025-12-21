# isDownloadable

**Framework**: StoreKit  
**Kind**: property

A Boolean value that indicates whether the App Store has downloadable content for this product.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS ?+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
var isDownloadable: Bool { get }
```

#### Discussion

You can associate a set of data files with the App Store Connect record you created for a product. The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) if at least one file has been associated with the product.

## See Also

- [var downloadContentLengths: [NSNumber]](skproduct/downloadcontentlengths.md)
  The lengths of the downloadable files available for this product.
- [var downloadContentVersion: String](skproduct/downloadcontentversion.md)
  A string that identifies which version of the content is available for download.
- [var downloadable: Bool](skproduct/downloadable.md)
  A Boolean value that indicates whether the App Store has downloadable content for this product.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproduct/isdownloadable)*