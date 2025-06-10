# snapshot()

**Framework**: SceneKit  
**Kind**: method

Renders the view’s scene into a new image object.

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
@MainActor
func snapshot() -> UIImage
```

#### Return Value

An image object depicting the view in its current state.

#### Discussion

This method is thread-safe and may be called at any time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnview/snapshot())*