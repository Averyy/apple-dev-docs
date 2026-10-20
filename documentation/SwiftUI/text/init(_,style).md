# init(_:style:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates an instance that displays localized dates and times using a specific style.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init(_ date: Date, style: Text.DateStyle)
```

#### Discussion

> **Note**: In a widget, a `Text` that uses the [`relative`](./datestyle/relative.md), [`offset`](./datestyle/offset.md), or [`timer`](./datestyle/timer.md) style becomes horizontally flexible and expands to fill the available width. Widgets can’t perform layout again after the system archives them, so the text can’t measure itself against its eventual content, which changes as the date updates, without risking clipping. If you want to constrain the width, apply a [`frame(width:height:alignment:)`](../view/frame%28width,height,alignment%29.md) modifier, and use [`multilineTextAlignment(_:)`](../view/multilinetextalignment%28_%29.md) to align the text within that frame.

## Parameters

- `date`: The target date to display.
- `style`: The style used when displaying a date.

## See Also

### Creating a text view
- [init(LocalizedStringKey, tableName: String?, bundle: Bundle?, comment: StaticString?)](./init%28_,tablename,bundle,comment%29.md)
  Creates a text view that displays localized content identified by a key.
- [init(_:)](./init%28_%29.md)
  Creates a text view that displays styled attributed content.
- [init(verbatim: String)](./init%28verbatim%29.md)
  Creates a text view that displays a string literal without localization.
- [init(_:format:)](./init%28_,format%29.md)
  Creates a text view that displays the formatted representation of a nonstring type supported by a corresponding format style.
- [init(_:formatter:)](./init%28_,formatter%29.md)
  Creates a text view that displays the formatted representation of a Foundation object.
- [init(timerInterval: ClosedRange<Date>, pauseTime: Date?, countsDown: Bool, showsHours: Bool)](./init%28timerinterval,pausetime,countsdown,showshours%29.md)
  Creates an instance that displays a timer counting within the provided interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/init(_:style:))*