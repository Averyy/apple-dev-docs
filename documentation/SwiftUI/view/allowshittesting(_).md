# allowsHitTesting(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Configures whether this view participates in hit test operations.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func allowsHitTesting(_ enabled: Bool) -> some View
```

#### Discussion

Specify `true` to indicate this view participates in hit testing for a method such as [`hitTest(_:)`](../nshostingview/hittest%28_%29.md) to determine whether a point is inside a view. Otherwise specify `false`.

For more information, see [`hitTest(_:)`](../../AppKit/nsview/hittest%28_%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/allowshittesting(_:))*