# date(bySetting:value:of:)

**Framework**: Foundation  
**Kind**: method

Returns a new `Date` representing the date calculated by setting a specific component to a given time, and trying to keep lower components the same.  If the component already has that value, this may result in a date which is the same as the given date.

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
func date(bySetting component: Calendar.Component, value: Int, of date: Date) -> Date?
```

#### Discussion

Changing a component’s value often will require higher or coupled components to change as well.  For example, setting the Weekday to Thursday usually will require the Day component to change its value, and possibly the Month and Year as well. If no such time exists, the next available time is returned (which could, for example, be in a different day, week, month, … than the nominal target date).  Setting a component to something which would be inconsistent forces other components to change; for example, setting the Weekday to Thursday probably shifts the Day and possibly Month and Year. The exact behavior of this method is implementation-defined. For example, if changing the weekday to Thursday, does that move forward to the next, backward to the previous, or to the nearest Thursday? The algorithm will try to produce a result which is in the next-larger component to the one given (there’s a table of this mapping at the top of this document).  So for the “set to Thursday” example, find the Thursday in the Week in which the given date resides (which could be a forwards or backwards move, and not necessarily the nearest Thursday). For more control over the exact behavior, use `nextDate(after:matching:matchingPolicy:behavior:direction:)`.

## See Also

- [func date(from: DateComponents) -> Date?](calendar/date(from:).md)
  Returns a date created from the specified components.
- [func date(byAdding: DateComponents, to: Date, wrappingComponents: Bool) -> Date?](calendar/date(byadding:to:wrappingcomponents:).md)
  Returns a new `Date` representing the date calculated by adding components to a given date.
- [func date(byAdding: Calendar.Component, value: Int, to: Date, wrappingComponents: Bool) -> Date?](calendar/date(byadding:value:to:wrappingcomponents:).md)
  Returns a new `Date` representing the date calculated by adding an amount of a specific component to a given date.
- [func date(bySettingHour: Int, minute: Int, second: Int, of: Date, matchingPolicy: Calendar.MatchingPolicy, repeatedTimePolicy: Calendar.RepeatedTimePolicy, direction: Calendar.SearchDirection) -> Date?](calendar/date(bysettinghour:minute:second:of:matchingpolicy:repeatedtimepolicy:direction:).md)
  Returns a new `Date` representing the date calculated by setting hour, minute, and second to a given time on a specified `Date`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/calendar/date(bysetting:value:of:))*