# transaction

**Framework**: StoreKit  
**Kind**: property

The transaction associated with the downloadable file.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- watchOS 6.2+

## Declaration

```swift
var transaction: SKPaymentTransaction { get }
```

#### Discussion

A download object is always associated with a payment transaction. The download object may only be queued after payment is processed and before the transaction is finished.

## See Also

- [var expectedContentLength: Int64](skdownload/expectedcontentlength.md)
  The length of the downloadable content, in bytes.
- [var contentIdentifier: String](skdownload/contentidentifier.md)
  A string that uniquely identifies the downloadable content.
- [var contentVersion: String](skdownload/contentversion.md)
  A string that identifies which version of the content is available for download.
- [var contentLength: Int64](skdownload/contentlength.md)
  The length of the downloadable content, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skdownload/transaction)*