# AXBrailleTranslator

**Framework**: Accessibility  
**Kind**: class  
**Role**: Class

Translates print text to Braille and Braille to print text according to the given Braille table.

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
class AXBrailleTranslator
```

```objc
@interface AXBrailleTranslator : NSObject
```

## Topics

### Initializers
- [init(brailleTable: AXBrailleTable)](./axbrailletranslator/init%28brailletable%29.md)
### Instance Methods
- [func backTranslateBraille(String) -> AXBrailleTranslationResult](./axbrailletranslator/backtranslatebraille%28_%29.md)
  Input Braille should use the unicode Braille characters (0x2800-0x28FF).
- [func translatePrintText(String) -> AXBrailleTranslationResult](./axbrailletranslator/translateprinttext%28_%29.md)
  Output Braille uses the unicode Braille characters (0x2800-0x28FF).

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Braille
- [Braille displays](./braille-displays.md)
  Display a graphical representation of images, icons, data, and more on a two-dimensional braille display.
- [class AXBrailleTable](./axbrailletable.md)
  A rule for translating print text to Braille, and back-translating Braille to print text.
- [class AXBrailleTranslationResult](./axbrailletranslationresult.md)
  The result of translation or back-translation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axbrailletranslator)*