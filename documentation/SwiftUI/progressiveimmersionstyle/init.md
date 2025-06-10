# init()

**Framework**: SwiftUI  
**Kind**: init

An immersion style that displays unbounded content that partially replaces passthrough video.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
init()
```

#### Discussion

The system initially uses a radial portal effect that replaces passthrough in a portion of the field of view. People can interactively adjust the size of the portal by turning the Digital Crown, up to the point where the portal fully replaces passthrough. The latter matches the behavior of the [`full`](immersionstyle/full.md) immersion style, including the configurable visibility of the viewer’s upper limbs.

When this immersion style is selected, the immersion amount reported by the closure of [`onImmersionChange(initial:_:)`](view/onimmersionchange(initial:_:).md) is within the range of the immersion that this style is defined with.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/progressiveimmersionstyle/init())*