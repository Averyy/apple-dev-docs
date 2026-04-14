# BEExtendedTextInputTraits

**Framework**: BrowserEngineKit  
**Kind**: protocol

An object that customizes text-input appearance and behavior beyond the standard system traits.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
protocol BEExtendedTextInputTraits : UITextInputTraits
```

#### Overview

This class extends the standard text input traits to control cursor and selection colors, as well as single-line mode and typing adaptation in web content.

## Topics

### Customizing text input visuals
- [var insertionPointColor: UIColor?](beextendedtextinputtraits/insertionpointcolor.md)
  A color for the text cursor at the insertion point.
- [var selectionHandleColor: UIColor?](beextendedtextinputtraits/selectionhandlecolor.md)
  A color that customizes the look of the handle.
- [var selectionHighlightColor: UIColor?](beextendedtextinputtraits/selectionhighlightcolor.md)
  The highlight color of a rectangle.
### Customizing text input behavior
- [var isSingleLineDocument: Bool](beextendedtextinputtraits/issinglelinedocument.md)
  A Boolean value that represents whether the active web input field is a single line document.
- [var isTypingAdaptationEnabled: Bool](beextendedtextinputtraits/istypingadaptationenabled.md)
  A Boolean value that controls whether the system learns new words and corrections.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [UITextInputTraits](../UIKit/UITextInputTraits.md)

## See Also

- [struct BEDirectionalTextRange](bedirectionaltextrange.md)
  Modifications to text length based on its offset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/beextendedtextinputtraits)*