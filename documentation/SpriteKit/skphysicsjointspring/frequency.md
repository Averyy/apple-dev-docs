# frequency

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

Defines the frequency or stiffness characteristics of the spring.

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
var frequency: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat frequency;
```

#### Discussion

The default value is `0.0`, creating a rigid joint between the spring’s two bodies. Setting the frequency to a low value, for example `0.5`, creates a spring with slow oscillations that will settle slowly. Setting the frequency to a high value, for example `10.0`, creates a stiffer spring with faster and fewer oscillations.

## See Also

### Configuring a Spring Joint
- [var damping: CGFloat](./damping.md)
  Defines how the spring’s motion should be damped due to the forces of friction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsjointspring/frequency)*