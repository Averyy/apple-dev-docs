# NSOrderedCollectionDifferenceCalculationOptions

**Framework**: Foundation  
**Kind**: struct

Constants that specify the options to use when creating an ordered collection difference.

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
struct NSOrderedCollectionDifferenceCalculationOptions
```

## Topics

### Creating Difference Calculation Options
- [init(rawValue: UInt)](nsorderedcollectiondifferencecalculationoptions/init(rawvalue:).md)
  Creates a set of difference calculation options.
### Difference Calculation Options
- [static var inferMoves: NSOrderedCollectionDifferenceCalculationOptions](nsorderedcollectiondifferencecalculationoptions/infermoves.md)
  An option that identifies insertions or removals as moves.
- [static var omitInsertedObjects: NSOrderedCollectionDifferenceCalculationOptions](nsorderedcollectiondifferencecalculationoptions/omitinsertedobjects.md)
  An option that indicates that the difference should omit references to the insertions.
- [static var omitRemovedObjects: NSOrderedCollectionDifferenceCalculationOptions](nsorderedcollectiondifferencecalculationoptions/omitremovedobjects.md)
  An option that indicates that the difference should omit references to the removals.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [class NSOrderedCollectionDifference](nsorderedcollectiondifference.md)
  An object representing the difference between two ordered collections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedcollectiondifferencecalculationoptions)*