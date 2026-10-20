# SCNNodeFocusBehavior

**Framework**: SceneKit  
**Kind**: enum  
**Role**: Enumeration

Options for the focusable states of a SceneKit node.

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
enum SCNNodeFocusBehavior
```

```c
enum SCNNodeFocusBehavior : NSInteger;
```

## Topics

### Enumeration Cases
- [SCNNodeFocusBehavior.none](./scnnodefocusbehavior/none.md)
  Node is not focusable.
- [SCNNodeFocusBehavior.occluding](./scnnodefocusbehavior/occluding.md)
  Node is not focusable and prevents nodes that it visually obscures from becoming focusable.
- [SCNNodeFocusBehavior.focusable](./scnnodefocusbehavior/focusable.md)
  Node is focusable and prevents nodes that it visually obscures from becoming focusable.
### Initializers
- [init?(rawValue: Int)](./scnnodefocusbehavior/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Handling UI Focus
- [var focusBehavior: SCNNodeFocusBehavior](./scnnode/focusbehavior.md)
  The focus behavior for a node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnodefocusbehavior)*