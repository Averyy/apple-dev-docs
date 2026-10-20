# add(_:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (void) addTextAlternatives:(BETextAlternatives *) alternatives;
```

## Mentions

- [Integrating custom browser text views with UIKit](../integrating-custom-browser-text-views-with-uikit.md)

## See Also

### Inserting and replacing text
- [func insert(BETextSuggestion)](./insert%28_%29-5iryn.md)
  Inserts a text suggestion in response to a suggestion selection.
- [func insert(BETextAlternatives)](./insert%28_%29-6x7hd.md)
  Inserts the given text or one of the available alternatives.
- [func replaceSelectedText(String, withText: String)](./replaceselectedtext%28_,withtext%29.md)
  Replaces text with new text, either within the current selection or near the cursor.
- [func replaceDictatedText(String, withText: String)](./replacedictatedtext%28_,withtext%29.md)
  Replaces the specified text for the text of a dictation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/add(_:))*