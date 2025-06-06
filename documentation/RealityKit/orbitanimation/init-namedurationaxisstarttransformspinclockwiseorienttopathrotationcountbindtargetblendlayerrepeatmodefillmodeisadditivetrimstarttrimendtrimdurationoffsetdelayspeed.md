# init(name:duration:axis:startTransform:spinClockwise:orientToPath:rotationCount:bindTarget:blendLayer:repeatMode:fillMode:isAdditive:trimStart:trimEnd:trimDuration:offset:delay:speed:)

**Framework**: RealityKit  
**Kind**: init

Creates an animation that revolves an entity around its origin.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
init(name: String = "", duration: TimeInterval = 1.0, axis: SIMD3<Float> = .init(x: 0.0, y: 1.0, z: 0.0), startTransform: Transform = .identity, spinClockwise: Bool = true, orientToPath: Bool = false, rotationCount: Float = 1.0, bindTarget: BindTarget? = nil, blendLayer: Int32 = 0, repeatMode: AnimationRepeatMode = .none, fillMode: AnimationFillMode = [], isAdditive: Bool = false, trimStart: TimeInterval? = nil, trimEnd: TimeInterval? = nil, trimDuration: TimeInterval? = nil, offset: TimeInterval = 0, delay: TimeInterval = 0, speed: Float = 1)
```

## Parameters

- `name`: A textual name for the animation.
- `duration`: The elapsed time for one complete rotation.
- `axis`: A 3D vector that points in the direction of the axis around   which to rotate.
- `startTransform`: The orbiting entity’s beginning position.
- `spinClockwise`: A Boolean value that indicates whether the object   orbits the center point in the clockwise direction.
- `orientToPath`: A Boolean value that indicates whether the orbiting   object updates its orientation during the animation to orient itself   along the rotation path.
- `rotationCount`: The number of times to rotate the target entity before   stopping.
- `bindTarget`: A textual name that identifies the particular property   that animates.
- `blendLayer`: The order in which the framework composites the animation   into the view.
- `repeatMode`: An option that determines how the animation repeats.
- `fillMode`: The playback behavior outside of the normal duration.
- `isAdditive`: A Boolean value that indicates whether the animation   builds on the current state of the target entity or resets the state   before running.
- `trimStart`: The optional time, in seconds, at which the animation plays.
- `trimEnd`: The optional time, in seconds, at which the animation stops.
- `trimDuration`: An optional duration that overrides the calculated duration.
- `offset`: The time, in seconds, at which the animation begins within the duration.
- `delay`: An amount of time that lapses before the animation plays.
- `speed`: A factor that changes the animation’s rate of playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/orbitanimation/init(name:duration:axis:starttransform:spinclockwise:orienttopath:rotationcount:bindtarget:blendlayer:repeatmode:fillmode:isadditive:trimstart:trimend:trimduration:offset:delay:speed:))*