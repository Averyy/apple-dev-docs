# date(bySettingHour:minute:second:of:matchingPolicy:repeatedTimePolicy:direction:)

**Framework**: Foundation  
**Kind**: method

Returns a new `Date` representing the date calculated by setting hour, minute, and second to a given time on a specified `Date`.

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
func date(bySettingHour hour: Int, minute: Int, second: Int, of date: Date, matchingPolicy: Calendar.MatchingPolicy = .nextTime, repeatedTimePolicy: Calendar.RepeatedTimePolicy = .first, direction: Calendar.SearchDirection = .forward) -> Date?
```

#### Return Value

A `Date` representing the result of the search, or `nil` if a result could not be found.

#### Discussion

If no such time exists, the next available time is returned (which could, for example, be in a different day than the nominal target date). The intent is to return a date on the same day as the original date argument.  This may result in a date which is backward than the given date, of course.

## Parameters

- `hour`: A specified hour.
- `minute`: A specified minute.
- `second`: A specified second.
- `date`: The date to start calculation with.
- `matchingPolicy`: Specifies the technique the search algorithm uses to find results. Default value is  .
- `repeatedTimePolicy`: Specifies the behavior when multiple matches are found. Default value is  .
- `direction`: Specifies the direction in time to search. Default is  .

## See Also

- [func date(from: DateComponents) -> Date?](calendar/date(from:).md)
  Returns a date created from the specified components.
- [func date(byAdding: DateComponents, to: Date, wrappingComponents: Bool) -> Date?](calendar/date(byadding:to:wrappingcomponents:).md)
  Returns a new `Date` representing the date calculated by adding components to a given date.
- [func date(byAdding: Calendar.Component, value: Int, to: Date, wrappingComponents: Bool) -> Date?](calendar/date(byadding:value:to:wrappingcomponents:).md)
  Returns a new `Date` representing the date calculated by adding an amount of a specific component to a given date.
- [func date(bySetting: Calendar.Component, value: Int, of: Date) -> Date?](calendar/date(bysetting:value:of:).md)
  Returns a new `Date` representing the date calculated by setting a specific component to a given time, and trying to keep lower components the same.  If the component already has that value, this may result in a date which is the same as the given date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/calendar/date(bysettinghour:minute:second:of:matchingpolicy:repeatedtimepolicy:direction:))*