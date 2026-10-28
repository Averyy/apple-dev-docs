# MixedImmersionStyle

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

An immersion style that displays unbounded content intermixed with other app content, along with passthrough video.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
struct MixedImmersionStyle
```

## Overview

When this immersion style is selected, the immersion amount reported by the closure of [`onImmersionChange(initial:_:)`](./view/onimmersionchange%28initial,_%29.md) is `0.0`.

Use [`mixed`](./immersionstyle/mixed.md) with the [`immersionStyle(selection:in:)`](./scene/immersionstyle%28selection,in%29.md)modifier to specify this style.

## Topics

### Creating the immersion style
- [init()](./mixedimmersionstyle/init%28%29.md)

## Relationships

### Conforms To
- [ImmersionStyle](./immersionstyle.md)

## See Also

### Supporting types
- [struct AutomaticImmersionStyle](./automaticimmersionstyle.md)
  The default style of immersive spaces.
- [struct FullImmersionStyle](./fullimmersionstyle.md)
  An immersion style that displays unbounded content that completely replaces passthrough video.
- [struct ProgressiveImmersionStyle](./progressiveimmersionstyle.md)
  An immersion style that displays unbounded content that partially replaces passthrough video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/mixedimmersionstyle)*