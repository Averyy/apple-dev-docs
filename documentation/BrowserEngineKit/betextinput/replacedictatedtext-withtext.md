# replaceDictatedText(_:withText:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Required**: Yes

Replaces the specified text for the text of a dictation.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func replaceDictatedText(_ oldText: String, withText newText: String)
```

## See Also

- [func insert(BETextSuggestion)](betextinput/insert(_:)-5iryn.md)
  Inserts a text suggestion in response to a suggestion selection.
- [func insert(BETextAlternatives)](betextinput/insert(_:)-6x7hd.md)
  Inserts the given text or one of the available alternatives.
- [func replaceSelectedText(String, withText: String)](betextinput/replaceselectedtext(_:withtext:).md)
  Replaces text with new text, either within the current selection or near the cursor.
- [func add(BETextAlternatives)](betextinput/add(_:).md)
  Adds text alternatives to the text input object for the current selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/replacedictatedtext(_:withtext:))*