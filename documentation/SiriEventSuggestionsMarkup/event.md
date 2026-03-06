# Event

**Framework**: Siri Event Suggestions Markup  
**Kind**: dictionary

A sporting event, live show, or other scheduled event.

**Availability**:
- Siri Event Suggestions Markup 1.0+

## Declaration

```swift
object Event
```

## Properties

- `@type` (string) *(required)*
- `location` (Place) *(required)*: The venue hosting the event.
- `name` (string) *(required)*: The name of the event.
- `startDate` (dateTimeISO8601) *(required)*: The time and date the event starts.
- `endDate` (dateTimeISO8601): The time and date the event ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/event)*