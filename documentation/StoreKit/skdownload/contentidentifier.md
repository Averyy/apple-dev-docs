# contentIdentifier

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

A string that uniquely identifies the downloadable content.

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
var contentIdentifier: String { get }
```

```objc
@property (nonatomic, readonly) NSString * contentIdentifier;
```

## Discussion

Each piece of downloadable content associated with a product has its own unique identifier. The content identifier is specified in App Store Connect when you add the content.

## See Also

### Related Documentation
- [Apple In-App Purchase Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Introduction.html#//apple_ref/doc/uid/TP40008267)
### Getting Content Information
- [var expectedContentLength: Int64](./expectedcontentlength.md)
  The length of the downloadable content, in bytes.
- [var contentVersion: String](./contentversion.md)
  A string that identifies which version of the content is available for download.
- [var transaction: SKPaymentTransaction](./transaction.md)
  The transaction associated with the downloadable file.
- [var contentLength: Int64](./contentlength.md)
  The length of the downloadable content, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skdownload/contentidentifier)*