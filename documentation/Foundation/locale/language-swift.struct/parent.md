# parent

**Framework**: Foundation  
**Kind**: property

The parent language of this language, if available.

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
var parent: Locale.Language? { get }
```

#### Discussion

For example, the parent language of `en_US_POSIX` is `en_US`.

If the system can’t determine a parent language, this value is `nil`.

## See Also

- [func hasCommonParent(with: Locale.Language) -> Bool](locale/language-swift.struct/hascommonparent(with:).md)
  Returns a Boolean value that indicates if the given language shares a common parent with this language.
- [func isEquivalent(to: Locale.Language) -> Bool](locale/language-swift.struct/isequivalent(to:).md)
  Returns a Boolean value that indicates whether this language and another language are equivalent after expanding missing components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/language-swift.struct/parent)*