# sampleType

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The type of objects being queried.

**Availability**:
- iOS 8.0+ - Deprecated in 9.3
- iPadOS 8.0+ - Deprecated in 9.3
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 13.0+
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.2

> **Deprecated**: Use [`objectType`](./objecttype.md) instead.

## Declaration

```swift
var sampleType: HKSampleType? { get }
```

```objc
@property (strong, readonly, nullable) HKSampleType * sampleType;
```

#### Discussion

Not all queries return objects of the specified type; however, they all use the object type to generate their results. For example, source queries return a set of data sources that have saved objects with a matching type, while statistics queries return statistical information about the objects with a matching type.

## See Also

### Accessing properties
- [var predicate: NSPredicate?](./predicate.md)
  A predicate used to filter the objects returned from the HealthKit store.
- [var objectType: HKObjectType?](./objecttype.md)
  The type of objects being queried.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery/sampletype)*