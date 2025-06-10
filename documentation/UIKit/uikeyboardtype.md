# UIKeyboardType

**Framework**: UIKit  
**Kind**: enum

Constants that specify the type of keyboard to display for a text-based view.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum UIKeyboardType
```

#### Overview

Use these constants with the [`keyboardType`](uitextinputtraits/keyboardtype.md) property.

## Topics

### Constants
- [UIKeyboardType.default](uikeyboardtype/default.md)
  Specifies the default keyboard for the current input method.
- [UIKeyboardType.asciiCapable](uikeyboardtype/asciicapable.md)
  Specifies a keyboard that displays standard ASCII characters.
- [UIKeyboardType.numbersAndPunctuation](uikeyboardtype/numbersandpunctuation.md)
  Specifies the numbers and punctuation keyboard.
- [UIKeyboardType.URL](uikeyboardtype/url.md)
  Specifies a keyboard for URL entry.
- [UIKeyboardType.numberPad](uikeyboardtype/numberpad.md)
  Specifies a numeric keypad for PIN entry.
- [UIKeyboardType.phonePad](uikeyboardtype/phonepad.md)
  Specifies a keypad for entering telephone numbers.
- [UIKeyboardType.namePhonePad](uikeyboardtype/namephonepad.md)
  Specifies a keypad for entering a person’s name or phone number.
- [UIKeyboardType.emailAddress](uikeyboardtype/emailaddress.md)
  Specifies a keyboard for entering email addresses.
- [UIKeyboardType.decimalPad](uikeyboardtype/decimalpad.md)
  Specifies a keyboard with numbers and a decimal point.
- [UIKeyboardType.twitter](uikeyboardtype/twitter.md)
  Specifies a keyboard for Twitter text entry, with easy access to the at (”`@`”) and hash (”`#`”) characters.
- [UIKeyboardType.webSearch](uikeyboardtype/websearch.md)
  Specifies a keyboard for web search terms and URL entry.
- [UIKeyboardType.asciiCapableNumberPad](uikeyboardtype/asciicapablenumberpad.md)
  Specifies a number pad that outputs only ASCII digits.
- [static var alphabet: UIKeyboardType](uikeyboardtype/alphabet.md)
  Specifies a keyboard for alphabetic entry.
### Initializers
- [init?(rawValue: Int)](uikeyboardtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var keyboardType: UIKeyboardType](uitextinputtraits/keyboardtype.md)
  The keyboard type for the text object.
- [var keyboardAppearance: UIKeyboardAppearance](uitextinputtraits/keyboardappearance.md)
  The appearance style of the keyboard for the text object.
- [enum UIKeyboardAppearance](uikeyboardappearance.md)
  Constants that specify the appearance of the keyboard for a text-based view.
- [var returnKeyType: UIReturnKeyType](uitextinputtraits/returnkeytype.md)
  The visible indication of what the Return key does.
- [enum UIReturnKeyType](uireturnkeytype.md)
  Constants that specify the type of Return key the keyboard displays.
- [var textContentType: UITextContentType!](uitextinputtraits/textcontenttype.md)
  The semantic meaning for a text input area.
- [struct UITextContentType](uitextcontenttype.md)
  Constants that identify the semantic meaning for a text-entry area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uikeyboardtype)*