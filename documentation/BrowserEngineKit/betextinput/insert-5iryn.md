# insert(_:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Required**: Yes

Inserts a text suggestion in response to a suggestion selection.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func insert(_ textSuggestion: BETextSuggestion)
```

## Mentions

- [Integrating custom browser text views with UIKit](integrating-custom-browser-text-views-with-uikit.md)

#### Discussion

The system calls this method to suggest text-view insertions, for example, for AutoFill credentials.

## Parameters

- `textSuggestion`: The suggestion to insert.

## See Also

- [func insert(BETextAlternatives)](betextinput/insert(_:)-6x7hd.md)
  Inserts the given text or one of the available alternatives.
- [func replaceSelectedText(String, withText: String)](betextinput/replaceselectedtext(_:withtext:).md)
  Replaces text with new text, either within the current selection or near the cursor.
- [func replaceDictatedText(String, withText: String)](betextinput/replacedictatedtext(_:withtext:).md)
  Replaces the specified text for the text of a dictation.
- [func add(BETextAlternatives)](betextinput/add(_:).md)
  Adds text alternatives to the text input object for the current selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/insert(_:)-5iryn)*