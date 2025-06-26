# lineHeight(_:)

**Framework**: FamilyControls  
**Kind**: method

A modifier for the default line height in the view hierarchy.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func lineHeight(_ lineHeight: AttributedString.LineHeight?) -> some View
```

#### Discussion

The default value is `nil`. In that case, SwiftUI automatically chooses an appropriate line height setting for each context.

> **Note**: `EnvironmentValues/lineHeight`


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitytitleview/lineheight(_:))*