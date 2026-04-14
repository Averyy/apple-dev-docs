# replaceText(_:withText:options:completionHandler:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Required**: Yes

Replace the specified text preceding the current selection.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func replaceText(_ originalText: String, withText replacementText: String, options: BETextReplacementOptions = []) async -> [UITextSelectionRect]
```

#### Discussion

Completion handler should be invoked with the rects representing the replacementText.  If the replaceText could not be completed succesfully, such as when the originalText no longer matches the current text, then the completion handler should be invoked with an empty array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/replacetext(_:withtext:options:completionhandler:))*