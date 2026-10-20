# shouldEnableEffects

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the effect node applies the filter to its children as they are drawn.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var shouldEnableEffects: Bool { get set }
```

```objc
@property (nonatomic) BOOL shouldEnableEffects;
```

#### Discussion

If the value of this property is [`true`](../../Swift/true.md), the effect node applies the filter and blends the results. If the value is [`false`](../../Swift/false.md), the effect node is ignored and its children are rendered normally. The default value is [`false`](../../Swift/false.md).

## See Also

### Applying Core Image Filters with an Effect Node
- [Applying Special Effects to a Node’s Children](../applying-special-effects-to-a-node-s-children.md)
  Apply the Core Image suite of filters to child nodes of an effect node.
- [var filter: CIFilter?](./filter.md)
  The Core Image filter to apply.
- [var shouldCenterFilter: Bool](./shouldcenterfilter.md)
  A Boolean value that determines whether the effect node automatically sets the filter’s image center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skeffectnode/shouldenableeffects)*