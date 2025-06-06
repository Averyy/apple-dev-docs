# blendMode(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the blend mode for compositing this view with overlapping views.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func blendMode(_ blendMode: BlendMode) -> some VisualEffect
```

#### Return Value

An effect that applies `blendMode` to this view.

#### Discussion

Use `blendMode(_:)` to combine overlapping views and use a different visual effect to produce the result. The [`BlendMode`](blendmode.md) enumeration defines many possible effects.

## Parameters

- `blendMode`: The   for compositing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/visualeffect/blendmode(_:))*