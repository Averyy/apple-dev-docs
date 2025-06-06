# firstTextBaseline

**Framework**: SwiftUI  
**Kind**: property

A guide that marks the top-most text baseline in a view.

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
static let firstTextBaseline: VerticalAlignment
```

## Mentions

- [Aligning views within a stack](aligning-views-within-a-stack.md)
- [Aligning views across stacks](aligning-views-across-stacks.md)

#### Discussion

Use this guide to align with the baseline of the top-most text in a view. The guide aligns with the bottom of a view that contains no text:

![A box that contains the text, First Text Baseline.](https://docs-assets.developer.apple.com/published/e676907b319612805deae559c8d91cc4/VerticalAlignment-firstTextBaseline-1-iOS%402x.png)

The following code generates the image above using an [`HStack`](hstack.md):

```swift
struct VerticalAlignmentFirstTextBaseline: View {
    var body: some View {
        HStack(alignment: .firstTextBaseline, spacing: 0) {
            Color.red.frame(height: 1)
            Text("First Text Baseline").font(.title).border(.gray)
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
- [static let bottom: VerticalAlignment](verticalalignment/bottom.md)
  A guide that marks the bottom edge of the view.
- [static let lastTextBaseline: VerticalAlignment](verticalalignment/lasttextbaseline.md)
  A guide that marks the bottom-most text baseline in a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/verticalalignment/firsttextbaseline)*