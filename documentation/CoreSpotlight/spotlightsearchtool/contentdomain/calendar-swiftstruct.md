# SpotlightSearchTool.ContentDomain.Calendar

**Framework**: Core Spotlight  
**Kind**: struct

Attribute mapping for the calendar domain.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Calendar
```

## Topics

### Configuring the domain
- [init(organizer: [SearchableItemAttribute]?, attendees: [SearchableItemAttribute]?, location: [SearchableItemAttribute]?, date: [SearchableItemAttribute]?)](spotlightsearchtool/contentdomain/calendar-swift.struct/init(organizer:attendees:location:date:).md)
### Getting the domain attributes
- [var attendees: [SearchableItemAttribute]?](spotlightsearchtool/contentdomain/calendar-swift.struct/attendees.md)
  Attributes queried for attendees/participants. Default: [`participants`](searchableitemattribute/participants.md)
- [var date: [SearchableItemAttribute]?](spotlightsearchtool/contentdomain/calendar-swift.struct/date.md)
  Attributes queried for the event date. Default: [`dueDate`](searchableitemattribute/duedate.md)
- [var location: [SearchableItemAttribute]?](spotlightsearchtool/contentdomain/calendar-swift.struct/location.md)
  Attributes queried for the event location. Default: [`namedLocation`](searchableitemattribute/namedlocation.md), [`city`](searchableitemattribute/city.md), [`stateOrProvince`](searchableitemattribute/stateorprovince.md)
- [var organizer: [SearchableItemAttribute]?](spotlightsearchtool/contentdomain/calendar-swift.struct/organizer.md)
  Attributes queried for the event organizer/host.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [static var calendar: SpotlightSearchTool.ContentDomain](spotlightsearchtool/contentdomain/calendar-swift.type.property.md)
  Calendar events, meetings, and scheduled items.
- [static func calendar(SpotlightSearchTool.ContentDomain.Calendar) -> SpotlightSearchTool.ContentDomain](spotlightsearchtool/contentdomain/calendar(_:).md)
  Calendar events, meetings, and scheduled items with custom attribute mapping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/contentdomain/calendar-swift.struct)*