# NSChangeSpelling

**Framework**: AppKit  
**Kind**: protocol

A protocol that responder objects can implement to correct a misspelled word.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSChangeSpelling
```

## Topics

### Changing spellings
- [func changeSpelling(Any?)](nschangespelling/changespelling(_:).md)
  Replaces the selected word in the receiver with a corrected version from the Spelling panel.

## Relationships

### Conforming Types
- [NSText](nstext.md)
- [NSTextView](nstextview.md)

## See Also

- [class NSSpellChecker](nsspellchecker.md)
  An interface to the Cocoa spell-checking service.
- [protocol NSIgnoreMisspelledWords](nsignoremisspelledwords.md)
  A protocol that enables the Ignore button in the Spelling panel to function properly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nschangespelling)*