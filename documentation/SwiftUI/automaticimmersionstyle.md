# AutomaticImmersionStyle

**Framework**: SwiftUI  
**Kind**: struct

The default style of immersive spaces.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
struct AutomaticImmersionStyle
```

#### Overview

You don’t typically use this style explicitly, but if you need to, use [`automatic`](immersionstyle/automatic.md) with the [`immersionStyle(selection:in:)`](scene/immersionstyle(selection:in:).md)modifier to specify this style.

## Topics

### Creating the immersion style
- [init()](automaticimmersionstyle/init.md)

## Relationships

### Conforms To
- [ImmersionStyle](immersionstyle.md)

## See Also

- [struct FullImmersionStyle](fullimmersionstyle.md)
  An immersion style that displays unbounded content that completely replaces passthrough video.
- [struct MixedImmersionStyle](mixedimmersionstyle.md)
  An immersion style that displays unbounded content intermixed with other app content, along with passthrough video.
- [struct ProgressiveImmersionStyle](progressiveimmersionstyle.md)
  An immersion style that displays unbounded content that partially replaces passthrough video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/automaticimmersionstyle)*