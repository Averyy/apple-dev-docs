# productType

**Framework**: Healthkit  
**Kind**: property

A string that identifies the device used to save a sample.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var productType: String? { get }
```

#### Discussion

For samples saved on Apple Watch Series 2, HealthKit sets the product type property to `watch2,4`.

> **Note**:  Samples saved using older versions of HealthKit may have a `nil`-valued product type, indicating that the product type is unknown.

## Topics

### Constants
- [let HKSourceRevisionAnyProductType: String](hksourcerevisionanyproducttype.md)
  A constant that matches any product type.

## See Also

- [var source: HKSource](hksourcerevision/source.md)
  The source for a sample.
- [var version: String?](hksourcerevision/version.md)
  A string that identifies a particular version of the source.
- [var operatingSystemVersion: OperatingSystemVersion](hksourcerevision/operatingsystemversion.md)
  A string that identifies the operating system used to save a sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hksourcerevision/producttype)*