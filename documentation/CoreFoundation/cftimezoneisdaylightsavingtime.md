# CFTimeZoneIsDaylightSavingTime(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns whether or not a time zone is in daylight savings time at a specified date.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func CFTimeZoneIsDaylightSavingTime(_ tz: CFTimeZone!, _ at: CFAbsoluteTime) -> Bool
```

#### Return Value

`true` if `tz` is in daylight savings time at `at`, otherwise `false`.

## Parameters

- `tz`: The time zone to analyze.
- `at`: The date in   to test for daylight savings.

## See Also

- [func CFTimeZoneGetDaylightSavingTimeOffset(CFTimeZone!, CFAbsoluteTime) -> CFTimeInterval](cftimezonegetdaylightsavingtimeoffset(_:_:).md)
  Returns the daylight saving time offset for a time zone at a given time.
- [func CFTimeZoneGetNextDaylightSavingTimeTransition(CFTimeZone!, CFAbsoluteTime) -> CFAbsoluteTime](cftimezonegetnextdaylightsavingtimetransition(_:_:).md)
  Returns the time in a given time zone of the next daylight saving time transition after a given time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cftimezoneisdaylightsavingtime(_:_:))*