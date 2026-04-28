# StatusAccountListSubscribedCalendarAccountObject

**Framework**: Device Management  
**Kind**: dictionary

A status report of the client’s subscribed calendar details.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 14.0+
- visionOS 1.1+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object StatusAccountListSubscribedCalendarAccountObject
```

## Properties

- `_removed` (boolean): If `true`, the subscribed calendar is removed and the status item object only contains this key and the `identifier` key.
- `calendar-url` (string): The URL of the subscribed calendar.
- `declaration-identifier` (string): The identifier of the declaration that installed the subscribed calendar. Only present if a declaration installed the subscribed calendar.
- `identifier` (string) *(required)*: The unique identifier for the subscribed calendar.
- `is-enabled` (boolean): A Boolean value that indicates whether the Calendar app displays this subscribed calendar.
- `username` (string): The user name for authenticating with the subscribed calendar.
- `visible-name` (string): The name of the subscribed calendar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusaccountlistsubscribedcalendaraccountobject)*