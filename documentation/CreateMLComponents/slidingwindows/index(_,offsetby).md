# index(_:offsetBy:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

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

## Return Value

An index offset by `distance` from the index `i`.

## Discussion

The value passed as `distance` must not offset `i` beyond the bounds of the collection.

## Parameters

- `i`: A valid index of the collection.
- `distance`: The distance to offset `i`.

## See Also

### Getting the index
- [func index(after: Int) -> Int](./index%28after%29.md)
  Returns the position immediately after the given index.
- [func index(before: Int) -> Int](./index%28before%29.md)
  Returns the position immediately before the given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/slidingwindows/index(_:offsetby:))*