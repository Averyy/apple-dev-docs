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
func navigationDocument<D>(_ document: D) -> some View where D : Transferable
```

**Other overloads**:

```swift
nonisolated
func navigationDocument(_ url: URL) -> some View
```

## Discussion

In iOS, iPadOS, this populates the title menu with a header previewing the document. In macOS, this populates a proxy icon.

Refer to the [Configure your apps navigation titles](../configure-your-apps-navigation-titles.md) article for more information on navigation document modifiers.

## Parameters

- `document`: The transferable content associated to the navigation title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/navigationdocument(_:)-66zro)*