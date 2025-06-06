# replaceSelectedText(_:withText:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Required**: Yes

Replaces the specified `text` with `replacementText`

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func replaceSelectedText(_ text: String, withText replacementText: String)
```

## Mentions

- [Integrating custom browser text views with UIKit](integrating-custom-browser-text-views-with-uikit.md)

#### Discussion

1. If there is a nonzero length current selection, then replace text with replacementText.
2. If there is zero length current selection, then replace the matching word before the selection
3. If the zero length selection is at the start of the element, then replace the matching word after the selection

Replaces the specified text with another string.

#### Overview

Your implementation of this method needs to vary its behavior based on the current text selection.

- If the selection has `0` length and is at the start of the document, replace the matching word after the selection.
- If the selection has `0` length and is anywhere else in the document, replace the matching word before the selection.
- Otherwise, replace the selected text.

## Parameters

- `text`: The text to replace.
- `replacementText`: The new text to use as the replacement.

## See Also

- [var isReplaceAllowed: Bool](betextinput/isreplaceallowed.md)
  Returns whether replacement should be allowed for an editable element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/replaceselectedtext(_:withtext:))*