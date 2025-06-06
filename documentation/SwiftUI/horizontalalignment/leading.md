# leading

**Framework**: SwiftUI  
**Kind**: property

A guide that marks the leading edge of the view.

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
static let leading: HorizontalAlignment
```

## Mentions

- [Building layouts with stack views](building-layouts-with-stack-views.md)

#### Discussion

Use this guide to align the leading edges of views. For a device that uses a left-to-right language, the leading edge is on the left:

![A box that contains the word, Leading. Vertical](https://docs-assets.developer.apple.com/published/7bde2ddd5347556c261423c21c988e18/HorizontalAlignment-leading-1-iOS%402x.png)

The following code generates the image above using a [`VStack`](vstack.md):

```swift
struct HorizontalAlignmentLeading: View {
    var body: some View {
        VStack(alignment: .leading, spacing: 0) {
            Color.red.frame(width: 1)
            Text("Leading").font(.title).border(.gray)
            Color.red.frame(width: 1)
        }
    }
}
```

## See Also

- [static let center: HorizontalAlignment](horizontalalignment/center.md)
  A guide that marks the horizontal center of the view.
- [static let trailing: HorizontalAlignment](horizontalalignment/trailing.md)
  A guide that marks the trailing edge of the view.
- [static let listRowSeparatorLeading: HorizontalAlignment](horizontalalignment/listrowseparatorleading.md)
  A guide marking the leading edge of a `List` row separator.
- [static let listRowSeparatorTrailing: HorizontalAlignment](horizontalalignment/listrowseparatortrailing.md)
  A guide marking the trailing edge of a `List` row separator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/horizontalalignment/leading)*