# AssistiveAccess

**Framework**: SwiftUI  
**Kind**: struct

A scene that presents an interface appropriate for Assistive Access on iOS and iPadOS. On other platforms, this scene is unused.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct AssistiveAccess<Content> where Content : View
```

## Topics

### Initializers
- [init(content: () -> Content)](assistiveaccess/init(content:).md)
  Creates an Assistive Access scene.

## Relationships

### Conforms To
- [Scene](scene.md)

## See Also

- [var accessibilityAssistiveAccessEnabled: Bool](environmentvalues/accessibilityassistiveaccessenabled.md)
  A Boolean value that indicates whether Assistive Access is in use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/assistiveaccess)*