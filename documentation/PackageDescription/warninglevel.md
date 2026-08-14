# WarningLevel

**Framework**: PackageDescription  
**Kind**: enum

The level at which a compiler warning should be treated.

**Availability**:
- SwiftPM 6.2+

## Declaration

```swift
enum WarningLevel
```

#### Overview

This enum is used with the `SwiftSetting.treatAllWarnings(as:_:)` and `SwiftSetting.treatWarning(name:as:_:)` methods to control how warnings are handled during compilation.

## Topics

### Enumeration Cases
- [WarningLevel.error](warninglevel/error.md)
  Treat as an error.
- [WarningLevel.warning](warninglevel/warning.md)
  Treat as a warning.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/warninglevel)*