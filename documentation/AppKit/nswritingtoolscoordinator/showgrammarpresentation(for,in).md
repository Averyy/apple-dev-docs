# showGrammarPresentation(for:in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Used to support the presentation of grammar issues in text. When the user interacts with an issue, call this to bring up the relevant UI.

**Availability**:
- macOS 27.0+

## Declaration

```swift
func showGrammarPresentation(for range: NSRange, in context: NSWritingToolsCoordinator.Context) -> Bool
```

```objc
- (BOOL) showGrammarPresentationForRange:(NSRange) range inContext:(NSWritingToolsCoordinatorContext *) context;
```

## Discussion

Pass in context and range to identify the issue the user selected. The context must match one of the contexts returned from [`writingToolsCoordinator(_:requestsContextsFor:completion:)`](./delegate-swift.protocol/writingtoolscoordinator%28_,requestscontextsfor,completion%29.md) and the range must match the range in the context of one of the grammar details returned for that context from [`writingToolsCoordinator(_:requestsGrammarResultsFor:completion:)`](./delegate-swift.protocol/writingtoolscoordinator%28_,requestsgrammarresultsfor,completion%29.md) Returns NO if the UI cannot be brought up.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/showgrammarpresentation(for:in:))*