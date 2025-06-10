# productType

**Framework**: SensorKit  
**Kind**: property

A string that identifies the device used to save a sample.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
var productType: String { get }
```

#### Discussion

> **Note**:  Samples saved using older versions of SensorKit may have a `nil`-valued product type that indicates the product type is unknown.

## See Also

- [var model: String](srdevice/model.md)
  The user-defined name of the device.
- [var name: String](srdevice/name.md)
  The framework-defined name of the device.
- [var systemName: String](srdevice/systemname.md)
  The device’s operating system.
- [var systemVersion: String](srdevice/systemversion.md)
  The device’s operating system version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srdevice/producttype)*