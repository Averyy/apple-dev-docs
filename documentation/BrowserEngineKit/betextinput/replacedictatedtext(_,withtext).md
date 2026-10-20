# replaceDictatedText(_:withText:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (void) replaceDictatedText:(NSString *) oldText withText:(NSString *) newText;
```

## See Also

### Inserting and replacing text
- [func insert(BETextSuggestion)](./insert%28_%29-5iryn.md)
  Inserts a text suggestion in response to a suggestion selection.
- [func insert(BETextAlternatives)](./insert%28_%29-6x7hd.md)
  Inserts the given text or one of the available alternatives.
- [func replaceSelectedText(String, withText: String)](./replaceselectedtext%28_,withtext%29.md)
  Replaces text with new text, either within the current selection or near the cursor.
- [func add(BETextAlternatives)](./add%28_%29.md)
  Adds text alternatives to the text input object for the current selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/replacedictatedtext(_:withtext:))*