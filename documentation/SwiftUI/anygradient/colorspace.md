# colorSpace(_:)

**Framework**: SwiftUI  
**Kind**: method

Returns a version of the gradient that will use a specified color space for interpolating between its colors.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func colorSpace(_ space: Gradient.ColorSpace) -> AnyGradient
```

#### Return Value

A new gradient that interpolates its colors in the specified color space.

#### Discussion

```swift
Rectangle().fill(.linearGradient(
    colors: [.white, .blue]).colorSpace(.perceptual))
```

## Parameters

- `space`: The color space the new gradient will use to   interpolate its constituent colors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/anygradient/colorspace(_:))*