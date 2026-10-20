# organizer

**Framework**: Core Spotlight  
**Kind**: property  
**Role**: Instance Property

Attributes queried for the event organizer/host.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var organizer: [SearchableItemAttribute]?
```

## See Also

### Getting the domain attributes
- [var attendees: [SearchableItemAttribute]?](./attendees.md)
  Attributes queried for attendees/participants. Default: [`participants`](../../../searchableitemattribute/participants.md)
- [var date: [SearchableItemAttribute]?](./date.md)
  Attributes queried for the event date. Default: [`dueDate`](../../../searchableitemattribute/duedate.md)
- [var location: [SearchableItemAttribute]?](./location.md)
  Attributes queried for the event location. Default: [`namedLocation`](../../../searchableitemattribute/namedlocation.md), [`city`](../../../searchableitemattribute/city.md), [`stateOrProvince`](../../../searchableitemattribute/stateorprovince.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/contentdomain/calendar-swift.struct/organizer)*