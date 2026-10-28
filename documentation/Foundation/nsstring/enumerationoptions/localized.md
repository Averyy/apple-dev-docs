# localized

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var localized: NSString.EnumerationOptions { get }
```

```c
NSStringEnumerationLocalized
```

## Discussion

Causes the enumeration to occur using the current locale. This does not make a difference in line, paragraph, or composed character sequence enumeration, but it may for words or sentences.

## See Also

### Constants
- [static var byLines: NSString.EnumerationOptions](./bylines.md)
- [static var byParagraphs: NSString.EnumerationOptions](./byparagraphs.md)
- [static var byComposedCharacterSequences: NSString.EnumerationOptions](./bycomposedcharactersequences.md)
- [static var byWords: NSString.EnumerationOptions](./bywords.md)
- [static var bySentences: NSString.EnumerationOptions](./bysentences.md)
- [static var reverse: NSString.EnumerationOptions](./reverse.md)
- [static var substringNotRequired: NSString.EnumerationOptions](./substringnotrequired.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/enumerationoptions/localized)*