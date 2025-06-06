# localizedDescription

**Framework**: StoreKit  
**Kind**: property

A description of the product.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS ?+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
var localizedDescription: String { get }
```

#### Discussion

The description’s language is determined by the storefront that the user’s device is connected to, not the preferred language set on the device.

## See Also

- [class SKStorefront](skstorefront.md)
  An object containing the location and unique identifier of an Apple App Store storefront.
- [var localizedTitle: String](skproduct/localizedtitle.md)
  The name of the product.
- [var contentVersion: String](skproduct/contentversion.md)
  A string that identifies the version of the content.
- [var isFamilyShareable: Bool](skproduct/isfamilyshareable.md)
  A Boolean value that indicates whether the product is available for Family Sharing in App Store Connect.
- [var contentLengths: [NSNumber]](skproduct/contentlengths.md)
  The total size of the content, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproduct/localizeddescription)*