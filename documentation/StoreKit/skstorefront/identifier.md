# identifier

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

A value defined by Apple that uniquely identifies an App Store storefront.

**Availability**:
- iOS 13.0+ - Deprecated in 18.0
- iPadOS 13.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.15+ - Deprecated in 15.0
- tvOS 13.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: Use 'Storefront.id'.

## Declaration

```swift
var identifier: String { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) NSString * identifier;
```

*macOS*

```objc
@property (atomic, copy, readonly) NSString * identifier;
```

## See Also

### Identifying the Storefront
- [var countryCode: String](./countrycode.md)
  The three-letter code representing the country or region associated with the App Store storefront.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skstorefront/identifier)*