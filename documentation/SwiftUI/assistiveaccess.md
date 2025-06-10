# AssistiveAccess

**Framework**: SwiftUI  
**Kind**: struct

A scene that presents an interface appropriate for Assistive Access on iOS and iPadOS. On other platforms, this scene is unused.

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
struct AssistiveAccess<Content> where Content : View
```

## Topics

### Initializers
- [init(content: () -> Content)](assistiveaccess/init(content:).md)
  Creates a Assistive Access scene.

## Relationships

### Conforms To
- [Scene](scene.md)

## See Also

- [var accessibilityAssistiveAccessEnabled: Bool](environmentvalues/accessibilityassistiveaccessenabled.md)
  A Boolean value that indicates whether Assistive Access is in use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/assistiveaccess)*