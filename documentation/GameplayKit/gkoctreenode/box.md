# box

**Framework**: GameplayKit  
**Kind**: property  
**Role**: Instance Property

The axis-aligned bounding box represented by the node.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var box: GKBox { get }
```

```objc
@property (readonly) struct GKBox box;
```

## Discussion

You can use this rectangle to find elements in the tree with the [`elements(in:)`](../gkoctree/elements%28in%29.md) method.

For more information, see [GameplayKit Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkoctreenode/box)*