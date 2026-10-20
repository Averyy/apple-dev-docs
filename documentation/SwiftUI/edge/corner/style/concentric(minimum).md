# concentric(minimum:)

**Framework**: SwiftUI  
**Kind**: method

A rounded corner style where the corner’s radius shares a center point with the container shape’s corner radius, with an optional minimum radius.

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

#### Discussion

When a corner is concentric to its container, the system calculates the corner radius to equal the container shape’s corner radius minus the distance between corners. If the radius that the system calculates is less than the minimum radius you provide, the system uses the minimum radius. When the system calculates a zero radius, the corner is square.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/edge/corner/style/concentric(minimum:))*