# runAction(_:forKey:completionHandler:)

**Framework**: SceneKit  
**Kind**: method  
**Required**: Yes

Adds an identifiable action to the list of actions executed by the node. SceneKit calls the specified block when the action completes.

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
func runAction(_ action: SCNAction, forKey key: String?) async
```

#### Discussion

> **Note**:  In Swift, you can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func runAction(_ action: SCNAction, forKey key: String?) async
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

This method is identical to [`runAction(_:completionHandler:)`](scnactionable/runaction(_:completionhandler:).md), but the action is stored and identified so that you can retrieve or cancel it later. If an action using the same key is already running, SceneKit removes it before adding the new action.

SceneKit calls your block after the action’s duration is complete. For example, you can use this method with a wait action to execute some code after a timed delay. If during the delay period you need to prevent the code from running, use the [`removeAction(forKey:)`](scnactionable/removeaction(forkey:).md) method to cancel it.

## Parameters

- `action`: The action to be performed.
- `key`: A unique key used to identify the action.
- `block`: A completion block called when the action completes.

## See Also

- [func action(forKey: String) -> SCNAction?](scnactionable/action(forkey:).md)
  Returns an action associated with a specific key.
- [func removeAction(forKey: String)](scnactionable/removeaction(forkey:).md)
  Removes an action associated with a specific key.
- [func runAction(SCNAction)](scnactionable/runaction(_:).md)
  Adds an action to the list of actions executed by the node.
- [func runAction(SCNAction, completionHandler: (() -> Void)?)](scnactionable/runaction(_:completionhandler:).md)
  Adds an action to the list of actions executed by the node. SceneKit calls the specified block when the action completes.
- [func runAction(SCNAction, forKey: String?)](scnactionable/runaction(_:forkey:).md)
  Adds an identifiable action to the list of actions executed by the node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnactionable/runaction(_:forkey:completionhandler:))*