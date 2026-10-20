# noiseField(smoothness:animationSpeed:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates and returns a field behavior object that applies random noise to other forces.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func noiseField(smoothness: CGFloat, animationSpeed speed: CGFloat) -> Self
```

```objc
+ (instancetype) noiseFieldWithSmoothness:(CGFloat) smoothness animationSpeed:(CGFloat) speed;
```

#### Return Value

A field behavior object that applies noise to other fields in the same area.

#### Discussion

A noise field creates a differentiable Perlin simplex noise field that varies over time. You can combine a noise field with other fields to add some variability to the behavior of those fields. The smoothness of the field defines how random the changes are from one point to the next point. A smooth field still adds noise but does so in a more predictable way. This field ignores the mass of the item.

## Parameters

- `smoothness`: The smoothness of the field. Specify a value between `0.0` and `1.0`, where `0.0` indicates the maximum amount of randomness in the generated field and `1.0` indicates the least amount of randomness.
- `speed`: The frequency at which the noise field changes, measured in Hertz (Hz). Specify `0.0` to create a noise field that does not change over time.

## See Also

### Getting the field behaviors
- [class func dragField() -> Self](./dragfield%28%29.md)
  Creates and returns a field behavior for slowing an object’s velocity.
- [class func springField() -> Self](./springfield%28%29.md)
  Creates and returns a spring field behavior.
- [class func velocityField(direction: CGVector) -> Self](./velocityfield%28direction%29.md)
  Creates and returns a field behavior object that applies a directional velocity to items.
- [class func electricField() -> Self](./electricfield%28%29.md)
  Creates and returns a field behavior object that interacts with charged items.
- [class func magneticField() -> Self](./magneticfield%28%29.md)
  Creates and returns a field behavior that interacts with charged items.
- [class func radialGravityField(position: CGPoint) -> Self](./radialgravityfield%28position%29.md)
  Creates and returns a field behavior object that models a radial gravitational force.
- [class func linearGravityField(direction: CGVector) -> Self](./lineargravityfield%28direction%29.md)
  Creates and returns a field behavior object that models a linear gravitational force.
- [class func vortexField() -> Self](./vortexfield%28%29.md)
  Creates and returns a field behavior object that applies a rotational force relative to the field’s position.
- [class func turbulenceField(smoothness: CGFloat, animationSpeed: CGFloat) -> Self](./turbulencefield%28smoothness,animationspeed%29.md)
  Creates and returns a field behavior object that applies noise to an item in motion.
- [class func field(evaluationBlock: (UIFieldBehavior, CGPoint, CGVector, CGFloat, CGFloat, TimeInterval) -> CGVector) -> Self](./field%28evaluationblock%29.md)
  Creates and returns a field behavior object that applies an app-specified field to items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifieldbehavior/noisefield(smoothness:animationspeed:))*