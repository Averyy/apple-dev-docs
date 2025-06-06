# addShortcut(_:)

**Framework**: BrowserEngineKit  
**Kind**: method

Adds a text-replacement shortcut to the edit dictionary.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
optional func addShortcut(_ sender: Any?)
```

#### Overview

To present the standard operating system UI for adding text-replacement shortcuts, call [`addShortcut(forText:from:)`](betextinteraction/addshortcut(fortext:from:).md) in your implementation of this method.

## Parameters

- `sender`: The object calling this method.

## See Also

- [func findSelected(Any?)](berespondereditactions/findselected(_:).md)
  Begins a search for the selected content in your browser text view.
- [func promptForReplace(Any?)](berespondereditactions/promptforreplace(_:).md)
  Shows potential replacements for the selected content.
- [func replace(Any?)](berespondereditactions/replace(_:).md)
  Removes the selected text and inputs the chosen replacement text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/berespondereditactions/addshortcut(_:))*