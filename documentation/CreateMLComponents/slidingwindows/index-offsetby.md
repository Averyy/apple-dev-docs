# index(_:offsetBy:)

**Framework**: Create ML Components  
**Kind**: method

Returns an index that is the specified distance from the given index.

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
func index(_ i: Int, offsetBy distance: Int) -> Int
```

#### Return Value

An index offset by `distance` from the index `i`.

#### Discussion

The value passed as `distance` must not offset `i` beyond the bounds of the collection.

## Parameters

- `i`: A valid index of the collection.
- `distance`: The distance to offset  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/slidingwindows/index(_:offsetby:))*