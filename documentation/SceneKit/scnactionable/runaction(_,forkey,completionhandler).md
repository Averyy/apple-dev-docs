# runAction(_:forKey:completionHandler:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Adds an identifiable action to the list of actions executed by the node. SceneKit calls the specified block when the action completes.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
func runAction(_ action: SCNAction, forKey key: String?, completionHandler block: (@Sendable () -> Void)? = nil)
```

```swift
func runAction(_ action: SCNAction, forKey key: String?) async
```

```objc
- (void) runAction:(SCNAction *) action forKey:(NSString *) key completionHandler:(void (^)()) block;
```

#### Discussion

This method is identical to [`runAction(_:completionHandler:)`](./runaction%28_,completionhandler%29.md), but the action is stored and identified so that you can retrieve or cancel it later. If an action using the same key is already running, SceneKit removes it before adding the new action.

SceneKit calls your block after the action’s duration is complete. For example, you can use this method with a wait action to execute some code after a timed delay. If during the delay period you need to prevent the code from running, use the [`removeAction(forKey:)`](./removeaction%28forkey%29.md) method to cancel it.

## Parameters

- `action`: The action to be performed.
- `key`: A unique key used to identify the action.
- `block`: A completion block called when the action completes.

## See Also

### Related Documentation
- [func action(forKey: String) -> SCNAction?](./action%28forkey%29.md)
  Returns an action associated with a specific key.
- [func removeAction(forKey: String)](./removeaction%28forkey%29.md)
  Removes an action associated with a specific key.
### Running Actions
- [func runAction(SCNAction)](./runaction%28_%29.md)
  Adds an action to the list of actions executed by the node.
- [func runAction(SCNAction, completionHandler: (() -> Void)?)](./runaction%28_,completionhandler%29.md)
  Adds an action to the list of actions executed by the node. SceneKit calls the specified block when the action completes.
- [func runAction(SCNAction, forKey: String?)](./runaction%28_,forkey%29.md)
  Adds an identifiable action to the list of actions executed by the node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnactionable/runaction(_:forkey:completionhandler:))*