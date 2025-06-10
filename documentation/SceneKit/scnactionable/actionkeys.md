# actionKeys

**Framework**: SceneKit  
**Kind**: property  
**Required**: Yes

The list of keys for which the node has attached actions.

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
var actionKeys: [String] { get }
```

#### Discussion

Use this property to list actions you scheduled using the [`runAction(_:forKey:)`](scnactionable/runaction(_:forkey:).md) or [`runAction(_:forKey:completionHandler:)`](scnactionable/runaction(_:forkey:completionhandler:).md) method.

## See Also

- [func action(forKey: String) -> SCNAction?](scnactionable/action(forkey:).md)
  Returns an action associated with a specific key.
- [var hasActions: Bool](scnactionable/hasactions.md)
  A Boolean value that indicates whether the node is currently executing any actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnactionable/actionkeys)*