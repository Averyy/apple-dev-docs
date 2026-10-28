# uuid

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (strong, readonly) NSUUID * UUID;
```

## Discussion

HealthKit assigns a UUID to the object when you create it. If you want to add your own unique ID, add it to the object’s metadata using the [`HKMetadataKeyExternalUUID`](../hkmetadatakeyexternaluuid.md) key.

## See Also

### Accessing Properties
- [var metadata: [String : Any]?](./metadata.md)
  The metadata for this HealthKit object.
- [var device: HKDevice?](./device.md)
  The device that generated the data for this object.
- [var sourceRevision: HKSourceRevision](./sourcerevision.md)
  The app or device that created this object.
- [var source: HKSource](./source.md)
  A HealthKit source, representing the app or device that created this object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkobject/uuid)*