# contentVersion

**Framework**: StoreKit  
**Kind**: property

A string that identifies which version of the content is available for download.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- watchOS 6.2+

## Declaration

```swift
var contentVersion: String { get }
```

#### Discussion

The version string must be formatted as a series of integers separated by periods.

## See Also

- [var expectedContentLength: Int64](skdownload/expectedcontentlength.md)
  The length of the downloadable content, in bytes.
- [var contentIdentifier: String](skdownload/contentidentifier.md)
  A string that uniquely identifies the downloadable content.
- [var transaction: SKPaymentTransaction](skdownload/transaction.md)
  The transaction associated with the downloadable file.
- [var contentLength: Int64](skdownload/contentlength.md)
  The length of the downloadable content, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skdownload/contentversion)*