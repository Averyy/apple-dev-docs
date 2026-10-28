# countryCode

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The three-letter code representing the country or region associated with the App Store storefront.

**Availability**:
- iOS 13.0+ - Deprecated in 18.0
- iPadOS 13.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.15+ - Deprecated in 15.0
- tvOS 13.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: Use 'Storefront.countryCode'.

## Declaration

```swift
var countryCode: String { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) NSString * countryCode;
```

*macOS*

```objc
@property (atomic, copy, readonly) NSString * countryCode;
```

## Discussion

This property uses the ISO 3166-1 Alpha-3 country code representation.

## See Also

### Identifying the Storefront
- [var identifier: String](./identifier.md)
  A value defined by Apple that uniquely identifies an App Store storefront.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skstorefront/countrycode)*