# leadingLastTextBaseline

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

A guide that marks the leading edge and bottom-most text baseline in a view.

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
@export(implementation)
static var leadingLastTextBaseline: Alignment { get }
```

#### Discussion

This alignment combines the [`leading`](../horizontalalignment/leading.md) horizontal guide and the [`lastTextBaseline`](../verticalalignment/lasttextbaseline.md) vertical guide:

![A square that’s divided into four equal quadrants. The upper-](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/Alignment-leadingLastTextBaseline-1-iOS@2x.png)

## See Also

### Getting text baseline guides
- [static var leadingFirstTextBaseline: Alignment](./leadingfirsttextbaseline.md)
  A guide that marks the leading edge and top-most text baseline in a view.
- [static var centerFirstTextBaseline: Alignment](./centerfirsttextbaseline.md)
  A guide that marks the top-most text baseline in a view.
- [static var trailingFirstTextBaseline: Alignment](./trailingfirsttextbaseline.md)
  A guide that marks the trailing edge and top-most text baseline in a view.
- [static var centerLastTextBaseline: Alignment](./centerlasttextbaseline.md)
  A guide that marks the bottom-most text baseline in a view.
- [static var trailingLastTextBaseline: Alignment](./trailinglasttextbaseline.md)
  A guide that marks the trailing edge and bottom-most text baseline in a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/alignment/leadinglasttextbaseline)*