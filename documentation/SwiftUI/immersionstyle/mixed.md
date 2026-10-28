# mixed

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

An immersion style that displays unbounded content intermixed with other app content, along with passthrough video.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
static var mixed: MixedImmersionStyle { get }
```

Available when `Self` is `MixedImmersionStyle`.

## Discussion

When this immersion style is selected, the immersion amount reported by the closure of [`onImmersionChange(initial:_:)`](../view/onimmersionchange%28initial,_%29.md) is `0.0`.

Use the [`immersionStyle(selection:in:)`](../scene/immersionstyle%28selection,in%29.md) scene modifier to specify this style for an [`ImmersiveSpace`](../immersivespace.md). However, this is the default immersion style if you don’t specify one.

The immersion style affects how windows interact with virtual objects in the environment. In `mixed` immersion, a virtual object obscures part or all of a window that’s behind the object. Similarly, a window obscures a virtual object that’s behind the window.

## See Also

### Getting built-in styles
- [static var automatic: AutomaticImmersionStyle](./automatic.md)
  The default immersion style.
- [static var full: FullImmersionStyle](./full.md)
  An immersion style that displays unbounded content that completely replaces passthrough video.
- [static var progressive: ProgressiveImmersionStyle](./progressive.md)
  An immersion style that displays unbounded content that partially replaces passthrough video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/immersionstyle/mixed)*