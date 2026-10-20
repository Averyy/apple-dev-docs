# reloadDecorations(forDateComponents:animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Reloads the decorations for the dates you provide, with an option to animate the decoration reload.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
func reloadDecorations(forDateComponents dates: [DateComponents], animated: Bool)
```

```objc
- (void) reloadDecorationsForDateComponents:(NSArray<NSDateComponents *> *) dates animated:(BOOL) animated;
```

## Parameters

- `dates`: An array of dates to reload that you provide as date components.
- `animated`: A Boolean value that indicates whether the calendar view should animate the decoration reload.

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
- [var wantsDateDecorations: Bool](./wantsdatedecorations.md)
  A Boolean value that indicates whether the calendar view displays date decorations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarview/reloaddecorations(fordatecomponents:animated:))*