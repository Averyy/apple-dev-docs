# orderedSetByApplyingDifference:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Creates a new ordered set by applying a difference object to an existing ordered set.

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
- (NSOrderedSet<id> *) orderedSetByApplyingDifference:(NSOrderedCollectionDifference<id> *) difference;
```

## Discussion

The following example computes the difference between two ordered sets, then applies the difference to create an ordered set that duplicates the original:

```objc
NSOrderedSet *original = [NSOrderedSet orderedSetWithObjects:@"1", @"2", nil];
NSOrderedSet *modified = [NSOrderedSet orderedSetWithObjects:@"1", @"2", @"3", nil];

NSOrderedCollectionDifference *diff = [modified differenceFromOrderedSet:original];
// diff.hasChanges == true
// diff.insertions.count == 1
// diff.removals.count == 0

NSOrderedSet *updated = [original orderedSetByApplyingDifference:diff];
// updated == [@"1", @"2", @"3"]

```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedset/orderedsetbyapplyingdifference:)*