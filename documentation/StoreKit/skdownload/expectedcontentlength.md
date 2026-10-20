# expectedContentLength

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The length of the downloadable content, in bytes.

**Availability**:
- iOS 13.0+ - Deprecated in 16.0
- iPadOS 13.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.15+ - Deprecated in 13.0
- tvOS 13.0+ - Deprecated in 16.0
- watchOS 6.2+ - Deprecated in 9.0

> **Deprecated**: Hosted content is no longer supported.

## Declaration

```swift
var expectedContentLength: Int64 { get }
```

```objc
@property (nonatomic, readonly) long long expectedContentLength;
```

## See Also

### Getting Content Information
- [var contentIdentifier: String](./contentidentifier.md)
  A string that uniquely identifies the downloadable content.
- [var contentVersion: String](./contentversion.md)
  A string that identifies which version of the content is available for download.
- [var transaction: SKPaymentTransaction](./transaction.md)
  The transaction associated with the downloadable file.
- [var contentLength: Int64](./contentlength.md)
  The length of the downloadable content, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skdownload/expectedcontentlength)*