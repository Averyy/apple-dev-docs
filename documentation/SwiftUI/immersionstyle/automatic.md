# automatic

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

The default immersion style.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
static var automatic: AutomaticImmersionStyle { get }
```

Available when `Self` is `AutomaticImmersionStyle`.

#### Discussion

The system uses this style for an [`ImmersiveSpace`](../immersivespace.md) if you don’t provide an [`immersionStyle(selection:in:)`](../scene/immersionstyle%28selection,in%29.md) scene modifier. You don’t typically specify the `automatic` style explicitly.

By default, on visionOS, the system uses the [`mixed`](./mixed.md) immersion style as the `automatic` style and for macOS the [`full`](./full.md) immersion style as the `automatic` style.

## See Also

### Getting built-in styles
- [static var full: FullImmersionStyle](./full.md)
  An immersion style that displays unbounded content that completely replaces passthrough video.
- [static var mixed: MixedImmersionStyle](./mixed.md)
  An immersion style that displays unbounded content intermixed with other app content, along with passthrough video.
- [static var progressive: ProgressiveImmersionStyle](./progressive.md)
  An immersion style that displays unbounded content that partially replaces passthrough video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/immersionstyle/automatic)*