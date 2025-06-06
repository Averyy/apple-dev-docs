# lastTextBaseline

**Framework**: SwiftUI  
**Kind**: property

A guide that marks the bottom-most text baseline in a view.

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
static let lastTextBaseline: VerticalAlignment
```

#### Discussion

Use this guide to align with the baseline of the bottom-most text in a view. The guide aligns with the bottom of a view that contains no text.

![A box that contains the text, Last Text Baseline.](https://docs-assets.developer.apple.com/published/f5faacd72c9610f5feadce01aa0a1c5a/VerticalAlignment-lastTextBaseline-1-iOS%402x.png)

The following code generates the image above using an [`HStack`](hstack.md):

```swift
struct VerticalAlignmentLastTextBaseline: View {
    var body: some View {
        HStack(alignment: .lastTextBaseline, spacing: 0) {
            Color.red.frame(height: 1)
            Text("Last Text Baseline").font(.title).border(.gray)
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
- [static let firstTextBaseline: VerticalAlignment](verticalalignment/firsttextbaseline.md)
  A guide that marks the top-most text baseline in a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/verticalalignment/lasttextbaseline)*