# operatingSystemVersion

**Framework**: Healthkit  
**Kind**: property

A string that identifies the operating system used to save a sample.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var operatingSystemVersion: OperatingSystemVersion { get }
```

#### Discussion

For samples saved on watchOS 4.0, HealthKit sets the operating system property to `{4, 0, 0}`.

> **Note**:  For samples saved using older versions of HealthKit, the system approximates the operating system. For instance, HealthKit marks samples saved after iOS 8.0 but before 8.2 as `{8, 0, 0}`. HealthKit marks samples saved after 8.2 but before 9.0  as `{8, 2, 0}`.

## Topics

### Constants
- [let HKSourceRevisionAnyOperatingSystem: OperatingSystemVersion](hksourcerevisionanyoperatingsystem.md)
  A constant that matches any operating system.

## See Also

- [var source: HKSource](hksourcerevision/source.md)
  The source for a sample.
- [var version: String?](hksourcerevision/version.md)
  A string that identifies a particular version of the source.
- [var productType: String?](hksourcerevision/producttype.md)
  A string that identifies the device used to save a sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hksourcerevision/operatingsystemversion)*