# AXBrailleTranslator

**Framework**: Accessibility  
**Kind**: class

Translates print text to Braille and Braille to print text according to the given Braille table.

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
class AXBrailleTranslator
```

## Topics

### Initializers
- [init(brailleTable: AXBrailleTable)](axbrailletranslator/init(brailletable:).md)
### Instance Methods
- [func backTranslateBraille(String) -> AXBrailleTranslationResult](axbrailletranslator/backtranslatebraille(_:).md)
  Input Braille should use the unicode Braille characters (0x2800-0x28FF).
- [func translatePrintText(String) -> AXBrailleTranslationResult](axbrailletranslator/translateprinttext(_:).md)
  Output Braille uses the unicode Braille characters (0x2800-0x28FF).

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axbrailletranslator)*