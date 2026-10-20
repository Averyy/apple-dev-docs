# ProgressiveImmersionStyle

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

An immersion style that displays unbounded content that partially replaces passthrough video.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
struct ProgressiveImmersionStyle
```

#### Overview

Use [`progressive`](./immersionstyle/progressive.md) with the [`immersionStyle(selection:in:)`](./scene/immersionstyle%28selection,in%29.md)modifier to specify this style.

## Topics

### Creating the immersion style
- [init()](./progressiveimmersionstyle/init%28%29.md)
  An immersion style that displays unbounded content that partially replaces passthrough video.
### Initializers
- [init(immersion:initialAmount:)](./progressiveimmersionstyle/init%28immersion,initialamount%29.md)
  An immersion style that displays unbounded content that partially replaces passthrough video.
### Instance Properties
- [let aspectRatio: ProgressiveImmersionAspectRatio](./progressiveimmersionstyle/aspectratio.md)
  The aspect ratio used for this instance of the style.
- [let initialImmersionAmount: Double?](./progressiveimmersionstyle/initialimmersionamount.md)
  The initial amount of immersion used for this instance of the style.
- [let maximumImmersionAmount: Double?](./progressiveimmersionstyle/maximumimmersionamount.md)
  The maximum amount of immersion used for this instance of the style.
- [let minimumImmersionAmount: Double?](./progressiveimmersionstyle/minimumimmersionamount.md)
  The minimum amount of immersion used for this instance of the style.

## Relationships

### Conforms To
- [ImmersionStyle](./immersionstyle.md)

## See Also

### Supporting types
- [struct AutomaticImmersionStyle](./automaticimmersionstyle.md)
  The default style of immersive spaces.
- [struct FullImmersionStyle](./fullimmersionstyle.md)
  An immersion style that displays unbounded content that completely replaces passthrough video.
- [struct MixedImmersionStyle](./mixedimmersionstyle.md)
  An immersion style that displays unbounded content intermixed with other app content, along with passthrough video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/progressiveimmersionstyle)*