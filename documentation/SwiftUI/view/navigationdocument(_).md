# navigationDocument(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Configures the view’s document for purposes of navigation.

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
func navigationDocument(_ url: URL) -> some View
```

**Other overloads**:

```swift
nonisolated
func navigationDocument<D>(_ document: D) -> some View where D : Transferable
```

## Discussion

In iOS, iPadOS, this populates the title menu with a header previewing the document. In macOS, this populates a proxy icon.

Refer to the [Configure your apps navigation titles](../configure-your-apps-navigation-titles.md) article for more information on navigation document modifiers.

## Parameters

- `url`: The URL content associated to the navigation title.

## See Also

### Setting titles for navigation content
- [func navigationTitle(_:)](./navigationtitle%28_%29.md)
  Configures the view’s title for purposes of navigation, using a localized string resource.
- [func navigationSubtitle(_:)](./navigationsubtitle%28_%29.md)
  Configures the view’s subtitle for purposes of navigation, using a localized string resource.
- [func navigationDocument(_:preview:)](./navigationdocument%28_,preview%29.md)
  Configures the view’s document for purposes of navigation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/navigationdocument(_:))*