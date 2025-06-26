# navigationDocument(_:preview:)

**Framework**: FamilyControls  
**Kind**: method

Configures the view’s document for purposes of navigation.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func navigationDocument<D, I1, I2>(_ document: D, preview: SharePreview<I1, I2>) -> some View where D : Transferable, I1 : Transferable, I2 : Transferable
```

#### Discussion

In iOS, iPadOS, this populates the title menu with a header previewing the document. In macOS, this populates a proxy icon.

Refer to the doc:Configure-Your-Apps-Navigation-Titles article for more information on navigation document modifiers.

## Parameters

- `document`: The transferable content associated to the   navigation title.
- `preview`: The preview of the document to use when sharing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivityiconview/navigationdocument(_:preview:)-5tmle)*