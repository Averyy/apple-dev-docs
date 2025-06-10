# suffix(_:)

**Framework**: Foundation Models  
**Kind**: method

Returns a subsequence, up to the given maximum length, containing the final elements of the collection.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func suffix(_ maxLength: Int) -> Self.SubSequence
```

#### Return Value

A subsequence terminating at the end of the collection with at most `maxLength` elements.

#### Discussion

If the maximum length exceeds the number of elements in the collection, the result contains the entire collection.

```None
let numbers = [1, 2, 3, 4, 5]
print(numbers.suffix(2))
// Prints "[4, 5]"
print(numbers.suffix(10))
// Prints "[1, 2, 3, 4, 5]"
```

> **Note**: O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(), where  is equal to `maxLength`.

## Parameters

- `maxLength`: The maximum number of elements to return.    must be greater than or equal to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/toolcalls/suffix(_:))*