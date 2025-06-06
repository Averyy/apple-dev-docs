# init(calendarIdentifier:)

**Framework**: Foundation  
**Kind**: init

Initializes a calendar according to a given identifier.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(calendarIdentifier ident: NSCalendar.Identifier)
```

#### Return Value

The initialized calendar, or `nil` if the identifier is unknown (if, for example, it is either an unrecognized string or the calendar is not supported by the current version of the operating system).

## Parameters

- `ident`: The identifier for the new calendar. For valid identifiers, see  .

## See Also

- [var calendarIdentifier: NSCalendar.Identifier](nscalendar/calendaridentifier.md)
  An identifier for the calendar.
- [class var autoupdatingCurrent: Calendar](nscalendar/autoupdatingcurrent.md)
  A calendar that tracks changes to user’s preferred calendar.
- [init?(identifier: NSCalendar.Identifier)](nscalendar/init(identifier:).md)
  Creates a new calendar specified by a given identifier.
- [NSCalendar.Identifier](nscalendar/identifier.md)
  The supported calendar types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscalendar/init(calendaridentifier:))*