# dropLast(_:)

**Framework**: Createmlcomponents  
**Kind**: method

Returns a sequence containing all but the given number of final elements.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
func dropLast(_ k: Int = 1) -> [Self.Element]
```

#### Return Value

A sequence leaving off the specified number of elements.

#### Discussion

The sequence must be finite. If the number of elements to drop exceeds the number of elements in the sequence, the result is an empty sequence.

```None
let numbers = [1, 2, 3, 4, 5]
print(numbers.dropLast(2))
// Prints "[1, 2, 3]"
print(numbers.dropLast(10))
// Prints "[]"
```

> **Note**: O(), where  is the length of the sequence.

## Parameters

- `n`: The number of elements to drop off the end of the   sequence.   must be greater than or equal to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/timeseriesforecasterbatches/droplast(_:))*