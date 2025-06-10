# version

**Framework**: HealthKit  
**Kind**: property

A string that identifies a particular version of the source.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var version: String? { get }
```

#### Discussion

This property contains a string that identifies the version of the app or device used to save the sample. If the sample is saved by an app, the property contains the current version number of the app (for example, `1.4`). If it is saved by an iOS device or an Apple Watch, the property contains the current version number of the device’s OS (for example, `9.0` or `2.0` respectively). If it is saved directly by a Bluetooth device, this property contains the version string provided by that device.

> **Note**:  For samples saved prior to iOS 9.0 or watchOS 2.0, the version is set to `nil`.

## Topics

### Constants
- [let HKSourceRevisionAnyVersion: String](hksourcerevisionanyversion.md)
  A constant that matches any version.

## See Also

- [var source: HKSource](hksourcerevision/source.md)
  The source for a sample.
- [var operatingSystemVersion: OperatingSystemVersion](hksourcerevision/operatingsystemversion.md)
  A string that identifies the operating system used to save a sample.
- [var productType: String?](hksourcerevision/producttype.md)
  A string that identifies the device used to save a sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hksourcerevision/version)*