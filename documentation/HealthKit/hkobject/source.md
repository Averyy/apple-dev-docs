# source

**Framework**: HealthKit  
**Kind**: property

A HealthKit source, representing the app or device that created this object.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var source: HKSource { get }
```

#### Discussion

The `source` property is only available on objects you have retrieved from the HealthKit store. When you create a new object, the source is set to `nil`. The system automatically sets the source property when you save the object to the HealthKit store. The source is then available the next time the object is retrieved from the store.

## See Also

- [var uuid: UUID](hkobject/uuid.md)
  The universally unique identifier (UUID) for this HealthKit object.
- [var metadata: [String : Any]?](hkobject/metadata.md)
  The metadata for this HealthKit object.
- [var device: HKDevice?](hkobject/device.md)
  The device that generated the data for this object.
- [var sourceRevision: HKSourceRevision](hkobject/sourcerevision.md)
  The app or device that created this object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkobject/source)*