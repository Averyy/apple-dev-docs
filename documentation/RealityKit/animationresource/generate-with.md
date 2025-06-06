# generate(with:)

**Framework**: RealityKit  
**Kind**: method

Creates an animation resource from a definition.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency static func generate(with definition: any AnimationDefinition) throws -> AnimationResource
```

#### Return Value

An animation resource that shares the configuration of the definition.

## Parameters

- `definition`: The configuration of a timeframe and visual semantics from   which to generate an animation resource.

## See Also

- [static func sequence(with: [AnimationResource]) throws -> AnimationResource](animationresource/sequence(with:).md)
  Creates an animation resource that plays a collection of animations in a specified sequence.
- [static func group(with: [AnimationResource]) throws -> AnimationResource](animationresource/group(with:).md)
  Creates an animation resource that simultaneously plays back a collection of animations.
- [func `repeat`(count: Int) -> AnimationResource](animationresource/repeat(count:).md)
  Creates an animation that repeats the specified number of times.
- [func `repeat`(duration: TimeInterval) -> AnimationResource](animationresource/repeat(duration:).md)
  Repeats an animation for the specified amount of time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationresource/generate(with:))*