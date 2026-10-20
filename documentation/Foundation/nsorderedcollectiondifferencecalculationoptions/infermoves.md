# inferMoves

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

An option that identifies insertions or removals as moves.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
static var inferMoves: NSOrderedCollectionDifferenceCalculationOptions { get }
```

```c
NSOrderedCollectionDifferenceCalculationInferMoves
```

#### Discussion

When you use the option to infer moves, the difference calculation adds an associated index to change objects to indicate the original positions of the objects.

## See Also

### Difference Calculation Options
- [static var omitInsertedObjects: NSOrderedCollectionDifferenceCalculationOptions](./omitinsertedobjects.md)
  An option that indicates that the difference should omit references to the insertions.
- [static var omitRemovedObjects: NSOrderedCollectionDifferenceCalculationOptions](./omitremovedobjects.md)
  An option that indicates that the difference should omit references to the removals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedcollectiondifferencecalculationoptions/infermoves)*