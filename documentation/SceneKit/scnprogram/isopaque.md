# isOpaque

**Framework**: SceneKit  
**Kind**: property

A Boolean value that indicates whether fragments rendered by the program are fully opaque.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var isOpaque: Bool { get set }
```

#### Discussion

The default value is [`true`](https://developer.apple.com/documentation/Swift/true), indicating that all fragments rendered by the program are fully opaque. In this case, SceneKit can composite these fragments into the final image without blending, improving rendering performance.

If your shader program renders fragment colors whose alpha value is less than `1.0`, change this property’s value to [`false`](https://developer.apple.com/documentation/Swift/false) for proper blending.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnprogram/isopaque)*