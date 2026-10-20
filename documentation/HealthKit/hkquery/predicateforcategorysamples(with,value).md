# predicateForCategorySamples(with:value:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Type Method

Returns a predicate that checks a category sample’s value.

**Availability**:
- iOS 8.0+ - Deprecated in 27.2
- iPadOS 8.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use [`predicateForSamples(_:value:)`](../hkcategoryvaluepredicateproviding/predicateforsamples%28_,value%29.md) instead.

## Declaration

```swift
class func predicateForCategorySamples(with operatorType: NSComparisonPredicate.Operator, value: Int) -> NSPredicate
```

```objc
+ (NSPredicate *) predicateForCategorySamplesWithOperatorType:(NSPredicateOperatorType) operatorType value:(NSInteger) value;
```

#### Return Value

A predicate that matches category samples based on the provided expression. This predicate works only with category samples.

#### Discussion

Use this convenience method to create a predicate that checks a category sample’s value. The following listing uses both the convenience method and a predicate format string to create equivalent predicates.

**Swift**:

```swift
let asleep = HKQuery.predicateForCategorySamplesWithOperatorType(
    .EqualToPredicateOperatorType,
    value: HKCategoryValueSleepAnalysis.Asleep.rawValue)
 
let explicitAsleep =
    NSPredicate(format: "%K == %d",
                HKPredicateKeyPathCategoryValue,
                HKCategoryValueSleepAnalysis.Asleep.rawValue)
```

**Objective-C**:

```objc
NSPredicate *asleep =
    [HKQuery
     predicateForCategorySamplesWithOperatorType:NSEqualToPredicateOperatorType
     value:HKCategoryValueSleepAnalysisAsleep];
 
NSPredicate *explicitAsleep =
    [NSPredicate predicateWithFormat:@"%K == %d",
     HKPredicateKeyPathCategoryValue,
     HKCategoryValueSleepAnalysisAsleep];
```

## Parameters

- `operatorType`: The type of operation to perform when matching the category sample’s value against the target value. For a list of possible operators, see [`NSComparisonPredicate.Operator.contains`](../../Foundation/nscomparisonpredicate/operator/contains.md).
- `value`: The category sample’s target value. Use an enumeration value appropriate for the type of category samples you are working with. For example, a predicate for sleep analysis samples use values from the [`HKCategoryValueSleepAnalysis`](../hkcategoryvaluesleepanalysis.md) enumeration.

## See Also

### Related Documentation
- [var value: Int](../hkcategorysample/value.md)
  The category value for this sample.
- [let HKPredicateKeyPathCategoryValue: String](../hkpredicatekeypathcategoryvalue.md)
  The key path for accessing the category sample’s value.
### Creating category sample predicates
- [protocol HKCategoryValuePredicateProviding](../hkcategoryvaluepredicateproviding.md)
  A protocol for objects that produce predicates that match category value samples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery/predicateforcategorysamples(with:value:))*