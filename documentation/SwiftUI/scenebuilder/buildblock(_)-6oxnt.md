# buildBlock(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

Passes a single scene written as a child scene through unmodified.

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
static func buildBlock<Content>(_ content: Content) -> Content where Content : Scene
```

**Other overloads**:

```swift
@export(implementation)
static func buildBlock<each Content>(_ content: repeat each Content) -> some Scene where repeat each Content : Scene
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scenebuilder/buildblock(_:)-6oxnt)*