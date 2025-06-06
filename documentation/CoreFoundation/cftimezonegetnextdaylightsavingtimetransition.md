# CFTimeZoneGetNextDaylightSavingTimeTransition(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the time in a given time zone of the next daylight saving time transition after a given time.

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
func CFTimeZoneGetNextDaylightSavingTimeTransition(_ tz: CFTimeZone!, _ at: CFAbsoluteTime) -> CFAbsoluteTime
```

#### Return Value

The time in `tz` of the next daylight saving time transition after `at`.

## Parameters

- `tz`: The time zone to analyze.
- `at`: A time in  .

## See Also

- [func CFTimeZoneIsDaylightSavingTime(CFTimeZone!, CFAbsoluteTime) -> Bool](cftimezoneisdaylightsavingtime(_:_:).md)
  Returns whether or not a time zone is in daylight savings time at a specified date.
- [func CFTimeZoneGetDaylightSavingTimeOffset(CFTimeZone!, CFAbsoluteTime) -> CFTimeInterval](cftimezonegetdaylightsavingtimeoffset(_:_:).md)
  Returns the daylight saving time offset for a time zone at a given time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cftimezonegetnextdaylightsavingtimetransition(_:_:))*