# FullImmersionStyle

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

An immersion style that displays unbounded content that completely replaces passthrough video.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
struct FullImmersionStyle
```

## Overview

When this immersion style is selected, the immersion amount reported by the closure of [`onImmersionChange(initial:_:)`](./view/onimmersionchange%28initial,_%29.md) is `1.0`.

Use [`full`](./immersionstyle/full.md) with the [`immersionStyle(selection:in:)`](./scene/immersionstyle%28selection,in%29.md)modifier to specify this style.

## Topics

### Creating the immersion style
- [init()](./fullimmersionstyle/init%28%29.md)

## Relationships

### Conforms To
- [ImmersionStyle](./immersionstyle.md)

## See Also

### Supporting types
- [struct AutomaticImmersionStyle](./automaticimmersionstyle.md)
  The default style of immersive spaces.
- [struct MixedImmersionStyle](./mixedimmersionstyle.md)
  An immersion style that displays unbounded content intermixed with other app content, along with passthrough video.
- [struct ProgressiveImmersionStyle](./progressiveimmersionstyle.md)
  An immersion style that displays unbounded content that partially replaces passthrough video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/fullimmersionstyle)*