# assistiveAccessNavigationIcon(_:)

**Framework**: SwiftUI  
**Kind**: method

Configures the view’s icon for purposes of navigation.

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
nonisolated
func assistiveAccessNavigationIcon(_ icon: Image) -> some View
```

#### Discussion

In an Assistive Access scene on iOS and iPadOS, the icon is displayed adjacent to the navigation title. Otherwise, the icon is unused.

## Parameters

- `icon`: The icon image to display.

## See Also

- [var accessibilityAssistiveAccessEnabled: Bool](environmentvalues/accessibilityassistiveaccessenabled.md)
  A Boolean value that indicates whether Assistive Access is in use.
- [struct AssistiveAccess](assistiveaccess.md)
  A scene that presents an interface appropriate for Assistive Access on iOS and iPadOS. On other platforms, this scene is unused.
- [func assistiveAccessNavigationIcon(systemImage: String) -> some View](view/assistiveaccessnavigationicon(systemimage:).md)
  Configures the view’s icon for purposes of navigation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/assistiveaccessnavigationicon(_:))*