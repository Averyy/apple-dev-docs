# hasActions

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean value that indicates whether the node is currently executing any actions.

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
var hasActions: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL hasActions;
```

#### Discussion

This value is [`true`](../../Swift/true.md) if the node has any executing actions; otherwise the value is [`false`](../../Swift/false.md).

## See Also

### Inspecting a Node’s Running Actions
- [func action(forKey: String) -> SCNAction?](./action%28forkey%29.md)
  Returns an action associated with a specific key.
- [var actionKeys: [String]](./actionkeys.md)
  The list of keys for which the node has attached actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnactionable/hasactions)*