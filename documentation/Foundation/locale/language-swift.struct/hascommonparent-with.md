# hasCommonParent(with:)

**Framework**: Foundation  
**Kind**: method

Returns a Boolean value that indicates if the given language shares a common parent with this language.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func hasCommonParent(with language: Locale.Language) -> Bool
```

#### Return Value

`true` if this language and language share a common parent; `false` otherwise.

## Parameters

- `language`: A language to compare parentage with.

## See Also

- [var parent: Locale.Language?](locale/language-swift.struct/parent.md)
  The parent language of this language, if available.
- [func isEquivalent(to: Locale.Language) -> Bool](locale/language-swift.struct/isequivalent(to:).md)
  Returns a Boolean value that indicates whether this language and another language are equivalent after expanding missing components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/language-swift.struct/hascommonparent(with:))*