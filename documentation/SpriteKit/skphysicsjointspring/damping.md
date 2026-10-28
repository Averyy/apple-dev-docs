# damping

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

Defines how the spring’s motion should be damped due to the forces of friction.

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
var damping: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat damping;
```

## Discussion

The default value is `0.0`. Increasing the value increases the energy loss with each oscillation: there will be fewer and smaller oscillations and time taken for the spring to settle will decrease.

## See Also

### Configuring a Spring Joint
- [var frequency: CGFloat](./frequency.md)
  Defines the frequency or stiffness characteristics of the spring.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsjointspring/damping)*