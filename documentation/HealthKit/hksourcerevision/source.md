# source

**Framework**: HealthKit  
**Kind**: property

The source for a sample.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var source: HKSource { get }
```

#### Discussion

This property contains an [`HKSource`](hksource.md) object representing the app that saved the data into the HealthKit store. The source can also represent a hardware device that writes data directly to HealthKit (for example, an iPhone, Apple Watch, or Bluetooth LE heart rate monitor). Before iOS 9.0, the companion app for other peripherals also saved device information in the object’s [`source`](hksourcerevision/source.md) property.

## See Also

- [var version: String?](hksourcerevision/version.md)
  A string that identifies a particular version of the source.
- [var operatingSystemVersion: OperatingSystemVersion](hksourcerevision/operatingsystemversion.md)
  A string that identifies the operating system used to save a sample.
- [var productType: String?](hksourcerevision/producttype.md)
  A string that identifies the device used to save a sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hksourcerevision/source)*