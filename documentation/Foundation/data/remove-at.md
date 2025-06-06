# remove(at:)

**Framework**: Foundation  
**Kind**: method

Removes and returns the element at the specified position.

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
@discardableResult
mutating func remove(at position: Self.Index) -> Self.Element
```

#### Return Value

The removed element.

#### Discussion

All the elements following the specified position are moved to close the gap. This example removes the middle element from an array of measurements.

```None
var measurements = [1.2, 1.5, 2.9, 1.2, 1.6]
let removed = measurements.remove(at: 2)
print(measurements)
// Prints "[1.2, 1.5, 1.2, 1.6]"
```

Calling this method may invalidate any existing indices for use with this collection.

> **Note**: O(), where  is the length of the collection.

O(), where  is the length of the collection.

## Parameters

- `position`: The position of the element to remove.    must be a valid index of the collection that is not equal to the   collection’s end index.

## See Also

- [func removeAll(keepingCapacity: Bool)](data/removeall(keepingcapacity:).md)
  Removes all elements from the collection.
- [func removeSubrange(Range<Self.Index>)](data/removesubrange(_:)-8ohtp.md)
  Removes the elements in the specified subrange from the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/remove(at:))*