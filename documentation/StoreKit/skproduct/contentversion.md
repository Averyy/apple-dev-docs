# contentVersion

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

A string that identifies the version of the content.

**Availability**:
- iOS 3.0+ - Deprecated in 18.0
- iPadOS 3.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.8+ - Deprecated in 10.14
- tvOS - Deprecated in 18.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: Use Product.

## Declaration

```swift
var contentVersion: String { get }
```

```objc
@property (nonatomic, readonly) NSString * contentVersion;
```

## See Also

### Getting Product Attributes
- [var localizedDescription: String](./localizeddescription.md)
  A description of the product.
- [var localizedTitle: String](./localizedtitle.md)
  The name of the product.
- [var isFamilyShareable: Bool](./isfamilyshareable.md)
  A Boolean value that indicates whether the product is available for Family Sharing in App Store Connect.
- [var contentLengths: [NSNumber]](./contentlengths.md)
  The total size of the content, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproduct/contentversion)*