# actionHandler

**Framework**: SharedWithYouCore  
**Kind**: property  
**Role**: Instance Property

The collaboration action handler.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
weak var actionHandler: (any SWCollaborationActionHandler)? { get set }
```

```objc
@property (nonatomic, weak, readwrite) id<SWCollaborationActionHandler> actionHandler;
```

## Discussion

Register the delegate soon after launch and handle actions immediately to avoid timeouts.

## See Also

### Accessing coordinator attributes
- [class var shared: SWCollaborationCoordinator](./shared.md)
  The shared collaboration coordinator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyoucore/swcollaborationcoordinator/actionhandler)*