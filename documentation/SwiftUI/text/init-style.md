# init(_:style:)

**Framework**: SwiftUI  
**Kind**: init

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

## Parameters

- `date`: The target date to display.
- `style`: The style used when displaying a date.

## See Also

- [init(LocalizedStringKey, tableName: String?, bundle: Bundle?, comment: StaticString?)](text/init(_:tablename:bundle:comment:).md)
  Creates a text view that displays localized content identified by a key.
- [init(_:)](text/init(_:).md)
  Creates a text view that displays styled attributed content.
- [init(verbatim: String)](text/init(verbatim:).md)
  Creates a text view that displays a string literal without localization.
- [init(_:format:)](text/init(_:format:).md)
  Creates a text view that displays the formatted representation of a nonstring type supported by a corresponding format style.
- [init(_:formatter:)](text/init(_:formatter:).md)
  Creates a text view that displays the formatted representation of a Foundation object.
- [init(timerInterval: ClosedRange<Date>, pauseTime: Date?, countsDown: Bool, showsHours: Bool)](text/init(timerinterval:pausetime:countsdown:showshours:).md)
  Creates an instance that displays a timer counting within the provided interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/init(_:style:))*