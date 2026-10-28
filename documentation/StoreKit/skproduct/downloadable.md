# downloadable

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the App Store has downloadable content for this product.

**Availability**:
- macOS 10.8+ - Deprecated in 10.15

> **Deprecated**: Use [`isDownloadable`](./isdownloadable.md) instead.

## Declaration

```swift
var downloadable: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL downloadable;
```

## Discussion

You can associate a set of data files with the App Store Connect record you created for a product. The value of this property is [`true`](../../Swift/true.md) if at least one file has been associated with the product.

## See Also

### Getting Downloadable Content Information
- [var isDownloadable: Bool](./isdownloadable.md)
  A Boolean value that indicates whether the App Store has downloadable content for this product.
- [var downloadContentLengths: [NSNumber]](./downloadcontentlengths.md)
  The lengths of the downloadable files available for this product.
- [var downloadContentVersion: String](./downloadcontentversion.md)
  A string that identifies which version of the content is available for download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproduct/downloadable)*