# differenceFromOrderedSet:withOptions:usingEquivalenceTest:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Compares two ordered sets, using the provided block and with options, to create a difference object that represents the changes between them.

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
- (NSOrderedCollectionDifference<id> *) differenceFromOrderedSet:(NSOrderedSet<id> *) other withOptions:(NSOrderedCollectionDifferenceCalculationOptions) options usingEquivalenceTest:(BOOL (^)(ObjectType obj1, ObjectType obj2)) block;
```

## Discussion

The options allow you to choose to omit insertion or removal references to the change objects within the difference object’s changes. Don’t use the option [`inferMoves`](../nsorderedcollectiondifferencecalculationoptions/infermoves.md) when providing a block for the equivalence test. The changes returned in the difference object don’t include valid values for [`associatedIndex`](../nsorderedcollectionchange/associatedindex.md).

## See Also

### Comparing with Another Set
- [- differenceFromOrderedSet:](./differencefromorderedset_.md)
  Compares two ordered sets to create a difference object that represents the changes between them.
- [- differenceFromOrderedSet:withOptions:](./differencefromorderedset_withoptions_.md)
  Compares two ordered sets, with options, to create a difference object that represents the changes between them.
- [class NSOrderedCollectionDifference](../nsorderedcollectiondifference.md)
  An object representing the difference between two ordered collections.
- [struct NSOrderedCollectionDifferenceCalculationOptions](../nsorderedcollectiondifferencecalculationoptions.md)
  Constants that specify the options to use when creating an ordered collection difference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedset/differencefromorderedset:withoptions:usingequivalencetest:)*