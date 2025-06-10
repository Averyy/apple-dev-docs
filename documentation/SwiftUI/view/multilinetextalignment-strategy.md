# multilineTextAlignment(strategy:)

**Framework**: SwiftUI  
**Kind**: method

A modifier for the default text alignment strategy in the view hierarchy.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func multilineTextAlignment(strategy: Text.AlignmentStrategy) -> some View
```

#### Discussion

To control the alignment explicitly at a view level, choose the [`layoutBased`](text/alignmentstrategy/layoutbased.md) mode and set the [`multilineTextAlignment`](environmentvalues/multilinetextalignment.md) to the appropriate value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/multilinetextalignment(strategy:))*