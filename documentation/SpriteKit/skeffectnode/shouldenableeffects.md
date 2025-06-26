# shouldEnableEffects

**Framework**: SpriteKit  
**Kind**: property

A Boolean value that determines whether the effect node applies the filter to its children as they are drawn.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
@MainActor
var shouldEnableEffects: Bool { get set }
```

#### Discussion

If the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the effect node applies the filter and blends the results. If the value is [`false`](https://developer.apple.com/documentation/swift/false), the effect node is ignored and its children are rendered normally. The default value is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [Applying Special Effects to a Node’s Children](applying-special-effects-to-a-node-s-children.md)
  Apply the Core Image suite of filters to child nodes of an effect node.
- [var filter: CIFilter?](skeffectnode/filter.md)
  The Core Image filter to apply.
- [var shouldCenterFilter: Bool](skeffectnode/shouldcenterfilter.md)
  A Boolean value that determines whether the effect node automatically sets the filter’s image center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skeffectnode/shouldenableeffects)*