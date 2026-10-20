# action(forKey:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns an action associated with a specific key.

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
func action(forKey key: String) -> SCNAction?
```

```objc
- (SCNAction *) actionForKey:(NSString *) key;
```

#### Return Value

The action object matching the specified key, or `nil` if the node does not have an action identified by the key.

#### Discussion

Use this method to retrieve actions you scheduled using the [`runAction(_:forKey:)`](./runaction%28_,forkey%29.md) or [`runAction(_:forKey:completionHandler:)`](./runaction%28_,forkey,completionhandler%29.md) method.

## Parameters

- `key`: A string that uniquely identifies a action.

## See Also

### Inspecting a Node’s Running Actions
- [var hasActions: Bool](./hasactions.md)
  A Boolean value that indicates whether the node is currently executing any actions.
- [var actionKeys: [String]](./actionkeys.md)
  The list of keys for which the node has attached actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnactionable/action(forkey:))*