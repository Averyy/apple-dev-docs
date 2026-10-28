# writingToolsCoordinator(_:requestsGrammarResultsFor:completion:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate for information about grammar issues in the specified context.

**Availability**:
- macOS 27.0+

## Declaration

```swift
optional func writingToolsCoordinator(_ writingToolsCoordinator: NSWritingToolsCoordinator, requestsGrammarResultsFor context: NSWritingToolsCoordinator.Context, completion: @escaping @Sendable ([NSTextCheckingResult]) -> Void)
```

```swift
optional func writingToolsCoordinator(_ writingToolsCoordinator: NSWritingToolsCoordinator, grammarResultsFor context: NSWritingToolsCoordinator.Context) async -> [NSTextCheckingResult]
```

```objc
- (void) writingToolsCoordinator:(NSWritingToolsCoordinator *) writingToolsCoordinator requestsGrammarResultsForContext:(NSWritingToolsCoordinatorContext *) context completion:(void (^)(NSArray<NSTextCheckingResult *> *results)) completion;
```

## Discussion

To support the grammar presentation UI, the delegate should provide information about the identified and currently indicated grammar issues in the specified context. The elements of the results array should be `NSTextCheckingResult` objects of grammar type, of the sort that are returned from grammar checking, with ranges relative to the context. If you use grammar presentation, you must implement this delegate method to provide them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestsgrammarresultsfor:completion:))*