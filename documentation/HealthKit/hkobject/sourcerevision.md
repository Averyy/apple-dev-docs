# sourceRevision

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The app or device that created this object.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var sourceRevision: HKSourceRevision { get }
```

```objc
@property (strong, readonly) HKSourceRevision * sourceRevision;
```

## Discussion

For samples saved by an app, the source revision is set to the version of the app that saved the object. For devices that write directly to HealthKit, the source revision is set to the version of the device that saved the object, while more complete device information is saved to the [`device`](./device.md) property.

The source revision property is only available on objects you have retrieved from the HealthKit store. When you create a new object, the source revision is set to `nil`. The system automatically sets this property to represent the current version of the app that saved the object to the HealthKit store. The source revision is then available the next time the object is retrieved from the store.

## See Also

### Accessing Properties
- [var uuid: UUID](./uuid.md)
  The universally unique identifier (UUID) for this HealthKit object.
- [var metadata: [String : Any]?](./metadata.md)
  The metadata for this HealthKit object.
- [var device: HKDevice?](./device.md)
  The device that generated the data for this object.
- [var source: HKSource](./source.md)
  A HealthKit source, representing the app or device that created this object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkobject/sourcerevision)*