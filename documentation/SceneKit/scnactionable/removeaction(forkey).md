# removeAction(forKey:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Removes an action associated with a specific key.

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
func removeAction(forKey key: String)
```

```objc
- (void) removeActionForKey:(NSString *) key;
```

## Discussion

If the node is currently running an action that matches the key, SceneKit removes that action from the node, skipping any remaining animation it would perform but keeping any changes already made to the node.

Use this method to cancel actions you scheduled using the [`runAction(_:forKey:)`](./runaction%28_,forkey%29.md) or [`runAction(_:forKey:completionHandler:)`](./runaction%28_,forkey,completionhandler%29.md) method.

## Parameters

- `key`: A string that uniquely identifies a action.

## See Also

### Canceling a Node’s Running Actions
- [func removeAllActions()](./removeallactions%28%29.md)
  Ends and removes all actions from the node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnactionable/removeaction(forkey:))*