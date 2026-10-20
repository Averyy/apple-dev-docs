# SpotlightSearchTool.ContentDomain.Calendar

**Framework**: Core Spotlight  
**Kind**: struct  
**Role**: Structure

Attribute mapping for the calendar domain.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Calendar
```

## Topics

### Configuring the domain
- [init(organizer: [SearchableItemAttribute]?, attendees: [SearchableItemAttribute]?, location: [SearchableItemAttribute]?, date: [SearchableItemAttribute]?)](./calendar-swift.struct/init%28organizer,attendees,location,date%29.md)
### Getting the domain attributes
- [var attendees: [SearchableItemAttribute]?](./calendar-swift.struct/attendees.md)
  Attributes queried for attendees/participants. Default: [`participants`](../../searchableitemattribute/participants.md)
- [var date: [SearchableItemAttribute]?](./calendar-swift.struct/date.md)
  Attributes queried for the event date. Default: [`dueDate`](../../searchableitemattribute/duedate.md)
- [var location: [SearchableItemAttribute]?](./calendar-swift.struct/location.md)
  Attributes queried for the event location. Default: [`namedLocation`](../../searchableitemattribute/namedlocation.md), [`city`](../../searchableitemattribute/city.md), [`stateOrProvince`](../../searchableitemattribute/stateorprovince.md)
- [var organizer: [SearchableItemAttribute]?](./calendar-swift.struct/organizer.md)
  Attributes queried for the event organizer/host.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Getting the calendar domain
- [static var calendar: SpotlightSearchTool.ContentDomain](./calendar-swift.type.property.md)
  Calendar events, meetings, and scheduled items.
- [static func calendar(SpotlightSearchTool.ContentDomain.Calendar) -> SpotlightSearchTool.ContentDomain](./calendar%28_%29.md)
  Calendar events, meetings, and scheduled items with custom attribute mapping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/contentdomain/calendar-swift.struct)*