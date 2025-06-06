# remove(at:)

**Framework**: Swift  
**Kind**: method

Removes and returns the element at the specified position.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@discardableResult
mutating func remove(at index: Int) -> Element
```

#### Return Value

The element at the specified index.

#### Discussion

All the elements following the specified position are moved up to close the gap.

```swift
var measurements: [Double] = [1.1, 1.5, 2.9, 1.2, 1.5, 1.3, 1.2]
let removed = measurements.remove(at: 2)
print(measurements)
// Prints "[1.1, 1.5, 1.2, 1.5, 1.3, 1.2]"
```

> **Note**: O(), where  is the length of the array.

O(), where  is the length of the array.

## Parameters

- `index`: The position of the element to remove.   must   be a valid index of the array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/contiguousarray/remove(at:))*