# requestTextRects(for:withCompletionHandler:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Gathers context for the presentation of a text-related user interface.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func requestTextRects(for input: String, withCompletionHandler completionHandler: @escaping @Sendable ([UITextSelectionRect]) -> Void)
```

```swift
func requestTextRects(for input: String) async -> [UITextSelectionRect]
```

```objc
- (void) requestTextRectsForString:(NSString *) input withCompletionHandler:(void (^)(NSArray<UITextSelectionRect *> *rects)) completionHandler;
```

## Discussion

The system invokes your implementation of this method. The completion handler receives [`UITextSelectionRect`](../../UIKit/uitextselectionrect.md) instances for the substring nearest to the caret that matches the given `input`.

## See Also

### Requesting context
- [func requestDocumentContext(BETextDocumentRequest, completionHandler: (BETextDocumentContext) -> Void)](./requestdocumentcontext%28_,completionhandler%29.md)
  Gathers context for the system about the current document.
- [func requestTextContextForAutocorrection(completionHandler: (BETextDocumentContext) -> Void)](./requesttextcontextforautocorrection%28completionhandler%29.md)
  A method the text system calls to get extra information for autocorrection suggestions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/requesttextrects(for:withcompletionhandler:))*