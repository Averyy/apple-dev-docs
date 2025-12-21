# shouldCenterFilter

**Framework**: SpriteKit  
**Kind**: property

A Boolean value that determines whether the effect node automatically sets the filter’s image center.

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
var shouldCenterFilter: Bool { get set }
```

#### Discussion

If the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) and the filter has an `inputCenter` parameter, the effect node automatically sets the filter’s input center to the effect node’s origin. The default value is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [Applying Special Effects to a Node’s Children](applying-special-effects-to-a-node-s-children.md)
  Apply the Core Image suite of filters to child nodes of an effect node.
- [var filter: CIFilter?](skeffectnode/filter.md)
  The Core Image filter to apply.
- [var shouldEnableEffects: Bool](skeffectnode/shouldenableeffects.md)
  A Boolean value that determines whether the effect node applies the filter to its children as they are drawn.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skeffectnode/shouldcenterfilter)*