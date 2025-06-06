# findSelected(_:)

**Framework**: BrowserEngineKit  
**Kind**: method

Begins a search for the selected content in your browser text view.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
optional func findSelected(_ sender: Any?)
```

#### Overview

UIKit calls this method when someone selects Use Selection for Find from an editing menu. Present the UI for finding text in your view, and use the selected text for the search. To present the standard operating system UI for finding text, and support standard keyboard shortcuts, add a [`UIFindInteraction`](https://developer.apple.com/documentation/UIKit/UIFindInteraction) to your browser text view.

## Parameters

- `sender`: The object calling this method.

## See Also

- [func promptForReplace(Any?)](berespondereditactions/promptforreplace(_:).md)
  Shows potential replacements for the selected content.
- [func replace(Any?)](berespondereditactions/replace(_:).md)
  Removes the selected text and inputs the chosen replacement text.
- [func addShortcut(Any?)](berespondereditactions/addshortcut(_:).md)
  Adds a text-replacement shortcut to the edit dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/berespondereditactions/findselected(_:))*