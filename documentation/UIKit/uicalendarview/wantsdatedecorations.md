# wantsDateDecorations

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the calendar view displays date decorations.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
var wantsDateDecorations: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL wantsDateDecorations;
```

## Discussion

Defaults to [`true`](../../Swift/true.md). You must implement `UICalendarDateDelegate`’s [`calendarView(_:decorationFor:)`](../uicalendarviewdelegate/calendarview%28_,decorationfor%29.md) to provide decorations that the calendar view shows.

## See Also

### Customizing the calendar display
- [var fontDesign: UIFontDescriptor.SystemDesign](./fontdesign.md)
  A font design that the calendar view uses for displaying calendar text.
- [var delegate: (any UICalendarViewDelegate)?](./delegate.md)
  A delegate object the calendar view calls for decoration views.
- [protocol UICalendarViewDelegate](../uicalendarviewdelegate.md)
  An object that a calendar view uses to display decorations for dates.
- [UICalendarView.Decoration](./decoration.md)
  A view that a calendar view displays for a specific date.
- [UICalendarView.DecorationSize](./decorationsize.md)
  Constants that indicate the relative size of a decoration in a calendar view.
- [func reloadDecorations(forDateComponents: [DateComponents], animated: Bool)](./reloaddecorations%28fordatecomponents,animated%29.md)
  Reloads the decorations for the dates you provide, with an option to animate the decoration reload.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarview/wantsdatedecorations)*