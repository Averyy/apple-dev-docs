# isValid

**Framework**: RealityKit  
**Kind**: property

A Boolean value that indicates whether the animation controller is functional.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var isValid: Bool { get }
```

#### Discussion

This function returns `false` for stopped animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationplaybackcontroller/isvalid-9tk2f)*