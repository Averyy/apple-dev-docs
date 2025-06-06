# image(_:color:size:)

**Framework**: UIKit  
**Kind**: method

Creates a new calendar view decoration with the image, color, and size that you specify.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency static func image(_ image: UIImage?, color: UIColor? = nil, size: UICalendarView.DecorationSize = .medium) -> UICalendarView.Decoration
```

#### Return Value

A calendar view decoration.

#### Discussion

The image defaults to `circlebadge.fill` if you don’t specify it.

The color defaults to [`systemFill`](uicolor/systemfill.md) if you don’t specify it.

The size defaults to [`UICalendarView.DecorationSize.medium`](uicalendarview/decorationsize/medium.md) if nil.

## Parameters

- `image`: An image to display as the decoration.
- `color`: A color for the decoration.
- `size`: A relative size for the decoration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarview/decoration/image(_:color:size:))*