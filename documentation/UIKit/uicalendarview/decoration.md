# UICalendarView.Decoration

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface UICalendarViewDecoration : NSObject
```

## Topics

### Creating a Default Decoration View
- [init()](./decoration/init%28%29.md)
  Creates a default calendar view decoration with a filled circle image, using the system fill color and medium size.
- [static func `default`(color: UIColor?, size: UICalendarView.DecorationSize) -> UICalendarView.Decoration](./decoration/default%28color,size%29.md)
  Creates a default calendar view decoration with a filled circle image, using the color and size you specify.
- [+ decorationWithColor:size:](../uicalendarviewdecoration/decorationwithcolor_size_.md)
  Creates a new calendar view decoration with a filled circle image, using the color and size that you specify.
### Creating a Custom Decoration View
- [class func customView(() -> UIView) -> Self](./decoration/customview%28_%29.md)
  Creates a new calendar view decoration with a custom view, using your view provider.
- [- initWithCustomViewProvider:](../uicalendarviewdecoration/initwithcustomviewprovider_.md)
  Creates a new calendar view decoration with a custom view, using your view provider.
### Creating Image Decoration Views
- [static func image(UIImage?, color: UIColor?, size: UICalendarView.DecorationSize) -> UICalendarView.Decoration](./decoration/image%28_,color,size%29.md)
  Creates a new calendar view decoration with the image, color, and size that you specify.
- [- initWithImage:color:size:](../uicalendarviewdecoration/initwithimage_color_size_.md)
  Creates a new calendar view decoration with the image, color, and size that you specify.
- [+ decorationWithImage:](../uicalendarviewdecoration/decorationwithimage_.md)
  Creates a new calendar view decoration with the image you specify, using the system fill color and medium relative size.
- [+ decorationWithImage:color:size:](../uicalendarviewdecoration/decorationwithimage_color_size_.md)
  Creates a new calendar view decoration with the image, color, and size that you specify.
### Initializers
- [convenience init(customViewProvider: () -> UIView)](./decoration/init%28customviewprovider%29.md)

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../../Swift/sendable.md)

## See Also

### Customizing the calendar display
- [var fontDesign: UIFontDescriptor.SystemDesign](./fontdesign.md)
  A font design that the calendar view uses for displaying calendar text.
- [var delegate: (any UICalendarViewDelegate)?](./delegate.md)
  A delegate object the calendar view calls for decoration views.
- [protocol UICalendarViewDelegate](../uicalendarviewdelegate.md)
  An object that a calendar view uses to display decorations for dates.
- [UICalendarView.DecorationSize](./decorationsize.md)
  Constants that indicate the relative size of a decoration in a calendar view.
- [var wantsDateDecorations: Bool](./wantsdatedecorations.md)
  A Boolean value that indicates whether the calendar view displays date decorations.
- [func reloadDecorations(forDateComponents: [DateComponents], animated: Bool)](./reloaddecorations%28fordatecomponents,animated%29.md)
  Reloads the decorations for the dates you provide, with an option to animate the decoration reload.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarview/decoration)*