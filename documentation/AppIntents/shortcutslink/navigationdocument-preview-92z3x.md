# navigationDocument(_:preview:)

**Framework**: App Intents  
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
func navigationDocument<D>(_ document: D, preview: SharePreview<Never, Never>) -> some View where D : Transferable
```

#### Discussion

In iOS, iPadOS, this populates the title menu with a header previewing the document. In macOS, this populates a proxy icon.

Refer to the doc:Configure-Your-Apps-Navigation-Titles article for more information on navigation document modifiers.

## Parameters

- `document`: The transferable content associated to the   navigation title.
- `preview`: The preview of the document to use when sharing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/shortcutslink/navigationdocument(_:preview:)-92z3x)*