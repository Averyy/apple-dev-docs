# makeCharacterIterator()

**Framework**: Swift  
**Kind**: method

Returns an iterator that will construct `Character`s from the underlying UTF-8 content.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func makeCharacterIterator() -> UTF8Span.CharacterIterator
```

#### Discussion

The resulting iterator has the same lifetime constraints as `self`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/utf8span/makecharacteriterator())*