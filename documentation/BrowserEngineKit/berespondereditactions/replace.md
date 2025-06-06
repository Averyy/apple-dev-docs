# replace(_:)

**Framework**: BrowserEngineKit  
**Kind**: method

Removes the selected text and inputs the chosen replacement text.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
optional func replace(_ sender: Any?)
```

#### Overview

To invoke the standard operating system behavior for replacing text, call [`textInput(_:deferReplaceTextActionToSystem:)`](betextinputdelegate/textinput(_:deferreplacetextactiontosystem:).md) in your implementation of this method.

## Parameters

- `sender`: The object calling this method.

## See Also

- [func findSelected(Any?)](berespondereditactions/findselected(_:).md)
  Begins a search for the selected content in your browser text view.
- [func promptForReplace(Any?)](berespondereditactions/promptforreplace(_:).md)
  Shows potential replacements for the selected content.
- [func addShortcut(Any?)](berespondereditactions/addshortcut(_:).md)
  Adds a text-replacement shortcut to the edit dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/berespondereditactions/replace(_:))*