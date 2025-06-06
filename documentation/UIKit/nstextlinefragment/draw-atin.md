# draw(at:in:)

**Framework**: UIKit  
**Kind**: method

Renders the line fragment contents at the rendering origin.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func draw(at point: CGPoint, in context: CGContext)
```

#### Discussion

You can specify the origin as (`NSMinX(typographicBounds) + glyphOrigin.x, NSMinY(typographicBounds) + glyphOrigin.y)` relative to the line fragment group coordinate system.

## Parameters

- `point`: The origin as a  .
- `context`: The drawing context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlinefragment/draw(at:in:))*