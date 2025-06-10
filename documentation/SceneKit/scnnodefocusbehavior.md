# SCNNodeFocusBehavior

**Framework**: SceneKit  
**Kind**: enum

Options for the focusable states of a SceneKit node.

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
enum SCNNodeFocusBehavior
```

## Topics

### Enumeration Cases
- [SCNNodeFocusBehavior.none](scnnodefocusbehavior/none.md)
  Node is not focusable.
- [SCNNodeFocusBehavior.occluding](scnnodefocusbehavior/occluding.md)
  Node is not focusable and prevents nodes that it visually obscures from becoming focusable.
- [SCNNodeFocusBehavior.focusable](scnnodefocusbehavior/focusable.md)
  Node is focusable and prevents nodes that it visually obscures from becoming focusable.
### Initializers
- [init?(rawValue: Int)](scnnodefocusbehavior/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var focusBehavior: SCNNodeFocusBehavior](scnnode/focusbehavior.md)
  The focus behavior for a node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnodefocusbehavior)*