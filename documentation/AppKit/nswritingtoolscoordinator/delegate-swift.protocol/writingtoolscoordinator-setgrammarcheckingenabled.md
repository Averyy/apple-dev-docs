# writingToolsCoordinator(_:setGrammarCheckingEnabled:)

**Framework**: AppKit  
**Kind**: method

Notifies the delegate when the user chooses to disable grammar checking.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
optional func writingToolsCoordinator(_ writingToolsCoordinator: NSWritingToolsCoordinator, setGrammarCheckingEnabled enabled: Bool)
```

#### Discussion

To support the grammar presentation UI, the delegate is notified if the user chooses the option provided in the grammar presentation UI to disable grammar checking for the view. If you use grammar presentation, you should implement this method to respond to that action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:setgrammarcheckingenabled:))*