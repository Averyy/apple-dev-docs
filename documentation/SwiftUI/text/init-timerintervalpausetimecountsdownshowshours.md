# init(timerInterval:pauseTime:countsDown:showsHours:)

**Framework**: SwiftUI  
**Kind**: init

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

## Parameters

- `timerInterval`: The interval between where to run the timer.
- `pauseTime`: If present, the date at which to pause the timer.   The default is   which indicates to never pause.
- `countsDown`: Whether to count up or down. The default is  .
- `showsHours`: Whether to include an hours component if there are   more than 60 minutes left on the timer. The default is  .

## See Also

- [init(LocalizedStringKey, tableName: String?, bundle: Bundle?, comment: StaticString?)](text/init(_:tablename:bundle:comment:).md)
  Creates a text view that displays localized content identified by a key.
- [init(_:)](text/init(_:).md)
  Creates a text view that displays styled attributed content.
- [init(verbatim: String)](text/init(verbatim:).md)
  Creates a text view that displays a string literal without localization.
- [init(Date, style: Text.DateStyle)](text/init(_:style:).md)
  Creates an instance that displays localized dates and times using a specific style.
- [init(_:format:)](text/init(_:format:).md)
  Creates a text view that displays the formatted representation of a nonstring type supported by a corresponding format style.
- [init(_:formatter:)](text/init(_:formatter:).md)
  Creates a text view that displays the formatted representation of a Foundation object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/init(timerinterval:pausetime:countsdown:showshours:))*