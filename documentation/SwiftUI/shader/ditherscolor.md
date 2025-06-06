# dithersColor

**Framework**: SwiftUI  
**Kind**: property

For shader functions that return color values, whether the returned color has dither noise added to it, or is simply rounded to the output bit-depth. For shaders generating smooth gradients, dithering is usually necessary to prevent visible banding in the result.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var dithersColor: Bool { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shader/ditherscolor)*