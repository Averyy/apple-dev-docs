# AXBrailleTranslationResult

**Framework**: Accessibility  
**Kind**: class

The result of translation or back-translation.

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
class AXBrailleTranslationResult
```

## Topics

### Instance Properties
- [var resultString: String](axbrailletranslationresult/resultstring.md)
  The resulting string after translation or back-translation.
### Instance Methods
- [func inputIndex(forResultIndex: String.Index) -> String.Index?](axbrailletranslationresult/inputindex(forresultindex:).md)
  Maps a location in the resultString to where it came from in the input string.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Braille displays](braille-displays.md)
  Display a graphical representation of images, icons, data, and more on a two-dimensional braille display.
- [class AXBrailleTable](axbrailletable.md)
  A rule for translating print text to Braille, and back-translating Braille to print text.
- [class AXBrailleTranslator](axbrailletranslator.md)
  Translates print text to Braille and Braille to print text according to the given Braille table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axbrailletranslationresult)*