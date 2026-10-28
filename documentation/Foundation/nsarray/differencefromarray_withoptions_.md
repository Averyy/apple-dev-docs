# differenceFromArray:withOptions:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Compares two arrays, with options, to create a difference object that represents the changes between them.

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
- (NSOrderedCollectionDifference<id> *) differenceFromArray:(NSArray<id> *) other withOptions:(NSOrderedCollectionDifferenceCalculationOptions) options;
```

## Discussion

The difference method creates the difference object by comparing objects within the arrays with the `isEqual:` method.

The options allow you to choose to omit insertion or removal references to the change objects within the difference object. You can also choose to infer moves when computing the difference, which provides an [`associatedIndex`](../nsorderedcollectionchange/associatedindex.md) within the change objects that indicates the index in the array where the object moved from.

The following example computes the difference between two arrays, inferring moves between them:

```objc
NSArray *original = @[@"Red", @"Green", @"Blue"];
NSArray *modified = @[@"Red", @"Blue", @"Green"];

NSOrderedCollectionDifference *diff = [original
                                       differenceFromArray:modified
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

### Comparing with Another Array
- [- differenceFromArray:](./differencefromarray_.md)
  Compares two arrays to create a difference object that represents the changes between them.
- [- differenceFromArray:withOptions:usingEquivalenceTest:](./differencefromarray_withoptions_usingequivalencetest_.md)
  Compares two arrays, using the provided block and with options, to create a difference object that represents the changes between them.
- [class NSOrderedCollectionDifference](../nsorderedcollectiondifference.md)
  An object representing the difference between two ordered collections.
- [struct NSOrderedCollectionDifferenceCalculationOptions](../nsorderedcollectiondifferencecalculationoptions.md)
  Constants that specify the options to use when creating an ordered collection difference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/differencefromarray:withoptions:)*