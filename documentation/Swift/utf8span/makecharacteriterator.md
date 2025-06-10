# makeCharacterIterator()

**Framework**: Swift  
**Kind**: method

Returns an iterator that will construct `Character`s from the underlying UTF-8 content.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
func makeCharacterIterator() -> UTF8Span.CharacterIterator
```

#### Discussion

The resulting iterator has the same lifetime constraints as `self`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/utf8span/makecharacteriterator())*