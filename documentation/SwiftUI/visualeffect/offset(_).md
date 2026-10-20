# offset(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Offsets the view by the horizontal and vertical amount specified in the offset parameter.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
func offset(_ offset: CGSize) -> some VisualEffect
```

#### Return Value

An effect that offsets the view by `offset`.

## Parameters

- `offset`: The distance to offset the view.

## See Also

### Translating
- [func offset(x: CGFloat, y: CGFloat) -> some VisualEffect](./offset%28x,y%29.md)
  Offsets the view by the specified horizontal and vertical distances.
- [func offset(z: CGFloat) -> some VisualEffect](./offset%28z%29.md)
  Brings a view forward in Z by the provided distance in points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/visualeffect/offset(_:))*