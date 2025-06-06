# navigationTitle(_:)

**Framework**: SwiftUI  
**Kind**: method

Configures the view’s title for purposes of navigation, using a string binding.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func navigationTitle(_ title: Binding<String>) -> some View
```

#### Discussion

In iOS, iPadOS, and macOS, this allows editing the navigation title when the title is displayed in the toolbar.

Refer to the [`Configure your apps navigation titles`](configure-your-apps-navigation-titles.md) article for more information on navigation title modifiers.

## Parameters

- `title`: The text of the title.

## See Also

- [func navigationSubtitle(_:)](view/navigationsubtitle(_:).md)
  Configures the view’s subtitle for purposes of navigation.
- [func navigationDocument(_:)](view/navigationdocument(_:).md)
  Configures the view’s document for purposes of navigation.
- [func navigationDocument(_:preview:)](view/navigationdocument(_:preview:).md)
  Configures the view’s document for purposes of navigation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/navigationtitle(_:))*