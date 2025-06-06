# contentIdentifier

**Framework**: StoreKit  
**Kind**: property

A string that uniquely identifies the downloadable content.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- watchOS 6.2+

## Declaration

```swift
var contentIdentifier: String { get }
```

#### Discussion

Each piece of downloadable content associated with a product has its own unique identifier. The content identifier is specified in App Store Connect when you add the content.

## See Also

- [In-App Purchase Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Introduction.html#//apple_ref/doc/uid/TP40008267)
- [var expectedContentLength: Int64](skdownload/expectedcontentlength.md)
  The length of the downloadable content, in bytes.
- [var contentVersion: String](skdownload/contentversion.md)
  A string that identifies which version of the content is available for download.
- [var transaction: SKPaymentTransaction](skdownload/transaction.md)
  The transaction associated with the downloadable file.
- [var contentLength: Int64](skdownload/contentlength.md)
  The length of the downloadable content, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skdownload/contentidentifier)*