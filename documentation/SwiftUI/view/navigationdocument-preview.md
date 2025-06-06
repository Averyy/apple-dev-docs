# navigationDocument(_:preview:)

**Framework**: SwiftUI  
**Kind**: method

Configures the view’s document for purposes of navigation.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func navigationDocument<D, I1, I2>(_ document: D, preview: SharePreview<I1, I2>) -> some View where D : Transferable, I1 : Transferable, I2 : Transferable
```

#### Discussion

In iOS, iPadOS, this populates the title menu with a header previewing the document. In macOS, this populates a proxy icon.

Refer to the [`Configure your apps navigation titles`](configure-your-apps-navigation-titles.md) article for more information on navigation document modifiers.

## Parameters

- `document`: The transferable content associated to the   navigation title.
- `preview`: The preview of the document to use when sharing.

## See Also

- [func navigationTitle(_:)](view/navigationtitle(_:).md)
  Configures the view’s title for purposes of navigation, using a string binding.
- [func navigationSubtitle(_:)](view/navigationsubtitle(_:).md)
  Configures the view’s subtitle for purposes of navigation.
- [func navigationDocument(_:)](view/navigationdocument(_:).md)
  Configures the view’s document for purposes of navigation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/navigationdocument(_:preview:))*