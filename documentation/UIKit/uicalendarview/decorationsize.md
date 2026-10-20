# UICalendarView.DecorationSize

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum UICalendarViewDecorationSize : NSInteger;
```

## Topics

### Decoration View Sizes
- [UICalendarView.DecorationSize.large](./decorationsize/large.md)
  A large relative decoration size in a calendar view.
- [UICalendarView.DecorationSize.medium](./decorationsize/medium.md)
  A medium relative decoration size in a calendar view.
- [UICalendarView.DecorationSize.small](./decorationsize/small.md)
  A small relative decoration size in a calendar view.
### Initializers
- [init?(rawValue: Int)](./decorationsize/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

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
- [var wantsDateDecorations: Bool](./wantsdatedecorations.md)
  A Boolean value that indicates whether the calendar view displays date decorations.
- [func reloadDecorations(forDateComponents: [DateComponents], animated: Bool)](./reloaddecorations%28fordatecomponents,animated%29.md)
  Reloads the decorations for the dates you provide, with an option to animate the decoration reload.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarview/decorationsize)*