# upperDistanceLimit

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The largest distance allowed for the sliding joint.

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
var upperDistanceLimit: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat upperDistanceLimit;
```

## Discussion

The default value is `0.0`.

## See Also

### Configuring a Sliding Joint
- [var shouldEnableLimits: Bool](./shouldenablelimits.md)
  A Boolean value that indicates whether the sliding joint is restricted so that the objects may only slide a finite distance from the initial anchor point.
- [var lowerDistanceLimit: CGFloat](./lowerdistancelimit.md)
  The smallest distance allowed for the sliding joint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsjointsliding/upperdistancelimit)*