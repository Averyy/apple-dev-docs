# removeSubrange(_:)

**Framework**: Foundation  
**Kind**: method

Removes the elements in the specified subrange from the collection.

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
mutating func removeSubrange(_ bounds: Range<Self.Index>)
```

#### Discussion

All the elements following the specified position are moved to close the gap. This example removes three elements from the middle of an array of measurements.

```None
var measurements = [1.2, 1.5, 2.9, 1.2, 1.5]
measurements.removeSubrange(1..<4)
print(measurements)
// Prints "[1.2, 1.5]"
```

Calling this method may invalidate any existing indices for use with this collection.

> **Note**: O(), where  is the length of the collection.

O(), where  is the length of the collection.

## Parameters

- `bounds`: The range of the collection to be removed. The   bounds of the range must be valid indices of the collection.

## See Also

- [func remove(at: Self.Index) -> Self.Element](data/remove(at:).md)
  Removes and returns the element at the specified position.
- [func removeAll(keepingCapacity: Bool)](data/removeall(keepingcapacity:).md)
  Removes all elements from the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/removesubrange(_:)-8ohtp)*