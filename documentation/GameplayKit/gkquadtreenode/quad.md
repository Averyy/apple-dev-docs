# quad

**Framework**: GameplayKit  
**Kind**: property  
**Role**: Instance Property

The axis-aligned bounding rectangle represented by the node.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var quad: GKQuad { get }
```

```objc
@property (nonatomic, readonly) GKQuad quad;
```

## Discussion

You can use this rectangle to find elements in the tree with the [`elements(in:)`](../gkquadtree/elements%28in%29.md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkquadtreenode/quad)*