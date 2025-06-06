# blur(radius:options:)

**Framework**: SwiftUI  
**Kind**: method

Returns a filter that applies a Gaussian blur.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static func blur(radius: CGFloat, options: GraphicsContext.BlurOptions = BlurOptions()) -> GraphicsContext.Filter
```

#### Return Value

A filter that applies Gaussian blur.

## Parameters

- `radius`: The standard deviation of the Gaussian blur.
- `options`: A set of options controlling the application of the   effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/filter/blur(radius:options:))*