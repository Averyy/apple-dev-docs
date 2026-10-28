# actionKeys

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The list of keys for which the node has attached actions.

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
var actionKeys: [String] { get }
```

```objc
@property (nonatomic, readonly) NSArray<NSString *> * actionKeys;
```

## Discussion

Use this property to list actions you scheduled using the [`runAction(_:forKey:)`](./runaction%28_,forkey%29.md) or [`runAction(_:forKey:completionHandler:)`](./runaction%28_,forkey,completionhandler%29.md) method.

## See Also

### Inspecting a Node’s Running Actions
- [func action(forKey: String) -> SCNAction?](./action%28forkey%29.md)
  Returns an action associated with a specific key.
- [var hasActions: Bool](./hasactions.md)
  A Boolean value that indicates whether the node is currently executing any actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnactionable/actionkeys)*