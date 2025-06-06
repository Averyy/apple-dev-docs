# objectType

**Framework**: HealthKit  
**Kind**: property

The type of objects being queried.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.2+

## Declaration

```swift
var objectType: HKObjectType? { get }
```

#### Discussion

Not all queries return objects of the specified type; however, they all use the object type to filter their results. For example, source queries return a set of data sources that have saved objects with a matching type, while statistics queries return statistical information about the objects with a matching type.

## See Also

- [var predicate: NSPredicate?](hkquery/predicate.md)
  A predicate used to filter the objects returned from the HealthKit store.
- [var sampleType: HKSampleType?](hkquery/sampletype.md)
  The type of objects being queried.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery/objecttype)*