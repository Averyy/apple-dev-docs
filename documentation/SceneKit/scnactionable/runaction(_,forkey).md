# runAction(_:forKey:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Adds an identifiable action to the list of actions executed by the node.

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
func runAction(_ action: SCNAction, forKey key: String?)
```

```objc
- (void) runAction:(SCNAction *) action forKey:(NSString *) key;
```

## Discussion

This method is identical to [`runAction(_:)`](./runaction%28_%29.md), but the action is stored and identified so that you can retrieve or cancel it later. If an action using the same key is already running, SceneKit removes it before adding the new action.

## Parameters

- `action`: The action to be performed.
- `key`: A unique key used to identify the action.

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
- [func runAction(SCNAction, forKey: String?, completionHandler: (() -> Void)?)](./runaction%28_,forkey,completionhandler%29.md)
  Adds an identifiable action to the list of actions executed by the node. SceneKit calls the specified block when the action completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnactionable/runaction(_:forkey:))*