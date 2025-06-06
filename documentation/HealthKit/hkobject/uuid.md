# uuid

**Framework**: HealthKit  
**Kind**: property

The universally unique identifier (UUID) for this HealthKit object.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var uuid: UUID { get }
```

#### Discussion

HealthKit assigns a UUID to the object when you create it. If you want to add your own unique ID, add it to the object’s metadata using the [`HKMetadataKeyExternalUUID`](hkmetadatakeyexternaluuid.md) key.

## See Also

- [var metadata: [String : Any]?](hkobject/metadata.md)
  The metadata for this HealthKit object.
- [var device: HKDevice?](hkobject/device.md)
  The device that generated the data for this object.
- [var sourceRevision: HKSourceRevision](hkobject/sourcerevision.md)
  The app or device that created this object.
- [var source: HKSource](hkobject/source.md)
  A HealthKit source, representing the app or device that created this object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkobject/uuid)*