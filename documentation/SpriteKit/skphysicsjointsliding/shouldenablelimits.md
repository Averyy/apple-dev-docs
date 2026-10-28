# shouldEnableLimits

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the sliding joint is restricted so that the objects may only slide a finite distance from the initial anchor point.

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
var shouldEnableLimits: Bool { get set }
```

```objc
@property (nonatomic) BOOL shouldEnableLimits;
```

## Discussion

The default value is [`false`](../../Swift/false.md). If [`true`](../../Swift/true.md), then the [`lowerDistanceLimit`](./lowerdistancelimit.md) and [`upperDistanceLimit`](./upperdistancelimit.md) properties are used to limit the distance of the sliding joint.

## See Also

### Configuring a Sliding Joint
- [var lowerDistanceLimit: CGFloat](./lowerdistancelimit.md)
  The smallest distance allowed for the sliding joint.
- [var upperDistanceLimit: CGFloat](./upperdistancelimit.md)
  The largest distance allowed for the sliding joint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsjointsliding/shouldenablelimits)*