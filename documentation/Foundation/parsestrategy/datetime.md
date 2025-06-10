# dateTime

**Framework**: Foundation  
**Kind**: property

A default format style for formatting dates.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static var dateTime: Date.FormatStyle { get }
```

#### Discussion

Use this type property when the call point allows the use of [`Date.FormatStyle`](date/formatstyle.md); in other words, when the value type is [`Date`](date.md). Typically, you use this with the [`formatted(_:)`](date/formatted(_:).md) method of [`Date`](date.md).

Customize the date format style using modifier syntax to apply specific date and time formats. For example:

```swift
let meetingDate = Date()
let localeArray = ["en_US", "sv_SE", "en_GB", "th_TH", "fr_BE"]
for localeID in localeArray {
    print(meetingDate.formatted(.dateTime
                                .day(.twoDigits)
                                .month(.wide)
                                .weekday(.short)
                                .hour(.conversationalTwoDigits(amPM: .wide))
                                .locale(Locale(identifier: localeID))))
}

// Tu, October 27, 5 PM
// ti 27 oktober 17
// Tu 27 October, 17
// อ. 27 ตุลาคม 17
// ma 27 octobre à 17 h
```

The default format styles provided are [`numeric`](date/formatstyle/datestyle/numeric.md) date format and [`shortened`](date/formatstyle/timestyle/shortened.md) time format. For example:

```swift
let meetingDate = Date()
meetingDate.formatted(.dateTime)) // 10/28/2020, 12:13 AM
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/parsestrategy/datetime)*