# repeat(count:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Creates an animation that repeats the specified number of times.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency func `repeat`(count: Int) -> AnimationResource
```

#### Return Value

A repeating copy of the calling animation resource.

## Parameters

- `count`: The number of animation repetitions.

## See Also

### Creating an animation resource
- [static func generate(with: any AnimationDefinition) throws -> AnimationResource](./generate%28with%29.md)
  Creates an animation resource from a definition.
- [static func sequence(with: [AnimationResource]) throws -> AnimationResource](./sequence%28with%29.md)
  Creates an animation resource that plays a collection of animations in a specified sequence.
- [static func group(with: [AnimationResource]) throws -> AnimationResource](./group%28with%29.md)
  Creates an animation resource that simultaneously plays back a collection of animations.
- [func `repeat`(duration: TimeInterval) -> AnimationResource](./repeat%28duration%29.md)
  Repeats an animation for the specified amount of time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationresource/repeat(count:))*