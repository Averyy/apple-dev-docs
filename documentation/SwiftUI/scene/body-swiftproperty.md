# body

**Framework**: SwiftUI  
**Kind**: property  
**Required**: Yes

The content and behavior of the scene.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@SceneBuilder
@MainActor @preconcurrency var body: Self.Body { get }
```

#### Discussion

For any scene that you create, provide a computed `body` property that defines the scene as a composition of other scenes. You can assemble a scene from built-in scenes that SwiftUI provides, as well as other scenes that you’ve defined.

Swift infers the scene’s [`Body`](scene/body-swift.associatedtype.md) associated type based on the contents of the `body` property.

## See Also

- [associatedtype Body : Scene](scene/body-swift.associatedtype.md)
  The type of scene that represents the body of this scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scene/body-swift.property)*