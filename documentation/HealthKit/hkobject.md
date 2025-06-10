# HKObject

**Framework**: HealthKit  
**Kind**: class

A piece of data that can be stored inside the HealthKit store.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class HKObject
```

## Mentions

- [About the HealthKit framework](about-the-healthkit-framework.md)

#### Overview

The `HKObject` class is an abstract class. You should never instantiate a `HKObject` object directly. Instead, always work with one of its concrete subclasses: [`HKCategorySample`](hkcategorysample.md), [`HKQuantitySample`](hkquantitysample.md), [`HKCorrelation`](hkcorrelation.md), or [`HKWorkout`](hkworkout.md).

HealthKit objects are all immutable. With a few exceptions (such as the object’s source revision), the object’s properties are set when the object is first created and they cannot change.

## Topics

### Accessing Properties
- [var uuid: UUID](hkobject/uuid.md)
  The universally unique identifier (UUID) for this HealthKit object.
- [var metadata: [String : Any]?](hkobject/metadata.md)
  The metadata for this HealthKit object.
- [var device: HKDevice?](hkobject/device.md)
  The device that generated the data for this object.
- [var sourceRevision: HKSourceRevision](hkobject/sourcerevision.md)
  The app or device that created this object.
- [var source: HKSource](hkobject/source.md)
  A HealthKit source, representing the app or device that created this object.
### Specifying Predicate Key Paths
- [let HKPredicateKeyPathUUID: String](hkpredicatekeypathuuid.md)
  The key path for accessing the object’s UUID inside a predicate format string.
- [let HKPredicateKeyPathMetadata: String](hkpredicatekeypathmetadata.md)
  The key path for accessing the object’s metadata dictionary inside a predicate format string.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [HKSample](hksample.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class HKQuantitySample](hkquantitysample.md)
  A sample that represents a quantity, including the value and the units.
- [class HKSample](hksample.md)
  A HealthKit sample represents a piece of data associated with a start and end time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkobject)*