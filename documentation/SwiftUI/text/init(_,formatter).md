# init(_:formatter:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a text view that displays the formatted representation of a Foundation object.

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
init<Subject>(_ subject: Subject, formatter: Formatter) where Subject : NSObject
```

**Other overloads**:

```swift
init<Subject>(_ subject: Subject, formatter: Formatter) where Subject : ReferenceConvertible
```

## Discussion

Use this initializer to create a text view that formats `subject` using `formatter`.

## Parameters

- `subject`: An [`NSObject`](../../ObjectiveC/nsobject-swift.class.md) instance compatible with `formatter`.
- `formatter`: A [`Formatter`](../../Foundation/formatter.md) capable of converting `subject` into a string representation.

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
- [init(timerInterval: ClosedRange<Date>, pauseTime: Date?, countsDown: Bool, showsHours: Bool)](./init%28timerinterval,pausetime,countsdown,showshours%29.md)
  Creates an instance that displays a timer counting within the provided interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/init(_:formatter:))*