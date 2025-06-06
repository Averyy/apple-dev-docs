# preferredMaxLayoutWidth

**Framework**: UIKit  
**Kind**: property

The preferred maximum width, in points, for a multiline label.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var preferredMaxLayoutWidth: CGFloat { get set }
```

#### Discussion

This property affects the size of the label when the system applies layout constraints to it. During layout, if the text extends beyond the width specified by this property, the additional text flows to one or more new lines, increasing the height of the label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilabel/preferredmaxlayoutwidth)*