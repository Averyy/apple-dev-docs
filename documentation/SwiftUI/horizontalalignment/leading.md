# leading

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

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

- [Building layouts with stack views](../building-layouts-with-stack-views.md)

## Discussion

Use this guide to align the leading edges of views. For a device that uses a left-to-right language, the leading edge is on the left:

![A box that contains the word, Leading. Vertical](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/HorizontalAlignment-leading-1-iOS@2x.png)

The following code generates the image above using a [`VStack`](../vstack.md):

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

### Getting guides
- [static let center: HorizontalAlignment](./center.md)
  A guide that marks the horizontal center of the view.
- [static let trailing: HorizontalAlignment](./trailing.md)
  A guide that marks the trailing edge of the view.
- [static let listRowSeparatorLeading: HorizontalAlignment](./listrowseparatorleading.md)
  A guide marking the leading edge of a `List` row separator.
- [static let listRowSeparatorTrailing: HorizontalAlignment](./listrowseparatortrailing.md)
  A guide marking the trailing edge of a `List` row separator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/horizontalalignment/leading)*