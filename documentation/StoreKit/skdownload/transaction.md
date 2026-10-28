# transaction

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The transaction associated with the downloadable file.

**Availability**:
- iOS 6.0+ - Deprecated in 16.0
- iPadOS 6.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.11+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- watchOS 6.2+ - Deprecated in 9.0

> **Deprecated**: Hosted content is no longer supported.

## Declaration

```swift
var transaction: SKPaymentTransaction { get }
```

```objc
@property (nonatomic, readonly) SKPaymentTransaction * transaction;
```

## Discussion

A download object is always associated with a payment transaction. The download object may only be queued after payment is processed and before the transaction is finished.

## See Also

### Getting Content Information
- [var expectedContentLength: Int64](./expectedcontentlength.md)
  The length of the downloadable content, in bytes.
- [var contentIdentifier: String](./contentidentifier.md)
  A string that uniquely identifies the downloadable content.
- [var contentVersion: String](./contentversion.md)
  A string that identifies which version of the content is available for download.
- [var contentLength: Int64](./contentlength.md)
  The length of the downloadable content, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skdownload/transaction)*