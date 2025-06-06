# subscript(_:)

**Framework**: RealityKit  
**Kind**: subscript

Accesses a pose transformation using the index of the joint name.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
subscript(joint: String) -> Transform? { get set }
```

#### Overview

> **Note**: Setting a joint to `nil` has no effect.

Setting a joint to `nil` has no effect.

## Parameters

- `joint`: The joint name of transformation to access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/skeletalpose/subscript(_:))*