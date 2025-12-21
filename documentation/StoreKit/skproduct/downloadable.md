# downloadable

**Framework**: StoreKit  
**Kind**: property

A Boolean value that indicates whether the App Store has downloadable content for this product.

**Availability**:
- macOS 10.8+

## Declaration

```swift
var downloadable: Bool { get }
```

#### Discussion

You can associate a set of data files with the App Store Connect record you created for a product. The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) if at least one file has been associated with the product.

## See Also

- [var isDownloadable: Bool](skproduct/isdownloadable.md)
  A Boolean value that indicates whether the App Store has downloadable content for this product.
- [var downloadContentLengths: [NSNumber]](skproduct/downloadcontentlengths.md)
  The lengths of the downloadable files available for this product.
- [var downloadContentVersion: String](skproduct/downloadcontentversion.md)
  A string that identifies which version of the content is available for download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproduct/downloadable)*