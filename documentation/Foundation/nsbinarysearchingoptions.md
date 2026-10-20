# NSBinarySearchingOptions

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

Options for searches and insertions using [`index(of:inSortedRange:options:usingComparator:)`](./nsarray/index%28of,insortedrange,options,usingcomparator%29.md).

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

```c
enum NSBinarySearchingOptions : NSUInteger;
```

## Topics

### Constants
- [static var firstEqual: NSBinarySearchingOptions](./nsbinarysearchingoptions/firstequal.md)
  Specifies that the search should return the first object in the range that is equal to the given object.
- [static var lastEqual: NSBinarySearchingOptions](./nsbinarysearchingoptions/lastequal.md)
  Specifies that the search should return the last object in the range that is equal to the given object.
- [static var insertionIndex: NSBinarySearchingOptions](./nsbinarysearchingoptions/insertionindex.md)
  Returns the index at which you should insert the object in order to maintain a sorted array.
### Initializers
- [init(rawValue: UInt)](./nsbinarysearchingoptions/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsbinarysearchingoptions)*