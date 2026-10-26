# arrayByApplyingDifference:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Creates a new array by applying a difference object to an existing array.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```objc
- (NSArray<id> *) arrayByApplyingDifference:(NSOrderedCollectionDifference<id> *) difference;
```

#### Discussion

The following example computes the difference between two arrays, then applies the difference to create an array that duplicates the original:

```objc
NSArray *original = @[@"1", @"2"];
NSArray *modified = @[@"1", @"2", @"3"];

NSOrderedCollectionDifference *diff = [modified differenceFromArray:original];
// diff.hasChanges == true
// diff.insertions.count == 
// diff.removals.count == 0

NSArray *updated = [original arrayByApplyingDifference:diff];
// updated == [@"1", @"2", @"3"]

```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/arraybyapplyingdifference:)*