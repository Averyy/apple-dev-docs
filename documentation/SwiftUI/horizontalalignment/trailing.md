# trailing

**Framework**: SwiftUI  
**Kind**: property

A guide that marks the trailing edge of the view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
static let trailing: HorizontalAlignment
```

#### Discussion

Use this guide to align the trailing edges of views. For a device that uses a left-to-right language, the trailing edge is on the right:

![A box that contains the word, Trailing. Vertical](https://docs-assets.developer.apple.com/published/3d36e49a665b5b5f456af2746870ae1c/HorizontalAlignment-trailing-1-iOS%402x.png)

The following code generates the image above using a [`VStack`](vstack.md):

```swift
struct HorizontalAlignmentTrailing: View {
    var body: some View {
        VStack(alignment: .trailing, spacing: 0) {
            Color.red.frame(width: 1)
            Text("Trailing").font(.title).border(.gray)
            Color.red.frame(width: 1)
        }
    }
}
```

## See Also

- [static let leading: HorizontalAlignment](horizontalalignment/leading.md)
  A guide that marks the leading edge of the view.
- [static let center: HorizontalAlignment](horizontalalignment/center.md)
  A guide that marks the horizontal center of the view.
- [static let listRowSeparatorLeading: HorizontalAlignment](horizontalalignment/listrowseparatorleading.md)
  A guide marking the leading edge of a `List` row separator.
- [static let listRowSeparatorTrailing: HorizontalAlignment](horizontalalignment/listrowseparatortrailing.md)
  A guide marking the trailing edge of a `List` row separator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/horizontalalignment/trailing)*