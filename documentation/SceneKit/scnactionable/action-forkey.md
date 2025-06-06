# action(forKey:)

**Framework**: SceneKit  
**Kind**: method  
**Required**: Yes

Returns an action associated with a specific key.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func action(forKey key: String) -> SCNAction?
```

#### Return Value

The action object matching the specified key, or `nil` if the node does not have an action identified by the key.

#### Discussion

Use this method to retrieve actions you scheduled using the [`runAction(_:forKey:)`](scnactionable/runaction(_:forkey:).md) or [`runAction(_:forKey:completionHandler:)`](scnactionable/runaction(_:forkey:completionhandler:).md) method.

## Parameters

- `key`: A string that uniquely identifies a action.

## See Also

- [var hasActions: Bool](scnactionable/hasactions.md)
  A Boolean value that indicates whether the node is currently executing any actions.
- [var actionKeys: [String]](scnactionable/actionkeys.md)
  The list of keys for which the node has attached actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnactionable/action(forkey:))*