# animatedValueType

**Framework**: RealityKit  
**Kind**: property  
**Required**: Yes

A value that defines the type that the action animates, if the action animates a target value.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
var animatedValueType: (any AnimatableData.Type)? { get }
```

#### Discussion

In your implementation, return a type that matches the action animation’s bind target.

For example if the action animates a [`Transform`](transform.md), return `Transform.self` in your implementation, and set the action animation’s bind target to  [`BindTarget.transform`](bindtarget/transform.md) when creating an [`AnimationResource`](animationresource.md) with `AnimationResource.makeActionAnimation(...)`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entityaction/animatedvaluetype)*