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

Note: On visionOS, Bloom only works in an immersive space and will have no effect in a shared space.

To adjust the appearance of the bloom effect, you also need a `BloomSettingsComponent`

Example Code:

```swift
// Add the bloom component to the root and set it to unbounded.
// This enables bloom in the scene with default parameters
var bloomComponent = BloomComponent()
bloomComponent.scope = .unbounded
self.root.components.set(bloomComponent)

// Add the bloom settings component to the root.
// Set strength 1 for a bright effect and threshold 0 so that
// everything blooms no matter how dim.
var bloomSettingsComponent = BloomSettingsComponent()
bloomSettingsComponent.strength = 1
bloomSettingsComponent.threshold = 0
self.root.components.set(bloomSettingsComponent)
```

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
- [struct BloomSettingsComponent](bloomsettingscomponent.md)
  A component that sets the properties for the bloom post-processing effects.
- [struct ToneMappingComponent](tonemappingcomponent.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/bloomcomponent)*