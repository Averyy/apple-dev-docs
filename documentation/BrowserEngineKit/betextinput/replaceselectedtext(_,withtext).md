# replaceSelectedText(_:withText:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Replaces text with new text, either within the current selection or near the cursor.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func replaceSelectedText(_ text: String, withText replacementText: String)
```

```objc
- (void) replaceSelectedText:(NSString *) text withText:(NSString *) replacementText;
```

## Mentions

- [Integrating custom browser text views with UIKit](../integrating-custom-browser-text-views-with-uikit.md)

#### Discussion

This method’s behavior depends on the current selection state:

- If text is selected, this method replaces occurrences of `text` within the selection with `replacementText`.
- If the cursor is positioned without a selection, this method searches for `text` immediately before the cursor and replaces it with `replacementText`.
- If the cursor is at the start of an editable element, this method searches for `text` immediately after the cursor instead.

## Parameters

- `text`: The text to find and replace.
- `replacementText`: The text to insert in place of the found text.

## See Also

### Inserting and replacing text
- [func insert(BETextSuggestion)](./insert%28_%29-5iryn.md)
  Inserts a text suggestion in response to a suggestion selection.
- [func insert(BETextAlternatives)](./insert%28_%29-6x7hd.md)
  Inserts the given text or one of the available alternatives.
- [func replaceDictatedText(String, withText: String)](./replacedictatedtext%28_,withtext%29.md)
  Replaces the specified text for the text of a dictation.
- [func add(BETextAlternatives)](./add%28_%29.md)
  Adds text alternatives to the text input object for the current selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/replaceselectedtext(_:withtext:))*