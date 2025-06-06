# CFTimeZoneGetDaylightSavingTimeOffset(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the daylight saving time offset for a time zone at a given time.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CFTimeZoneGetDaylightSavingTimeOffset(_ tz: CFTimeZone!, _ at: CFAbsoluteTime) -> CFTimeInterval
```

#### Return Value

The daylight saving time offset for `tz` at `at`.

## Parameters

- `tz`: The time zone to analyze.
- `at`: The time in   to test for daylight saving time offset.

## See Also

- [func CFTimeZoneIsDaylightSavingTime(CFTimeZone!, CFAbsoluteTime) -> Bool](cftimezoneisdaylightsavingtime(_:_:).md)
  Returns whether or not a time zone is in daylight savings time at a specified date.
- [func CFTimeZoneGetNextDaylightSavingTimeTransition(CFTimeZone!, CFAbsoluteTime) -> CFAbsoluteTime](cftimezonegetnextdaylightsavingtimetransition(_:_:).md)
  Returns the time in a given time zone of the next daylight saving time transition after a given time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cftimezonegetdaylightsavingtimeoffset(_:_:))*