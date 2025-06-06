# AnnotatedFiles.Index

**Framework**: Create ML Components  
**Kind**: typealias

A type that represents a position in the collection.

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
typealias Index = Array<AnnotatedFiles.Element>.Index
```

#### Discussion

Valid indices consist of the position of every element and a “past the end” position that’s not valid for use as a subscript argument.

## See Also

- [func index(after: AnnotatedFiles.Index) -> AnnotatedFiles.Index](annotatedfiles/index(after:).md)
  Returns the position immediately after the given index.
- [AnnotatedFiles.Element](annotatedfiles/element.md)
  A type representing the sequence’s elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/annotatedfiles/index)*