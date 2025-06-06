# mixed

**Framework**: SwiftUI  
**Kind**: property

An immersion style that displays unbounded content intermixed with other app content, along with passthrough video.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
static var mixed: MixedImmersionStyle { get }
```

#### Discussion

When this immersion style is selected, the immersion amount reported by the closure of `View/onImmersionChange(_:)` is `0.0`.

Use the [`immersionStyle(selection:in:)`](scene/immersionstyle(selection:in:).md) scene modifier to specify this style for an [`ImmersiveSpace`](immersivespace.md). However, this is the default immersion style if you don’t specify one.

The immersion style affects how windows interact with virtual objects in the environment. In `mixed` immersion, a virtual object obscures part or all of a window that’s behind the object. Similarly, a window obscures a virtual object that’s behind the window.

## See Also

- [static var automatic: AutomaticImmersionStyle](immersionstyle/automatic.md)
  The default immersion style.
- [static var full: FullImmersionStyle](immersionstyle/full.md)
  An immersion style that displays unbounded content that completely replaces passthrough video.
- [static var progressive: ProgressiveImmersionStyle](immersionstyle/progressive.md)
  An immersion style that displays unbounded content that partially replaces passthrough video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/immersionstyle/mixed)*