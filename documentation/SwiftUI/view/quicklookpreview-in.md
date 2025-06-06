# quickLookPreview(_:in:)

**Framework**: SwiftUI  
**Kind**: method

Presents a Quick Look preview of the URLs you provide.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+

## Declaration

```swift
nonisolated
func quickLookPreview<Items>(_ selection: Binding<Items.Element?>, in items: Items) -> some View where Items : RandomAccessCollection, Items.Element == URL
```

#### Return Value

A view that presents the preview of the contents of the URL.

#### Discussion

The Quick Look preview appears when you set the binding to a non-`nil` item. When you set the item back to `nil`, Quick Look dismisses the preview. If the value of the selection binding isn’t contained in the items collection, Quick Look treats it the same as a `nil` selection.

Quick Look updates the value of the selection binding to match the URL of the file the user is previewing. Upon dismissal by the user, Quick Look automatically sets the item binding to `nil`.

## Parameters

- `selection`: A   to an element that’s part of the items collection. This is the URL that you currently want to preview.
- `items`: A collection of URLs to preview.

## See Also

- [func quickLookPreview(Binding<URL?>) -> some View](view/quicklookpreview(_:).md)
  Presents a Quick Look preview of the contents of a single URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/quicklookpreview(_:in:))*