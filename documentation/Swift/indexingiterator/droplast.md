# dropLast(_:)

**Framework**: Swift  
**Kind**: method

Returns a sequence containing all but the given number of final elements.

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
func dropLast(_ k: Int = 1) -> [Self.Element]
```

#### Return Value

A sequence leaving off the specified number of elements.

#### Discussion

The sequence must be finite. If the number of elements to drop exceeds the number of elements in the sequence, the result is an empty sequence.

```swift
let numbers = [1, 2, 3, 4, 5]
print(numbers.dropLast(2))
// Prints "[1, 2, 3]"
print(numbers.dropLast(10))
// Prints "[]"
```

> **Note**: O(), where  is the length of the sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/indexingiterator/droplast(_:))*