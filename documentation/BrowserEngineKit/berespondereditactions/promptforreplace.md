# promptForReplace(_:)

**Framework**: BrowserEngineKit  
**Kind**: method

Shows potential replacements for the selected content.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
optional func promptForReplace(_ sender: Any?)
```

#### Overview

To present the standard operating system UI for this action, call [`showReplacements(forText:)`](betextinteraction/showreplacements(fortext:).md) in your implementation of this method.

## Parameters

- `sender`: The object calling this method.

## See Also

- [func findSelected(Any?)](berespondereditactions/findselected(_:).md)
  Begins a search for the selected content in your browser text view.
- [func replace(Any?)](berespondereditactions/replace(_:).md)
  Removes the selected text and inputs the chosen replacement text.
- [func addShortcut(Any?)](berespondereditactions/addshortcut(_:).md)
  Adds a text-replacement shortcut to the edit dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/berespondereditactions/promptforreplace(_:))*