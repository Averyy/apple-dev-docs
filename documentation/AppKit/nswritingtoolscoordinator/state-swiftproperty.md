# state

**Framework**: AppKit  
**Kind**: property

The current level of Writing Tools activity in your view.

**Availability**:
- macOS 15.2+

## Declaration

```swift
@MainActor
var state: NSWritingToolsCoordinator.State { get }
```

#### Discussion

Use this property to determine when Writing Tools is actively making changes to your view. During the course of Writing Tools interactions, the system reports state changes to the delegate’s [`writingToolsCoordinator(_:willChangeTo:completion:)`](nswritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:willchangeto:completion:).md) method and updates this property accordingly.

## See Also

- [func stopWritingTools()](nswritingtoolscoordinator/stopwritingtools.md)
  Stops the current Writing Tools operation and dismisses the system UI.
- [NSWritingToolsCoordinator.State](nswritingtoolscoordinator/state-swift.enum.md)
  The states that indicate the current activity, if any, Writing Tools is performing in your view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/state-swift.property)*