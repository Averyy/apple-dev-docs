# countryCode

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The three-letter code that represents the country or region associated with the App Store storefront.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
let countryCode: String
```

#### Discussion

This property uses the ISO 3166-1 Alpha-3 country code representation.

## See Also

### Identifying the storefront
- [static var current: Storefront?](./current.md)
  The current App Store storefront for product purchases.
- [let id: String](./id.md)
  An Apple-defined value that uniquely identifies an App Store storefront.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/storefront/countrycode)*