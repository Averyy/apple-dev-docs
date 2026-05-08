# centerLastTextBaseline

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
static var centerLastTextBaseline: Alignment { get }
```

#### Discussion

This alignment combines the [`center`](horizontalalignment/center.md) horizontal guide and the [`lastTextBaseline`](verticalalignment/lasttextbaseline.md) vertical guide:

![A square that’s divided into four equal quadrants. The upper-](https://docs-assets.developer.apple.com/published/721a60b87f43a3e8cd5342720b6b0770/Alignment-centerLastTextBaseline-1-iOS%402x.png)

## See Also

- [static var leadingFirstTextBaseline: Alignment](alignment/leadingfirsttextbaseline.md)
  A guide that marks the leading edge and top-most text baseline in a view.
- [static var centerFirstTextBaseline: Alignment](alignment/centerfirsttextbaseline.md)
  A guide that marks the top-most text baseline in a view.
- [static var trailingFirstTextBaseline: Alignment](alignment/trailingfirsttextbaseline.md)
  A guide that marks the trailing edge and top-most text baseline in a view.
- [static var leadingLastTextBaseline: Alignment](alignment/leadinglasttextbaseline.md)
  A guide that marks the leading edge and bottom-most text baseline in a view.
- [static var trailingLastTextBaseline: Alignment](alignment/trailinglasttextbaseline.md)
  A guide that marks the trailing edge and bottom-most text baseline in a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/alignment/centerlasttextbaseline)*