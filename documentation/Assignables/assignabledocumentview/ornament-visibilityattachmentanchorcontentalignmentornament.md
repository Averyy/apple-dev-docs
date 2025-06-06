# ornament(visibility:attachmentAnchor:contentAlignment:ornament:)

**Framework**: Assignables  
**Kind**: method

Presents an ornament.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
nonisolated
func ornament<Content>(visibility: Visibility = .automatic, attachmentAnchor: OrnamentAttachmentAnchor, contentAlignment: Alignment = .center, @ViewBuilder ornament: () -> Content) -> some View where Content : View
```

#### Discussion

Use this method to show an ornament at the specified position. The example below displays an ornament below the window:

```None
Text("A view with an ornament")
    .ornament(attachmentAnchor: .scene(.bottom)) {
        OrnamentContent()
    }
```

## Parameters

- `visibility`: The visibility of the ornament.
- `attachmentAnchor`: The positioning anchor that defines the   attachment point of the ornament.
- `contentAlignment`: The alignment of the ornament with its attachment anchor.
- `content`: The content of the ornament.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocumentview/ornament(visibility:attachmentanchor:contentalignment:ornament:))*