# isAsynchronous

**Framework**: SpriteKit  
**Kind**: property

A Boolean value that indicates whether the content is rendered asynchronously.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
var isAsynchronous: Bool { get set }
```

#### Discussion

The default value is [`true`](https://developer.apple.com/documentation/Swift/true). If the value is [`false`](https://developer.apple.com/documentation/Swift/false), the contents of this view are synchronized with Core Animation updates.

## See Also

- [var ignoresSiblingOrder: Bool](skview/ignoressiblingorder.md)
  A Boolean value that indicates whether parent-child and sibling relationships affect the rendering order of nodes in the scene.
- [var shouldCullNonVisibleNodes: Bool](skview/shouldcullnonvisiblenodes.md)
  A Boolean value that indicates whether the view automatically culls non-visible nodes from the rendering tree.
- [var allowsTransparency: Bool](skview/allowstransparency.md)
  A Boolean property that indicates whether the view is rendered using transparency.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skview/isasynchronous)*