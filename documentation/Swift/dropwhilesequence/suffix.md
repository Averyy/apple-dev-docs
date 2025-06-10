# suffix(_:)

**Framework**: Swift  
**Kind**: method

Returns a subsequence, up to the given maximum length, containing the final elements of the sequence.

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
func suffix(_ maxLength: Int) -> [Self.Element]
```

#### Discussion

The sequence must be finite. If the maximum length exceeds the number of elements in the sequence, the result contains all the elements in the sequence.

```swift
let numbers = [1, 2, 3, 4, 5]
print(numbers.suffix(2))
// Prints "[4, 5]"
print(numbers.suffix(10))
// Prints "[1, 2, 3, 4, 5]"
```

> **Note**: O(), where  is the length of the sequence.

## Parameters

- `maxLength`: The maximum number of elements to return. The   value of   must be greater than or equal to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dropwhilesequence/suffix(_:))*