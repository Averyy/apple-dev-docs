# UICalendarView.DecorationSize

**Framework**: UIKit  
**Kind**: enum

Constants that indicate the relative size of a decoration in a calendar view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
enum DecorationSize
```

## Topics

### Decoration View Sizes
- [UICalendarView.DecorationSize.large](uicalendarview/decorationsize/large.md)
  A large relative decoration size in a calendar view.
- [UICalendarView.DecorationSize.medium](uicalendarview/decorationsize/medium.md)
  A medium relative decoration size in a calendar view.
- [UICalendarView.DecorationSize.small](uicalendarview/decorationsize/small.md)
  A small relative decoration size in a calendar view.
### Initializers
- [init?(rawValue: Int)](uicalendarview/decorationsize/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var fontDesign: UIFontDescriptor.SystemDesign](uicalendarview/fontdesign.md)
  A font design that the calendar view uses for displaying calendar text.
- [var delegate: (any UICalendarViewDelegate)?](uicalendarview/delegate.md)
  A delegate object the calendar view calls for decoration views.
- [protocol UICalendarViewDelegate](uicalendarviewdelegate.md)
  An object that a calendar view uses to display decorations for dates.
- [UICalendarView.Decoration](uicalendarview/decoration.md)
  A view that a calendar view displays for a specific date.
- [var wantsDateDecorations: Bool](uicalendarview/wantsdatedecorations.md)
  A Boolean value that indicates whether the calendar view displays date decorations.
- [func reloadDecorations(forDateComponents: [DateComponents], animated: Bool)](uicalendarview/reloaddecorations(fordatecomponents:animated:).md)
  Reloads the decorations for the dates you provide, with an option to animate the decoration reload.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarview/decorationsize)*