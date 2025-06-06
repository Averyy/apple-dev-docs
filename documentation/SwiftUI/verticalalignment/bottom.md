# bottom

**Framework**: SwiftUI  
**Kind**: property

A guide that marks the bottom edge of the view.

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
static let bottom: VerticalAlignment
```

## Mentions

- [Aligning views within a stack](aligning-views-within-a-stack.md)

#### Discussion

Use this guide to align the bottom edges of views:

![A box that contains the word, Bottom. A horizontal](https://docs-assets.developer.apple.com/published/cf3af2d8bd3b57705462db8e421c1aba/VerticalAlignment-bottom-1-iOS%402x.png)

The following code generates the image above using an [`HStack`](hstack.md):

```swift
struct VerticalAlignmentBottom: View {
    var body: some View {
        HStack(alignment: .bottom, spacing: 0) {
            Color.red.frame(height: 1)
            Text("Bottom").font(.title).border(.gray)
            Color.red.frame(height: 1)
        }
    }
}
```

## See Also

- [static let top: VerticalAlignment](verticalalignment/top.md)
  A guide that marks the top edge of the view.
- [static let center: VerticalAlignment](verticalalignment/center.md)
  A guide that marks the vertical center of the view.
- [static let firstTextBaseline: VerticalAlignment](verticalalignment/firsttextbaseline.md)
  A guide that marks the top-most text baseline in a view.
- [static let lastTextBaseline: VerticalAlignment](verticalalignment/lasttextbaseline.md)
  A guide that marks the bottom-most text baseline in a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/verticalalignment/bottom)*