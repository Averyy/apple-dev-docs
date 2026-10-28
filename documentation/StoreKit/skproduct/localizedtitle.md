# localizedTitle

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The name of the product.

**Availability**:
- iOS 3.0+ - Deprecated in 18.0
- iPadOS 3.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.7+ - Deprecated in 15.0
- tvOS - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: Use Product.displayName.

## Declaration

```swift
var localizedTitle: String { get }
```

```objc
@property (nonatomic, readonly) NSString * localizedTitle;
```

## Discussion

The title’s language is determined by the storefront that the user’s device is connected to, not the preferred language set on the device.

## See Also

### Related Documentation
- [class SKStorefront](../skstorefront.md)
  An object containing the location and unique identifier of an Apple App Store storefront.
### Getting Product Attributes
- [var localizedDescription: String](./localizeddescription.md)
  A description of the product.
- [var contentVersion: String](./contentversion.md)
  A string that identifies the version of the content.
- [var isFamilyShareable: Bool](./isfamilyshareable.md)
  A Boolean value that indicates whether the product is available for Family Sharing in App Store Connect.
- [var contentLengths: [NSNumber]](./contentlengths.md)
  The total size of the content, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproduct/localizedtitle)*