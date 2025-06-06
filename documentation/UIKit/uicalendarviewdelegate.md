# UICalendarViewDelegate

**Framework**: UIKit  
**Kind**: protocol

An object that a calendar view uses to display decorations for dates.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UICalendarViewDelegate : NSObjectProtocol
```

## Topics

### Providing calendar view decorations
- [func calendarView(UICalendarView, decorationFor: DateComponents) -> UICalendarView.Decoration?](uicalendarviewdelegate/calendarview(_:decorationfor:).md)
  Creates a calendar view decoration for the date represented by the date components you provide.
### Instance Methods
- [func calendarView(UICalendarView, didChangeVisibleDateComponentsFrom: DateComponents)](uicalendarviewdelegate/calendarview(_:didchangevisibledatecomponentsfrom:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var fontDesign: UIFontDescriptor.SystemDesign](uicalendarview/fontdesign.md)
  A font design that the calendar view uses for displaying calendar text.
- [var delegate: (any UICalendarViewDelegate)?](uicalendarview/delegate.md)
  A delegate object the calendar view calls for decoration views.
- [UICalendarView.Decoration](uicalendarview/decoration.md)
  A view that a calendar view displays for a specific date.
- [UICalendarView.DecorationSize](uicalendarview/decorationsize.md)
  Constants that indicate the relative size of a decoration in a calendar view.
- [var wantsDateDecorations: Bool](uicalendarview/wantsdatedecorations.md)
  A Boolean value that indicates whether the calendar view displays date decorations.
- [func reloadDecorations(forDateComponents: [DateComponents], animated: Bool)](uicalendarview/reloaddecorations(fordatecomponents:animated:).md)
  Reloads the decorations for the dates you provide, with an option to animate the decoration reload.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarviewdelegate)*