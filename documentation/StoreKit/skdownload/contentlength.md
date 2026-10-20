# contentLength

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The length of the downloadable content, in bytes.

**Availability**:
- iOS 6.0+ - Deprecated in 13.0
- iPadOS 6.0+ - Deprecated in 13.0
- Mac Catalyst 13.0+ - Deprecated in 13.0
- macOS 10.8+ - Deprecated in 10.15
- tvOS 9.0+ - Deprecated in 13.0

> **Deprecated**: Use [`expectedContentLength`](./expectedcontentlength.md) instead.

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS*

```swift
var contentLength: Int64 { get }
```

*macOS*

```swift
@NSCopying
var contentLength: NSNumber { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly) long long contentLength;
```

*macOS*

```objc
@property (nonatomic, copy, readonly) NSNumber * contentLength;
```

## See Also

### Getting Content Information
- [var expectedContentLength: Int64](./expectedcontentlength.md)
  The length of the downloadable content, in bytes.
- [var contentIdentifier: String](./contentidentifier.md)
  A string that uniquely identifies the downloadable content.
- [var contentVersion: String](./contentversion.md)
  A string that identifies which version of the content is available for download.
- [var transaction: SKPaymentTransaction](./transaction.md)
  The transaction associated with the downloadable file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skdownload/contentlength)*