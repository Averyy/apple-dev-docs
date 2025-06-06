# visible(_:)

**Framework**: SwiftUI  
**Kind**: method

The target view is visible by the given amount, where zero is fully hidden, and one is fully visible.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
static func visible(_ amount: Double) -> ScrollTransitionConfiguration.Threshold
```

#### Discussion

Values less than zero or greater than one are clamped.

## See Also

- [static var centered: ScrollTransitionConfiguration.Threshold](scrolltransitionconfiguration/threshold/centered.md)
  The target view is centered within the container
- [static let hidden: ScrollTransitionConfiguration.Threshold](scrolltransitionconfiguration/threshold/hidden.md)
- [static let visible: ScrollTransitionConfiguration.Threshold](scrolltransitionconfiguration/threshold/visible.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrolltransitionconfiguration/threshold/visible(_:))*