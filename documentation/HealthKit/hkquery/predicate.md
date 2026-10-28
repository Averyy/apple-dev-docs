# predicate

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

A predicate used to filter the objects returned from the HealthKit store.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var predicate: NSPredicate? { get }
```

```objc
@property (strong, readonly, nullable) NSPredicate * predicate;
```

## Discussion

If the predicate is `nil`, the query does not filter its results. Instead, it returns all the objects matching the query’s other parameters.

## See Also

### Accessing properties
- [var objectType: HKObjectType?](./objecttype.md)
  The type of objects being queried.
- [var sampleType: HKSampleType?](./sampletype.md)
  The type of objects being queried.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery/predicate)*