# automatic

**Framework**: SwiftUI  
**Kind**: property

The automatic behavior. The scene’s windows will be restored as defined by the underlying platform.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
static let automatic: SceneRestorationBehavior
```

#### Discussion

On macOS, this behavior is governed by a system setting which can be toggled on and off by the user. On all other platforms, it is enabled by default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scenerestorationbehavior/automatic)*