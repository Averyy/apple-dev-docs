# calendars(for:)

**Framework**: EventKit  
**Kind**: method

Returns the calendars that belong to this source object that support a particular entity type.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func calendars(for entityType: EKEntityType) -> Set<EKCalendar>
```

#### Return Value

The calendars belonging to this source that support the entity type.

## Parameters

- `entityType`: The entity type of either an event or a reminder.

## See Also

- [struct EKEntityMask](ekentitymask.md)
  A bitmask of `EKEntityType` for specifying multiple entities at once.
- [var calendars: Set<EKCalendar>](eksource/calendars.md)
  The calendars that belong to this source object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/eksource/calendars(for:))*