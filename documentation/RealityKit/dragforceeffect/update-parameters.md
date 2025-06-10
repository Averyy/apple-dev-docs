# update(parameters:)

**Framework**: RealityKit  
**Kind**: method

Calculates the drag forces for rigid bodies from the force effect.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
func update(parameters: inout ForceEffectParameters)
```

#### Discussion

The framework automatically calls this method for you at each physics simulation step, so you don’t need to call it yourself.

## Parameters

- `parameters`: On input, the parameters that calculate forces to the affected physics bodies; on output, the updates to those forces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/dragforceeffect/update(parameters:))*