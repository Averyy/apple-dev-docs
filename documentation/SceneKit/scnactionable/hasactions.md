# hasActions

**Framework**: SceneKit  
**Kind**: property  
**Required**: Yes

A Boolean value that indicates whether the node is currently executing any actions.

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
var hasActions: Bool { get }
```

#### Discussion

This value is [`true`](https://developer.apple.com/documentation/swift/true) if the node has any executing actions; otherwise the value is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [func action(forKey: String) -> SCNAction?](scnactionable/action(forkey:).md)
  Returns an action associated with a specific key.
- [var actionKeys: [String]](scnactionable/actionkeys.md)
  The list of keys for which the node has attached actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnactionable/hasactions)*