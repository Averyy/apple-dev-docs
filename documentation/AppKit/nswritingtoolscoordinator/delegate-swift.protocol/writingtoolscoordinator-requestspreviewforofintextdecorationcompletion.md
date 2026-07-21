# writingToolsCoordinator(_:requestsPreviewFor:of:in:textDecoration:completion:)

**Framework**: AppKit  
**Kind**: method

Asks the delegate for preview images for the specified text.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
optional func writingToolsCoordinator(_ writingToolsCoordinator: NSWritingToolsCoordinator, previewFor textAnimation: NSWritingToolsCoordinator.TextAnimation, range: NSRange, context: NSWritingToolsCoordinator.Context, textDecoration: NSWritingToolsCoordinator.TextDecoration) async -> [NSTextPreview]?
```

#### Discussion

To support grammar animation, the delegate should provide previews for the relevant text, as with the required `requestsPreviewFor` method, but in this case showing the text with the specified decoration applied. The grammar animation needs previews of the text of the issue in two forms, without and with the grammar indication underline applied. If you use grammar animation, you must implement this delegate method to provide them, based on the specified decoration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestspreviewfor:of:in:textdecoration:completion:))*