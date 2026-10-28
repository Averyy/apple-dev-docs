# differenceFromOrderedSet:withOptions:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Compares two ordered sets, with options, to create a difference object that represents the changes between them.

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
- (NSOrderedCollectionDifference<id> *) differenceFromOrderedSet:(NSOrderedSet<id> *) other withOptions:(NSOrderedCollectionDifferenceCalculationOptions) options;
```

## Discussion

The difference method creates the difference object by comparing objects within the ordered sets with the `isEqual:` method.

The options allow you to choose to omit insertion or removal references to the change objects within the difference object. You can also choose to infer moves when computing the difference, which provides an [`associatedIndex`](../nsorderedcollectionchange/associatedindex.md) within the change objects that indicates the index in the ordered set where the object moved from.

The following example computes the difference between two ordered sets, inferring moves between them:

```objc
NSOrderedSet *original = [NSOrderedSet
                           orderedSetWithObjects:@"Red", @"Green", @"Blue", nil];
NSOrderedSet *modified = [NSOrderedSet
                           orderedSetWithObjects:@"Red", @"Blue", @"Green", nil];

NSOrderedCollectionDifference *diff = [original
                                       differenceFromOrderedSet:modified
                                       withOptions:NSOrderedCollectionDifferenceCalculationInferMoves];

// diff.hasChanges == TRUE
// diff.insertions.count == 1
// diff.removals.count == 1

// Inferring the moves adds an associatedIndex into the change.
NSOrderedCollectionChange* insertion = diff.insertions[0];
// insertion.index == 2
// insertion.associatedIndex == 1

NSOrderedCollectionChange* deletion = diff.removals[0];
// deletion.index == 1
// deletion.associatedIndex == 2

```

## See Also

### Comparing with Another Set
- [- differenceFromOrderedSet:](./differencefromorderedset_.md)
  Compares two ordered sets to create a difference object that represents the changes between them.
- [- differenceFromOrderedSet:withOptions:usingEquivalenceTest:](./differencefromorderedset_withoptions_usingequivalencetest_.md)
  Compares two ordered sets, using the provided block and with options, to create a difference object that represents the changes between them.
- [class NSOrderedCollectionDifference](../nsorderedcollectiondifference.md)
  An object representing the difference between two ordered collections.
- [struct NSOrderedCollectionDifferenceCalculationOptions](../nsorderedcollectiondifferencecalculationoptions.md)
  Constants that specify the options to use when creating an ordered collection difference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedset/differencefromorderedset:withoptions:)*