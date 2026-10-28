# isAsynchronous

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the content is rendered asynchronously.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var isAsynchronous: Bool { get set }
```

```objc
@property (nonatomic, getter=isAsynchronous) BOOL asynchronous;
```

## Discussion

The default value is [`true`](../../Swift/true.md). If the value is [`false`](../../Swift/false.md), the contents of this view are synchronized with Core Animation updates.

## See Also

### Configuring Performance Related Toggles
- [var ignoresSiblingOrder: Bool](./ignoressiblingorder.md)
  A Boolean value that indicates whether parent-child and sibling relationships affect the rendering order of nodes in the scene.
- [var shouldCullNonVisibleNodes: Bool](./shouldcullnonvisiblenodes.md)
  A Boolean value that indicates whether the view automatically culls non-visible nodes from the rendering tree.
- [var allowsTransparency: Bool](./allowstransparency.md)
  A Boolean property that indicates whether the view is rendered using transparency.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skview/isasynchronous)*