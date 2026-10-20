# init(timerInterval:pauseTime:countsDown:showsHours:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates an instance that displays a timer counting within the provided interval.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init(timerInterval: ClosedRange<Date>, pauseTime: Date? = nil, countsDown: Bool = true, showsHours: Bool = true)
```

#### Discussion

```swift
Text(
    timerInterval: Date.now...Date(timeInterval: 12 * 60, since: .now),
    pauseTime: Date.now + (10 * 60))
```

The example above shows a text that displays a timer counting down from “12:00” and will pause when reaching “10:00”.

> **Note**: In a widget, this `Text` becomes horizontally flexible and expands to fill the available width, because its content keeps changing as the timer counts. Widgets can’t perform layout again after the system archives them, so the text can’t measure itself against its eventual content without risking clipping. If you want to constrain the width, apply a [`frame(width:height:alignment:)`](../view/frame%28width,height,alignment%29.md) modifier, and use [`multilineTextAlignment(_:)`](../view/multilinetextalignment%28_%29.md) to align the text within that frame.

## Parameters

- `timerInterval`: The interval between where to run the timer.
- `pauseTime`: If present, the date at which to pause the timer. The default is `nil` which indicates to never pause.
- `countsDown`: Whether to count up or down. The default is `true`.
- `showsHours`: Whether to include an hours component if there are more than 60 minutes left on the timer. The default is `true`.

## See Also

### Creating a text view
- [init(LocalizedStringKey, tableName: String?, bundle: Bundle?, comment: StaticString?)](./init%28_,tablename,bundle,comment%29.md)
  Creates a text view that displays localized content identified by a key.
- [init(_:)](./init%28_%29.md)
  Creates a text view that displays styled attributed content.
- [init(verbatim: String)](./init%28verbatim%29.md)
  Creates a text view that displays a string literal without localization.
- [init(Date, style: Text.DateStyle)](./init%28_,style%29.md)
  Creates an instance that displays localized dates and times using a specific style.
- [init(_:format:)](./init%28_,format%29.md)
  Creates a text view that displays the formatted representation of a nonstring type supported by a corresponding format style.
- [init(_:formatter:)](./init%28_,formatter%29.md)
  Creates a text view that displays the formatted representation of a Foundation object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/init(timerinterval:pausetime:countsdown:showshours:))*