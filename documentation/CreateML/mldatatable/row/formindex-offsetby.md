# formIndex(_:offsetBy:)

**Framework**: Create ML  
**Kind**: method

Offsets the given index by the specified distance.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func formIndex(_ i: inout Self.Index, offsetBy distance: Int)
```

#### Discussion

The value passed as `distance` must not offset `i` beyond the bounds of the collection.

> **Note**: O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(), where  is the absolute value of `distance`.

## Parameters

- `i`: A valid index of the collection.
- `distance`: The distance to offset  .   must not be negative   unless the collection conforms to the    protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/row/formindex(_:offsetby:))*