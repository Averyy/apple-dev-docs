# requestDocumentContext(_:completionHandler:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Gathers context for the system about the current document.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func requestDocumentContext(_ request: BETextDocumentRequest, completionHandler: @escaping @Sendable (BETextDocumentContext) -> Void)
```

```swift
func requestDocumentContext(_ request: BETextDocumentRequest) async -> BETextDocumentContext
```

```objc
- (void) requestDocumentContext:(BETextDocumentRequest *) request completionHandler:(void (^)(BETextDocumentContext *)) completionHandler;
```

## See Also

### Requesting context
- [func requestTextContextForAutocorrection(completionHandler: (BETextDocumentContext) -> Void)](./requesttextcontextforautocorrection%28completionhandler%29.md)
  A method the text system calls to get extra information for autocorrection suggestions.
- [func requestTextRects(for: String, withCompletionHandler: ([UITextSelectionRect]) -> Void)](./requesttextrects%28for,withcompletionhandler%29.md)
  Gathers context for the presentation of a text-related user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/requestdocumentcontext(_:completionhandler:))*