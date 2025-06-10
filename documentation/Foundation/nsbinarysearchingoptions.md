# NSBinarySearchingOptions

**Framework**: Foundation  
**Kind**: struct

Options for searches and insertions using [`index(of:inSortedRange:options:usingComparator:)`](nsarray/index(of:insortedrange:options:usingcomparator:).md).

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct NSBinarySearchingOptions
```

## Topics

### Constants
- [static var firstEqual: NSBinarySearchingOptions](nsbinarysearchingoptions/firstequal.md)
  Specifies that the search should return the first object in the range that is equal to the given object.
- [static var lastEqual: NSBinarySearchingOptions](nsbinarysearchingoptions/lastequal.md)
  Specifies that the search should return the last object in the range that is equal to the given object.
- [static var insertionIndex: NSBinarySearchingOptions](nsbinarysearchingoptions/insertionindex.md)
  Returns the index at which you should insert the object in order to maintain a sorted array.
### Initializers
- [init(rawValue: UInt)](nsbinarysearchingoptions/init(rawvalue:).md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsbinarysearchingoptions)*