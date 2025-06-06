# default(color:size:)

**Framework**: UIKit  
**Kind**: method

Creates a default calendar view decoration with a filled circle image, using the color and size you specify.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency static func `default`(color: UIColor? = nil, size: UICalendarView.DecorationSize = .medium) -> UICalendarView.Decoration
```

#### Return Value

A calendar view decoration.

## Parameters

- `color`: A color for the decoration.
- `size`: A relative size for the decoration.

## See Also

- [init()](uicalendarview/decoration/init.md)
  Creates a default calendar view decoration with a filled circle image, using the system fill color and medium size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarview/decoration/default(color:size:))*