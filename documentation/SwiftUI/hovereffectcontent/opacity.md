# opacity(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the transparency of the view.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func opacity(_ opacity: Double) -> some HoverEffectContent
```

#### Return Value

An effect that sets the transparency of the view.

#### Discussion

When applying the `opacity(_:)` effect to a view that has already had its opacity transformed, the effect of the underlying opacity transformation is multiplied.

## Parameters

- `opacity`: A value between 0 (fully transparent) and 1 (fully   opaque).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/hovereffectcontent/opacity(_:))*