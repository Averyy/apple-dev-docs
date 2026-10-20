# productType

**Framework**: SensorKit  
**Kind**: property  
**Role**: Instance Property

A string that identifies the device used to save a sample.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
var productType: String { get }
```

```objc
@property (copy, readonly) NSString * productType;
```

#### Discussion

> **Note**:  Samples saved using older versions of SensorKit may have a `nil`-valued product type that indicates the product type is unknown.

## See Also

### Accessing Device Information
- [var model: String](./model.md)
  The user-defined name of the device.
- [var name: String](./name.md)
  The framework-defined name of the device.
- [var systemName: String](./systemname.md)
  The device’s operating system.
- [var systemVersion: String](./systemversion.md)
  The device’s operating system version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srdevice/producttype)*