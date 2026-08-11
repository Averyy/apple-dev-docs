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

Pass in context and range to identify the issue the user selected. The context must match one of the contexts returned from [`writingToolsCoordinator(_:requestsContextsFor:completion:)`](nswritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestscontextsfor:completion:).md) and the range must match the range in the context of one of the grammar details returned for that context from [`writingToolsCoordinator(_:requestsGrammarResultsFor:completion:)`](nswritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestsgrammarresultsfor:completion:).md) Returns NO if the UI cannot be brought up.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/showgrammarpresentation(for:in:))*