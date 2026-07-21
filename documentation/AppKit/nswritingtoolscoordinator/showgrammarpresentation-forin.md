# showGrammarPresentation(for:in:)

**Framework**: AppKit  
**Kind**: method

Used to support the presentation of grammar issues in text. When the user interacts with an issue, call this to bring up the relevant UI.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func showGrammarPresentation(for range: NSRange, in context: NSWritingToolsCoordinator.Context) -> Bool
```

#### Discussion

Pass in context and range to identify the issue the user selected. Returns NO if the UI cannot be brought up.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/showgrammarpresentation(for:in:))*