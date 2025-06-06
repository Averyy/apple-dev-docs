# full

**Framework**: SwiftUI  
**Kind**: property

An immersion style that displays unbounded content that completely replaces passthrough video.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
static var full: FullImmersionStyle { get }
```

#### Discussion

When this immersion style is selected, the immersion amount reported by the closure of `View/onImmersionChange(_:)` is `1.0`.

Use the [`immersionStyle(selection:in:)`](scene/immersionstyle(selection:in:).md) scene modifier to specify this style for an [`ImmersiveSpace`](immersivespace.md).

When using this style, the space’s content fully obscures passthrough except for the user’s upper limbs. You can manage limb visibility separately by applying the [`upperLimbVisibility(_:)`](scene/upperlimbvisibility(_:).md) scene modifier to the space, or the view modifier equivalent to a view inside the scene.

The immersion style affects how windows interact with virtual objects in the environment. In `full` immersion, windows always render in front of virtual content, no matter how someone positions the window or the content. This helps people to avoid losing track of windows behind virtual content when passthrough is off.

## See Also

- [static var automatic: AutomaticImmersionStyle](immersionstyle/automatic.md)
  The default immersion style.
- [static var mixed: MixedImmersionStyle](immersionstyle/mixed.md)
  An immersion style that displays unbounded content intermixed with other app content, along with passthrough video.
- [static var progressive: ProgressiveImmersionStyle](immersionstyle/progressive.md)
  An immersion style that displays unbounded content that partially replaces passthrough video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/immersionstyle/full)*