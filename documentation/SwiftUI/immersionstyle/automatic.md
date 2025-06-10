# automatic

**Framework**: SwiftUI  
**Kind**: property

The default immersion style.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
static var automatic: AutomaticImmersionStyle { get }
```

#### Discussion

The system uses this style for an [`ImmersiveSpace`](immersivespace.md) if you don’t provide an [`immersionStyle(selection:in:)`](scene/immersionstyle(selection:in:).md) scene modifier. You don’t typically specify the `automatic` style explicitly.

By default, on visionOS, the system uses the [`mixed`](immersionstyle/mixed.md) immersion style as the `automatic` style and for macOS the [`full`](immersionstyle/full.md) immersion style as the `automatic` style.

## See Also

- [static var full: FullImmersionStyle](immersionstyle/full.md)
  An immersion style that displays unbounded content that completely replaces passthrough video.
- [static var mixed: MixedImmersionStyle](immersionstyle/mixed.md)
  An immersion style that displays unbounded content intermixed with other app content, along with passthrough video.
- [static var progressive: ProgressiveImmersionStyle](immersionstyle/progressive.md)
  An immersion style that displays unbounded content that partially replaces passthrough video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/immersionstyle/automatic)*