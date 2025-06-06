# MixedImmersionStyle

**Framework**: SwiftUI  
**Kind**: struct

An immersion style that displays unbounded content intermixed with other app content, along with passthrough video.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
struct MixedImmersionStyle
```

#### Overview

When this immersion style is selected, the immersion amount reported by the closure of `View/onImmersionChange(_:)` is `0.0`.

Use [`mixed`](immersionstyle/mixed.md) with the [`immersionStyle(selection:in:)`](scene/immersionstyle(selection:in:).md)modifier to specify this style.

## Topics

### Creating the immersion style
- [init()](mixedimmersionstyle/init.md)

## Relationships

### Conforms To
- [ImmersionStyle](immersionstyle.md)

## See Also

- [struct AutomaticImmersionStyle](automaticimmersionstyle.md)
  The default style of immersive spaces.
- [struct FullImmersionStyle](fullimmersionstyle.md)
  An immersion style that displays unbounded content that completely replaces passthrough video.
- [struct ProgressiveImmersionStyle](progressiveimmersionstyle.md)
  An immersion style that displays unbounded content that partially replaces passthrough video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/mixedimmersionstyle)*