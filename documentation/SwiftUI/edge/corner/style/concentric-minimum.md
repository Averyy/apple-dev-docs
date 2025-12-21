# concentric(minimum:)

**Framework**: SwiftUI  
**Kind**: method

The concentric corner style with an optional minimum corner style. When a corner is concentric to its container, it will adjust the current corner radius to ensure that the container corner radius equals to current corner radius plus the distance between corners. If the current corner is too far away from the container corner, the radius will be resolved as zero unless a minimum corner style is provided.

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
static func concentric(minimum: Edge.Corner.Style? = nil) -> Edge.Corner.Style
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/edge/corner/style/concentric(minimum:))*