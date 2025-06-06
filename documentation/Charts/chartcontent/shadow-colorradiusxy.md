# shadow(color:radius:x:y:)

**Framework**: Swift Charts  
**Kind**: method

A chart content that adds a shadow to this chart content.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+
- watchOS 9.4+

## Declaration

```swift
nonisolated
func shadow(color: Color = Color(.sRGBLinear, white: 0, opacity: 0.33), radius: CGFloat, x: CGFloat = 0, y: CGFloat = 0) -> some ChartContent
```

## Parameters

- `color`: The shadow’s color.
- `radius`: A measure of how much to blur the shadow. Larger values result in more blur.
- `x`: An amount to offset the shadow horizontally.
- `y`: An amount to offset the shadow vertically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chartcontent/shadow(color:radius:x:y:))*