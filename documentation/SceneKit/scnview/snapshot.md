# snapshot()

**Framework**: SceneKit  
**Kind**: method

Renders the view’s scene into a new image object.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
func snapshot() -> NSImage
```

#### Return Value

An image object depicting the view in its current state.

#### Discussion

This method is thread-safe and may be called at any time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnview/snapshot())*