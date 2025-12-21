# resolveHDR(in:)

**Framework**: SwiftUI  
**Kind**: method

Evaluates this color to a resolved color with content headroom, given a set of environment values.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func resolveHDR(in environment: EnvironmentValues) -> Color.ResolvedHDR
```

#### Return Value

The color’s value in the sRGB color space.

## Parameters

- `environment`: The environment of the view displaying   the color.

## See Also

- [struct ResolvedHDR](color/resolvedhdr.md)
  A concrete color value, including HDR headroom information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/color/resolvehdr(in:))*