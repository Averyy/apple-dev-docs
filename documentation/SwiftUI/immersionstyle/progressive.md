# progressive

**Framework**: SwiftUI  
**Kind**: property

An immersion style that displays unbounded content that partially replaces passthrough video.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
static var progressive: ProgressiveImmersionStyle { get }
```

#### Discussion

The system initially uses a radial portal effect that replaces passthrough in a portion of the field of view. People can interactively adjust the size of the portal by turning the Digital Crown, including down to a minimum amount of immersion defined by the system and up to the point where the portal fully covers passthrough. If someone tries to reduce the portal size below the minimum value, the portal smoothly bounces back to the minimum size. The portal’s behavior at the maximum size matches the behavior of the [`full`](immersionstyle/full.md) immersion style, including the configurable visibility of the viewer’s upper limbs.

When this immersion style is selected, the immersion amount reported by the closure of `View/onImmersionChange(_:)` is within the range of the immersion that this style uses.

Use the [`immersionStyle(selection:in:)`](scene/immersionstyle(selection:in:).md) scene modifier to specify this style for an [`ImmersiveSpace`](immersivespace.md):

```swift
@main
struct ImmersiveApp: App {
    @State private var immersionStyle: ImmersionStyle = .progressive
    var body: some Scene {
        ImmersiveSpace { ... }
        .immersionStyle(selection: $immersionStyle, in: .progressive))
    }
}
```

The immersion style affects how windows interact with virtual objects in the environment. In `progressive` immersion, windows always render in front of virtual content, no matter how someone positions the window or the content. This helps people avoid losing track of windows behind virtual content when passthrough is off.

## See Also

- [static var automatic: AutomaticImmersionStyle](immersionstyle/automatic.md)
  The default immersion style.
- [static var full: FullImmersionStyle](immersionstyle/full.md)
  An immersion style that displays unbounded content that completely replaces passthrough video.
- [static var mixed: MixedImmersionStyle](immersionstyle/mixed.md)
  An immersion style that displays unbounded content intermixed with other app content, along with passthrough video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/immersionstyle/progressive)*