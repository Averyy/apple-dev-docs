# init(verbatim:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

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

If you want to localize a string literal before displaying it, use the [`init(_:tableName:bundle:comment:)`](./init%28_,tablename,bundle,comment%29.md) initializer instead. If you want to display a string variable, use the [`init(_:)`](./init%28_%29-9d1g4.md) initializer, which also bypasses localization.

## Parameters

- `content`: A string to display without localization.

## See Also

### Creating a text view
- [init(LocalizedStringKey, tableName: String?, bundle: Bundle?, comment: StaticString?)](./init%28_,tablename,bundle,comment%29.md)
  Creates a text view that displays localized content identified by a key.
- [init(_:)](./init%28_%29.md)
  Creates a text view that displays styled attributed content.
- [init(Date, style: Text.DateStyle)](./init%28_,style%29.md)
  Creates an instance that displays localized dates and times using a specific style.
- [init(_:format:)](./init%28_,format%29.md)
  Creates a text view that displays the formatted representation of a nonstring type supported by a corresponding format style.
- [init(_:formatter:)](./init%28_,formatter%29.md)
  Creates a text view that displays the formatted representation of a Foundation object.
- [init(timerInterval: ClosedRange<Date>, pauseTime: Date?, countsDown: Bool, showsHours: Bool)](./init%28timerinterval,pausetime,countsdown,showshours%29.md)
  Creates an instance that displays a timer counting within the provided interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/init(verbatim:))*