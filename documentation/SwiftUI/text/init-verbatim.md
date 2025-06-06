# init(verbatim:)

**Framework**: SwiftUI  
**Kind**: init

Creates a text view that displays a string literal without localization.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(verbatim content: String)
```

#### Discussion

Use this initializer to create a text view with a string literal without performing localization:

```swift
Text(verbatim: "pencil") // Displays the string "pencil" in any locale.
```

If you want to localize a string literal before displaying it, use the [`init(_:tableName:bundle:comment:)`](text/init(_:tablename:bundle:comment:).md) initializer instead. If you want to display a string variable, use the [`init(_:)`](text/init(_:)-9d1g4.md) initializer, which also bypasses localization.

## Parameters

- `content`: A string to display without localization.

## See Also

- [init(LocalizedStringKey, tableName: String?, bundle: Bundle?, comment: StaticString?)](text/init(_:tablename:bundle:comment:).md)
  Creates a text view that displays localized content identified by a key.
- [init(_:)](text/init(_:).md)
  Creates a text view that displays styled attributed content.
- [init(Date, style: Text.DateStyle)](text/init(_:style:).md)
  Creates an instance that displays localized dates and times using a specific style.
- [init(_:format:)](text/init(_:format:).md)
  Creates a text view that displays the formatted representation of a nonstring type supported by a corresponding format style.
- [init(_:formatter:)](text/init(_:formatter:).md)
  Creates a text view that displays the formatted representation of a Foundation object.
- [init(timerInterval: ClosedRange<Date>, pauseTime: Date?, countsDown: Bool, showsHours: Bool)](text/init(timerinterval:pausetime:countsdown:showshours:).md)
  Creates an instance that displays a timer counting within the provided interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/init(verbatim:))*