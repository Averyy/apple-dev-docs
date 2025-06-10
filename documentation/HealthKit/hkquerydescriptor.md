# HKQueryDescriptor

**Framework**: HealthKit  
**Kind**: class

A descriptor that specifies a set of samples based on the data type and a predicate.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
class HKQueryDescriptor
```

#### Overview

Use descriptors to create queries that return multiple data types. You can use descriptors when creating [`HKSampleQuery`](hksamplequery.md), [`HKAnchoredObjectQuery`](hkanchoredobjectquery.md), or [`HKObserverQuery`](hkobserverquery.md) instances.

## Topics

### Creating Query Descriptors
- [init(sampleType: HKSampleType, predicate: NSPredicate?)](hkquerydescriptor/init(sampletype:predicate:).md)
  Creates a new descriptor for the data type and predicate you provided.
### Accessing Descriptor Data
- [var predicate: NSPredicate?](hkquerydescriptor/predicate.md)
  The predicate that filters samples matching this descriptor.
- [var sampleType: HKSampleType](hkquerydescriptor/sampletype.md)
  The data type of samples that match this descriptor.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct HKSampleQueryDescriptor](hksamplequerydescriptor.md)
  A query interface that reads samples using Swift concurrency.
- [class HKSampleQuery](hksamplequery.md)
  A general query that returns a snapshot of all the matching samples currently saved in the HealthKit store.
- [class HKCorrelationQuery](hkcorrelationquery.md)
  A query that performs complex searches based on the correlation’s contents, and returns a snapshot of all matching samples.
- [class HKQuery](hkquery.md)
  An abstract class for all the query classes in HealthKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquerydescriptor)*