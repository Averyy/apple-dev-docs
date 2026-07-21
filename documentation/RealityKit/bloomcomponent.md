# BloomComponent

**Framework**: RealityKit  
**Kind**: struct

The `BloomComponent` adds a luminous glow effect around bright objects in the scene by extracting and blurring the brightest parts of the image, then combining them back with the original rendering. If scope is set to `unbounded` Bloom will be computed on the entire screen. If scope is set to `hierarchical` multiple Bloom Components can be used to opt in only the regions around certain objects for blooming.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct BloomComponent
```

#### Overview

Bloom is available on devices with Apple7 GPU family feature support. Note: On visionOS, Bloom only works in an immersive space and will have no effect in a shared space.

To adjust the appearance of the bloom effect, you also need a `BloomOptionsComponent`

Example Code:

```swift
// Add the bloom component to the root and set it to unbounded.
// This enables bloom in the scene with default parameters
var bloomComponent = BloomComponent()
bloomComponent.scope = .unbounded
self.root.components.set(bloomComponent)

// Add the bloom options component to the root.
// Set strength 1 for a bright effect and threshold 0 so that
// everything blooms no matter how dim.
var bloomOptionsComponent = BloomOptionsComponent()
bloomOptionsComponent.strength = 1
bloomOptionsComponent.threshold = 0
self.root.components.set(bloomOptionsComponent)
```

#### Performance and Thermal State

Bloom is a screen-space effect, so its cost scales with how much of the screen it touches. There are two distinct contributions to keep in mind:

- **Applying the bloom** is proportional to the on-screen size of the bloomers — the bright regions that exceed the [`threshold`](bloomoptionscomponent/threshold.md). Larger and brighter bloomers and a larger [`blurRadius`](bloomoptionscomponent/blurradius.md) increase this cost.
- **Searching for bloom** is a separate step with a large cost that is proportional to the portion of the screen scanned for bright pixels. With [`unbounded`](bloomcomponent/bloomscope/unbounded.md) this scans the entire screen regardless of how much of the scene actually blooms.

You can shrink the searched region — and therefore this large cost — by using [`hierarchical`](bloomcomponent/bloomscope/hierarchical.md) and attaching a `BloomComponent` to the entities that should bloom. Bloom is then only searched for and applied within the screen-space bounds of those entity hierarchies. Prefer [`hierarchical`](bloomcomponent/bloomscope/hierarchical.md) whenever you know which objects bloom; reserve [`unbounded`](bloomcomponent/bloomscope/unbounded.md) for cases where bright pixels can appear anywhere on screen.

Excessive bloom may contribute to user-noticeable frame drops and can cause the device to heat up in graphically demanding scenes. Monitor the thermal state and shrink the bloom region (prefer [`hierarchical`](bloomcomponent/bloomscope/hierarchical.md) over [`unbounded`](bloomcomponent/bloomscope/unbounded.md)), lower the [`blurRadius`](bloomoptionscomponent/blurradius.md), raise the [`threshold`](bloomoptionscomponent/threshold.md), or disable bloom entirely if necessary.

To stay responsive to the device’s available thermal headroom, read `ProcessInfo.processInfo.thermalState` and observe [`ProcessInfo.thermalStateDidChangeNotification`](https://developer.apple.comhttps://developer.apple.com/documentation/foundation/processinfo/thermalstatedidchangenotification) to react when it changes. As the reported state moves from `.fair` toward `.serious` and `.critical`, reduce bloom’s footprint.

## Topics

### Creating a bloom component
- [init(scope: BloomComponent.BloomScope)](bloomcomponent/init(scope:).md)
  Creates a BloomComponent with the specified scope.
### Configuring the bloom scope
- [var scope: BloomComponent.BloomScope](bloomcomponent/scope.md)
  The scope of where bloom will be computed
- [BloomComponent.BloomScope](bloomcomponent/bloomscope.md)
### Initializers
- [init()](bloomcomponent/init.md)
  Creates a Bloom Component.

## Relationships

### Conforms To
- [Component](component.md)

## See Also

- [struct BloomOptionsComponent](bloomoptionscomponent.md)
  A component that sets the properties for the bloom post-processing effects.
- [struct ToneMappingComponent](tonemappingcomponent.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/bloomcomponent)*