# subscript(_:)

**Framework**: Swift  
**Kind**: subscript

Accesses the element at the specified position.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
subscript(i: RangeSet<Bound>.Ranges.Index) -> RangeSet<Bound>.Ranges.Element { get }
```

#### Overview

The following example accesses an element of an array through its subscript to print its value:

```swift
var streets = ["Adams", "Bryant", "Channing", "Douglas", "Evarts"]
print(streets[1])
// Prints "Bryant"
```

You can subscript a collection with any valid index other than the collection’s end index. The end index refers to the position one past the last element of a collection, so it doesn’t correspond with an element.

> **Note**: O(1)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/rangeset/ranges-swift.struct/subscript(_:))*