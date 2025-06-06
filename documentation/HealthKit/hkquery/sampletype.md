# sampleType

**Framework**: HealthKit  
**Kind**: property

The type of objects being queried.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var sampleType: HKSampleType? { get }
```

#### Discussion

Not all queries return objects of the specified type; however, they all use the object type to generate their results. For example, source queries return a set of data sources that have saved objects with a matching type, while statistics queries return statistical information about the objects with a matching type.

## See Also

- [var predicate: NSPredicate?](hkquery/predicate.md)
  A predicate used to filter the objects returned from the HealthKit store.
- [var objectType: HKObjectType?](hkquery/objecttype.md)
  The type of objects being queried.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery/sampletype)*