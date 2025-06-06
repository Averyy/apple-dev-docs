# center

**Framework**: SwiftUI  
**Kind**: property

A guide that marks the horizontal center of the view.

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
static let center: HorizontalAlignment
```

#### Discussion

Use this guide to align the centers of views:

![A box that contains the word, Center. Vertical](https://docs-assets.developer.apple.com/published/98c827da09fff59ad521ae1431e95b70/HorizontalAlignment-center-1-iOS%402x.png)

The following code generates the image above using a [`VStack`](vstack.md):

```swift
struct HorizontalAlignmentCenter: View {
    var body: some View {
        VStack(alignment: .center, spacing: 0) {
            Color.red.frame(width: 1)
            Text("Center").font(.title).border(.gray)
            Color.red.frame(width: 1)
        }
    }
}
```

## See Also

- [static let leading: HorizontalAlignment](horizontalalignment/leading.md)
  A guide that marks the leading edge of the view.
- [static let trailing: HorizontalAlignment](horizontalalignment/trailing.md)
  A guide that marks the trailing edge of the view.
- [static let listRowSeparatorLeading: HorizontalAlignment](horizontalalignment/listrowseparatorleading.md)
  A guide marking the leading edge of a `List` row separator.
- [static let listRowSeparatorTrailing: HorizontalAlignment](horizontalalignment/listrowseparatortrailing.md)
  A guide marking the trailing edge of a `List` row separator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/horizontalalignment/center)*