# index(after:)

**Framework**: Create ML Components  
**Kind**: method

Returns the position immediately after the given index.

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
func index(after i: AnnotatedFiles.Index) -> AnnotatedFiles.Index
```

#### Return Value

The index value immediately after `i`.

#### Discussion

The successor of an index must be well defined. For an index `i` into a collection `c`, calling `c.index(after: i)` returns the same index every time.

## Parameters

- `i`: A valid index of the collection.   must be less than   .

## See Also

- [AnnotatedFiles.Index](annotatedfiles/index.md)
  A type that represents a position in the collection.
- [AnnotatedFiles.Element](annotatedfiles/element.md)
  A type representing the sequence’s elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/annotatedfiles/index(after:))*