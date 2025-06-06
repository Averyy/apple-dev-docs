# suffix(_:)

**Framework**: System  
**Kind**: method

Returns a subsequence, up to the given maximum length, containing the final elements of the collection.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func suffix(_ maxLength: Int) -> Self.SubSequence
```

#### Return Value

A subsequence terminating at the end of the collection with at most `maxLength` elements.

#### Discussion

If the maximum length exceeds the number of elements in the collection, the result contains the entire collection.

```swift
let numbers = [1, 2, 3, 4, 5]
print(numbers.suffix(2))
// Prints "[4, 5]"
print(numbers.suffix(10))
// Prints "[1, 2, 3, 4, 5]"
```

> **Note**: O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(), where  is equal to `maxLength`.

O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(), where  is equal to `maxLength`.

## Parameters

- `maxLength`: The maximum number of elements to return.    must be greater than or equal to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepath/componentview/suffix(_:))*