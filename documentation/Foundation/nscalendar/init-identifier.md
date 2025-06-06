# init(identifier:)

**Framework**: Foundation  
**Kind**: init

Creates a new calendar specified by a given identifier.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(identifier calendarIdentifierConstant: NSCalendar.Identifier)
```

#### Return Value

The initialized calendar, or `nil` if the identifier is unknown (if, for example, it is either an unrecognized string or the calendar is not supported by the current version of the operating system).

#### Discussion

The returned calendar defaults to the current locale and default time zone.

## Parameters

- `calendarIdentifierConstant`: The identifier for the new calendar. For valid identifiers, see  .

## See Also

- [var calendarIdentifier: NSCalendar.Identifier](nscalendar/calendaridentifier.md)
  An identifier for the calendar.
- [class var autoupdatingCurrent: Calendar](nscalendar/autoupdatingcurrent.md)
  A calendar that tracks changes to user’s preferred calendar.
- [init?(calendarIdentifier: NSCalendar.Identifier)](nscalendar/init(calendaridentifier:).md)
  Initializes a calendar according to a given identifier.
- [NSCalendar.Identifier](nscalendar/identifier.md)
  The supported calendar types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscalendar/init(identifier:))*