# correlationType

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The type of correlation to search for.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@NSCopying
var correlationType: HKCorrelationType { get }
```

```objc
@property (copy, readonly) HKCorrelationType * correlationType;
```

## See Also

### Getting Property Data
- [var samplePredicates: [HKSampleType : NSPredicate]?](./samplepredicates.md)
  A dictionary whose keys are [`HKSampleType`](../hksampletype.md) instances and whose values are [`NSPredicate`](../../Foundation/nspredicate.md) instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcorrelationquery/correlationtype)*