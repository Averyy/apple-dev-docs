# wantsDateDecorations

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the calendar view displays date decorations.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var wantsDateDecorations: Bool { get set }
```

#### Discussion

Defaults to [`true`](https://developer.apple.com/documentation/Swift/true). You must implement `UICalendarDateDelegate`’s [`calendarView(_:decorationFor:)`](uicalendarviewdelegate/calendarview(_:decorationfor:).md) to provide decorations that the calendar view shows.

## See Also

- [var fontDesign: UIFontDescriptor.SystemDesign](uicalendarview/fontdesign.md)
  A font design that the calendar view uses for displaying calendar text.
- [var delegate: (any UICalendarViewDelegate)?](uicalendarview/delegate.md)
  A delegate object the calendar view calls for decoration views.
- [protocol UICalendarViewDelegate](uicalendarviewdelegate.md)
  An object that a calendar view uses to display decorations for dates.
- [UICalendarView.Decoration](uicalendarview/decoration.md)
  A view that a calendar view displays for a specific date.
- [UICalendarView.DecorationSize](uicalendarview/decorationsize.md)
  Constants that indicate the relative size of a decoration in a calendar view.
- [func reloadDecorations(forDateComponents: [DateComponents], animated: Bool)](uicalendarview/reloaddecorations(fordatecomponents:animated:).md)
  Reloads the decorations for the dates you provide, with an option to animate the decoration reload.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarview/wantsdatedecorations)*