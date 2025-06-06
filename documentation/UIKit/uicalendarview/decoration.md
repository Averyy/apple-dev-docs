# UICalendarView.Decoration

**Framework**: UIKit  
**Kind**: class

A view that a calendar view displays for a specific date.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class Decoration
```

## Topics

### Creating a Default Decoration View
- [init()](uicalendarview/decoration/init.md)
  Creates a default calendar view decoration with a filled circle image, using the system fill color and medium size.
- [static func `default`(color: UIColor?, size: UICalendarView.DecorationSize) -> UICalendarView.Decoration](uicalendarview/decoration/default(color:size:).md)
  Creates a default calendar view decoration with a filled circle image, using the color and size you specify.
### Creating a Custom Decoration View
- [class func customView(() -> UIView) -> Self](uicalendarview/decoration/customview(_:).md)
  Creates a new calendar view decoration with a custom view, using your view provider.
### Creating Image Decoration Views
- [static func image(UIImage?, color: UIColor?, size: UICalendarView.DecorationSize) -> UICalendarView.Decoration](uicalendarview/decoration/image(_:color:size:).md)
  Creates a new calendar view decoration with the image, color, and size that you specify.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var fontDesign: UIFontDescriptor.SystemDesign](uicalendarview/fontdesign.md)
  A font design that the calendar view uses for displaying calendar text.
- [var delegate: (any UICalendarViewDelegate)?](uicalendarview/delegate.md)
  A delegate object the calendar view calls for decoration views.
- [protocol UICalendarViewDelegate](uicalendarviewdelegate.md)
  An object that a calendar view uses to display decorations for dates.
- [UICalendarView.DecorationSize](uicalendarview/decorationsize.md)
  Constants that indicate the relative size of a decoration in a calendar view.
- [var wantsDateDecorations: Bool](uicalendarview/wantsdatedecorations.md)
  A Boolean value that indicates whether the calendar view displays date decorations.
- [func reloadDecorations(forDateComponents: [DateComponents], animated: Bool)](uicalendarview/reloaddecorations(fordatecomponents:animated:).md)
  Reloads the decorations for the dates you provide, with an option to animate the decoration reload.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarview/decoration)*