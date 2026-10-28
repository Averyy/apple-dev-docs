# contentVersion

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

A string that identifies which version of the content is available for download.

**Availability**:
- iOS 6.0+ - Deprecated in 16.0
- iPadOS 6.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.8+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- watchOS 6.2+ - Deprecated in 9.0

> **Deprecated**: Hosted content is no longer supported.

## Declaration

```swift
var contentVersion: String { get }
```

```objc
@property (nonatomic, readonly) NSString * contentVersion;
```

## Discussion

The version string must be formatted as a series of integers separated by periods.

## See Also

### Getting Content Information
- [var expectedContentLength: Int64](./expectedcontentlength.md)
  The length of the downloadable content, in bytes.
- [var contentIdentifier: String](./contentidentifier.md)
  A string that uniquely identifies the downloadable content.
- [var transaction: SKPaymentTransaction](./transaction.md)
  The transaction associated with the downloadable file.
- [var contentLength: Int64](./contentlength.md)
  The length of the downloadable content, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skdownload/contentversion)*