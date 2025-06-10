# runAction(_:completionHandler:)

**Framework**: SceneKit  
**Kind**: method  
**Required**: Yes

Adds an action to the list of actions executed by the node. SceneKit calls the specified block when the action completes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func runAction(_ action: SCNAction) async
```

#### Discussion

> **Note**:  In Swift, you can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func runAction(_ action: SCNAction) async
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

The new action is processed the next time SceneKit prepares to render a frame.

SceneKit calls your block after the action’s duration is complete. For example, in a game you could use this method to show a Game Over message after performing a fade-out action on a node that displays a player character.

## Parameters

- `action`: The action to be performed.
- `block`: A completion block that SceneKit calls when the action completes.

## See Also

- [func runAction(SCNAction)](scnactionable/runaction(_:).md)
  Adds an action to the list of actions executed by the node.
- [func runAction(SCNAction, forKey: String?)](scnactionable/runaction(_:forkey:).md)
  Adds an identifiable action to the list of actions executed by the node.
- [func runAction(SCNAction, forKey: String?, completionHandler: (() -> Void)?)](scnactionable/runaction(_:forkey:completionhandler:).md)
  Adds an identifiable action to the list of actions executed by the node. SceneKit calls the specified block when the action completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnactionable/runaction(_:completionhandler:))*