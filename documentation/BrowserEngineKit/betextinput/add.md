# add(_:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Required**: Yes

Adds text alternatives to the text input object for the current selection.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func add(_ alternatives: BETextAlternatives)
```

## Mentions

- [Integrating custom browser text views with UIKit](integrating-custom-browser-text-views-with-uikit.md)

## See Also

- [func insert(BETextSuggestion)](betextinput/insert(_:)-5iryn.md)
  Inserts a text suggestion in response to a suggestion selection.
- [func insert(BETextAlternatives)](betextinput/insert(_:)-6x7hd.md)
  Inserts the given text or one of the available alternatives.
- [func replaceSelectedText(String, withText: String)](betextinput/replaceselectedtext(_:withtext:).md)
  Replaces text with new text, either within the current selection or near the cursor.
- [func replaceDictatedText(String, withText: String)](betextinput/replacedictatedtext(_:withtext:).md)
  Replaces the specified text for the text of a dictation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/add(_:))*