# source

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

A HealthKit source, representing the app or device that created this object.

**Availability**:
- iOS 8.0+ - Deprecated in 9.0
- iPadOS 8.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 13.0+
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: This property is deprecated. Use [`sourceRevision`](./sourcerevision.md) instead.

## Declaration

```swift
var source: HKSource { get }
```

```objc
@property (strong, readonly) HKSource * source;
```

## Discussion

The `source` property is only available on objects you have retrieved from the HealthKit store. When you create a new object, the source is set to `nil`. The system automatically sets the source property when you save the object to the HealthKit store. The source is then available the next time the object is retrieved from the store.

## See Also

### Accessing Properties
- [var uuid: UUID](./uuid.md)
  The universally unique identifier (UUID) for this HealthKit object.
- [var metadata: [String : Any]?](./metadata.md)
  The metadata for this HealthKit object.
- [var device: HKDevice?](./device.md)
  The device that generated the data for this object.
- [var sourceRevision: HKSourceRevision](./sourcerevision.md)
  The app or device that created this object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkobject/source)*