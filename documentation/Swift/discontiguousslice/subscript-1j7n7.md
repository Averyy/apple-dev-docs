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
subscript(i: DiscontiguousSlice<Base>.Index) -> Base.Element { get set }
```

#### Overview

For example, you can replace an element of an array by using its subscript.

```swift
var streets = ["Adams", "Bryant", "Channing", "Douglas", "Evarts"]
streets[1] = "Butler"
print(streets[1])
// Prints "Butler"
```

You can subscript a collection with any valid index other than the collection’s end index. The end index refers to the position one past the last element of a collection, so it doesn’t correspond with an element.

> **Note**: O(1)

O(1)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/discontiguousslice/subscript(_:)-1j7n7)*