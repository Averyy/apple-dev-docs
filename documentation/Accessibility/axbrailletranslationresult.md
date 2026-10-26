# AXBrailleTranslationResult

**Framework**: Accessibility  
**Kind**: class  
**Role**: Class

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

```objc
@interface AXBrailleTranslationResult : NSObject
```

## Topics

### Initializers
- [init?(coder: NSCoder)](./axbrailletranslationresult/init%28coder%29.md)
### Instance Properties
- [var resultString: String](./axbrailletranslationresult/resultstring.md)
  The resulting string after translation or back-translation.
- [locationMap](./axbrailletranslationresult/locationmap.md)
  An array of integers that has the same length as the resultString. locationMap[i]-th character in the input string corresponds to resultString[i].
### Instance Methods
- [func inputIndex(forResultIndex: String.Index) -> String.Index?](./axbrailletranslationresult/inputindex%28forresultindex%29.md)
  Maps a location in the resultString to where it came from in the input string.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Braille
- [Braille displays](./braille-displays.md)
  Display a graphical representation of images, icons, data, and more on a two-dimensional braille display.
- [class AXBrailleTable](./axbrailletable.md)
  A rule for translating print text to Braille, and back-translating Braille to print text.
- [class AXBrailleTranslator](./axbrailletranslator.md)
  Translates print text to Braille and Braille to print text according to the given Braille table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axbrailletranslationresult)*