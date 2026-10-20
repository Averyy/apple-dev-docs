# state

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The current level of Writing Tools activity in your view.

**Availability**:
- macOS 15.2+

## Declaration

```swift
var state: NSWritingToolsCoordinator.State { get }
```

```objc
@property (readonly) NSWritingToolsCoordinatorState state;
```

#### Discussion

Use this property to determine when Writing Tools is actively making changes to your view. During the course of Writing Tools interactions, the system reports state changes to the delegate’s [`writingToolsCoordinator(_:willChangeTo:completion:)`](./delegate-swift.protocol/writingtoolscoordinator%28_,willchangeto,completion%29.md) method and updates this property accordingly.

## See Also

### Managing the current state
- [func stopWritingTools()](./stopwritingtools%28%29.md)
  Stops the current Writing Tools operation and dismisses the system UI.
- [NSWritingToolsCoordinator.State](./state-swift.enum.md)
  The states that indicate the current activity, if any, Writing Tools is performing in your view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/state-swift.property)*