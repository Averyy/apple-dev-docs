# index(after:)

**Framework**: Create ML  
**Kind**: method

Returns the position immediately after the given index.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func index(after i: MLDataValue.DictionaryType.Index) -> MLDataValue.DictionaryType.Index
```

#### Return Value

The index value immediately after `i`.

#### Discussion

The successor of an index must be well defined. For an index `i` into a collection `c`, calling `c.index(after: i)` returns the same index every time.

## Parameters

- `i`: A valid index of the collection.   must be less than   .


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatavalue/dictionarytype/index(after:))*