# device

**Framework**: HealthKit  
**Kind**: property

The device that generated the data for this object.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var device: HKDevice? { get }
```

## See Also

- [var uuid: UUID](hkobject/uuid.md)
  The universally unique identifier (UUID) for this HealthKit object.
- [var metadata: [String : Any]?](hkobject/metadata.md)
  The metadata for this HealthKit object.
- [var sourceRevision: HKSourceRevision](hkobject/sourcerevision.md)
  The app or device that created this object.
- [var source: HKSource](hkobject/source.md)
  A HealthKit source, representing the app or device that created this object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkobject/device)*