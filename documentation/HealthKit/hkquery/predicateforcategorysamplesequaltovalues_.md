# predicateForCategorySamplesEqualToValues:

**Framework**: HealthKit  
**Kind**: method  
**Role**: Type Method

A predicate that returns category samples with a matching value.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```objc
+ (NSPredicate *) predicateForCategorySamplesEqualToValues:(NSSet<NSNumber *> *) values;
```

#### Discussion

The following example creates a query for sleep analysis samples with the [`HKCategoryValueSleepAnalysis.asleepDeep`](../hkcategoryvaluesleepanalysis/asleepdeep.md) category value.

```objc
HKCategoryType *sleepType = [HKObjectType categoryTypeForIdentifier:HKCategoryTypeIdentifierSleepAnalysis];

NSPredicate *deepSleepPredicate =
[HKQuery predicateForCategorySamplesEqualToValues:
 [NSSet setWithObject:
  [NSNumber numberWithInt:HKCategoryValueSleepAnalysisAsleepDeep]]];

HKSampleQuery *query = [[HKSampleQuery alloc]
                        initWithSampleType:sleepType
                        predicate:deepSleepPredicate
                        limit:HKObjectQueryNoLimit
                        sortDescriptors:nil
                        resultsHandler:^(HKSampleQuery * _Nonnull query,
                                         NSArray<__kindof HKSample *> * _Nullable results,
                                         NSError * _Nullable error) {
    
    if (error != nil) {
        // Handle the error here.
        NSLog(@"*** An error occurred: %@ ***", error.localizedDescription);
        return;
    }
    
    // Do something with the results here.
    
}];

[store executeQuery:query];
```

> **Note**:  Because the category type is an integer, several different category types may share the same value. You’ll need to specify the category type that you’re interested in, either in the query or in an additional predicate.

## Parameters

- `values`: The category value to match. Each category type has a set of valid values. For more information about the category types, see [`HKCategoryTypeIdentifier`](../hkcategorytypeidentifier.md).

## See Also

### Creating category sample predicates
- [class func predicateForCategorySamples(with: NSComparisonPredicate.Operator, value: Int) -> NSPredicate](./predicateforcategorysamples%28with,value%29.md)
  Returns a predicate that checks a category sample’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery/predicateforcategorysamplesequaltovalues:)*