# autoupdatingCurrent

**Framework**: Foundation  
**Kind**: property

A calendar that tracks changes to user’s preferred calendar.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var autoupdatingCurrent: Calendar { get }
```

#### Discussion

If mutated, this calendar will no longer track the user’s preferred calendar.

> **Note**:  The autoupdating Calendar will only compare equal to another autoupdating Calendar.

## See Also

- [static var current: Calendar](calendar/current.md)
  The user’s current calendar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/calendar/autoupdatingcurrent)*