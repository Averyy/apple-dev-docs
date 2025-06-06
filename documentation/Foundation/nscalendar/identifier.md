# NSCalendar.Identifier

**Framework**: Foundation  
**Kind**: struct

The supported calendar types.

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
struct Identifier
```

#### Discussion

Use these identifiers to specify the kind of calendar. The Gregorian calendar is the calendar typically used in Europe, the Western Hemisphere, and elsewhere.

## Topics

### Initializers
- [init(String)](nscalendar/identifier/init(_:).md)
- [init(rawValue: String)](nscalendar/identifier/init(rawvalue:).md)
### Type Properties
- [static let gregorian: NSCalendar.Identifier](nscalendar/identifier/gregorian.md)
  Identifier for the Gregorian calendar.
- [static let ISO8601: NSCalendar.Identifier](nscalendar/identifier/iso8601.md)
  Identifier for the ISO8601 calendar.
- [static let buddhist: NSCalendar.Identifier](nscalendar/identifier/buddhist.md)
  Identifier for the Buddhist calendar.
- [static let chinese: NSCalendar.Identifier](nscalendar/identifier/chinese.md)
  Identifier for the Chinese calendar.
- [static let coptic: NSCalendar.Identifier](nscalendar/identifier/coptic.md)
  Identifier for the Coptic calendar.
- [static let ethiopicAmeteAlem: NSCalendar.Identifier](nscalendar/identifier/ethiopicametealem.md)
  Identifier for the Ethiopic (Amete Alem) calendar.
- [static let ethiopicAmeteMihret: NSCalendar.Identifier](nscalendar/identifier/ethiopicametemihret.md)
  Identifier for the Ethiopic (Amete Mihret) calendar.
- [static let hebrew: NSCalendar.Identifier](nscalendar/identifier/hebrew.md)
  Identifier for the Hebrew calendar.
- [static let indian: NSCalendar.Identifier](nscalendar/identifier/indian.md)
  Identifier for the Indian calendar.
- [static let islamic: NSCalendar.Identifier](nscalendar/identifier/islamic.md)
  Identifier for the Islamic calendar.
- [static let islamicCivil: NSCalendar.Identifier](nscalendar/identifier/islamiccivil.md)
  Identifier for the Islamic civil calendar.
- [static let islamicTabular: NSCalendar.Identifier](nscalendar/identifier/islamictabular.md)
  Identifier for a tabular Islamic calendar.
- [static let islamicUmmAlQura: NSCalendar.Identifier](nscalendar/identifier/islamicummalqura.md)
  Identifier for the Islamic Umm al-Qura calendar.
- [static let japanese: NSCalendar.Identifier](nscalendar/identifier/japanese.md)
  Identifier for the Japanese calendar.
- [static let persian: NSCalendar.Identifier](nscalendar/identifier/persian.md)
  Identifier for the Persian calendar.
- [static let republicOfChina: NSCalendar.Identifier](nscalendar/identifier/republicofchina.md)
  Identifier for the Republic of China calendar.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [init?(identifier: NSCalendar.Identifier)](nscalendar/init(identifier:).md)
  Creates a new calendar specified by a given identifier.
- [init?(calendarIdentifier: NSCalendar.Identifier)](nscalendar/init(calendaridentifier:).md)
  Initializes a calendar according to a given identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscalendar/identifier)*