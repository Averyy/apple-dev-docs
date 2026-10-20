# NSCalendar.Identifier

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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

```c
typedef NSString * NSCalendarIdentifier;
```

#### Discussion

Use these identifiers to specify the kind of calendar. The Gregorian calendar is the calendar typically used in Europe, the Western Hemisphere, and elsewhere.

## Topics

### Initializers
- [init(String)](./identifier/init%28_%29.md)
- [init(rawValue: String)](./identifier/init%28rawvalue%29.md)
### Calendar identifiers
- [static let gregorian: NSCalendar.Identifier](./identifier/gregorian.md)
  Identifier for the Gregorian calendar.
- [static let ISO8601: NSCalendar.Identifier](./identifier/iso8601.md)
  Identifier for the ISO8601 calendar.
- [static let bangla: NSCalendar.Identifier](./identifier/bangla.md)
- [static let buddhist: NSCalendar.Identifier](./identifier/buddhist.md)
  Identifier for the Buddhist calendar.
- [static let chinese: NSCalendar.Identifier](./identifier/chinese.md)
  Identifier for the Chinese calendar.
- [static let coptic: NSCalendar.Identifier](./identifier/coptic.md)
  Identifier for the Coptic calendar.
- [static let dangi: NSCalendar.Identifier](./identifier/dangi.md)
- [static let ethiopicAmeteAlem: NSCalendar.Identifier](./identifier/ethiopicametealem.md)
  Identifier for the Ethiopic (Amete Alem) calendar.
- [static let ethiopicAmeteMihret: NSCalendar.Identifier](./identifier/ethiopicametemihret.md)
  Identifier for the Ethiopic (Amete Mihret) calendar.
- [static let gujarati: NSCalendar.Identifier](./identifier/gujarati.md)
- [static let hebrew: NSCalendar.Identifier](./identifier/hebrew.md)
  Identifier for the Hebrew calendar.
- [static let indian: NSCalendar.Identifier](./identifier/indian.md)
  Identifier for the Indian calendar.
- [static let islamic: NSCalendar.Identifier](./identifier/islamic.md)
  Identifier for the Islamic calendar.
- [static let islamicCivil: NSCalendar.Identifier](./identifier/islamiccivil.md)
  Identifier for the Islamic civil calendar.
- [static let islamicTabular: NSCalendar.Identifier](./identifier/islamictabular.md)
  Identifier for a tabular Islamic calendar.
- [static let islamicUmmAlQura: NSCalendar.Identifier](./identifier/islamicummalqura.md)
  Identifier for the Islamic Umm al-Qura calendar.
- [static let japanese: NSCalendar.Identifier](./identifier/japanese.md)
  Identifier for the Japanese calendar.
- [static let kannada: NSCalendar.Identifier](./identifier/kannada.md)
- [static let malayalam: NSCalendar.Identifier](./identifier/malayalam.md)
- [static let marathi: NSCalendar.Identifier](./identifier/marathi.md)
- [static let odia: NSCalendar.Identifier](./identifier/odia.md)
- [static let persian: NSCalendar.Identifier](./identifier/persian.md)
  Identifier for the Persian calendar.
- [static let republicOfChina: NSCalendar.Identifier](./identifier/republicofchina.md)
  Identifier for the Republic of China calendar.
- [static let tamil: NSCalendar.Identifier](./identifier/tamil.md)
- [static let telugu: NSCalendar.Identifier](./identifier/telugu.md)
- [static let vietnamese: NSCalendar.Identifier](./identifier/vietnamese.md)
- [static let vikram: NSCalendar.Identifier](./identifier/vikram.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating and Initializing Calendars
- [init?(identifier: NSCalendar.Identifier)](./init%28identifier%29.md)
  Creates a new calendar specified by a given identifier.
- [init?(calendarIdentifier: NSCalendar.Identifier)](./init%28calendaridentifier%29.md)
  Initializes a calendar according to a given identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscalendar/identifier)*