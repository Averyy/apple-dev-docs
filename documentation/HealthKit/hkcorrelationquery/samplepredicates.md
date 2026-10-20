# samplePredicates

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

A dictionary whose keys are [`HKSampleType`](../hksampletype.md) instances and whose values are [`NSPredicate`](../../Foundation/nspredicate.md) instances.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var samplePredicates: [HKSampleType : NSPredicate]? { get }
```

```objc
@property (copy, readonly, nullable) NSDictionary<__kindof HKSampleType *,NSPredicate *> * samplePredicates;
```

#### Discussion

The query uses this dictionary to perform complex tests against the correlation’s contents. For more information, see [`init(type:predicate:samplePredicates:completion:)`](./init%28type,predicate,samplepredicates,completion%29.md).

## See Also

### Getting Property Data
- [var correlationType: HKCorrelationType](./correlationtype.md)
  The type of correlation to search for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcorrelationquery/samplepredicates)*