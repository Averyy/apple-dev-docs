# init(startingAt:showsHours:maxFieldCount:maxPrecision:)

**Framework**: SwiftUI  
**Kind**: init

Create a stopwatch format style.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init(startingAt startDate: Date, showsHours: Bool = true, maxFieldCount: Int = 4, maxPrecision: Duration = .milliseconds(10))
```

#### Discussion

A stopwatch styled display that starts counting up from zero at the given `startDate`.

- startDate: The date at which the stopwatch starts counting.
- showsHours: If true, the stopwatch shows the hours as a separate   element on the formatted string, once the duration is at least one hour.   If false, the stopwatch displays minute values greather than sixty.
- maxFieldCount: The number of fields that can be shown at once. For example, 1 hour, 34 minutes is shown as `1:34:00` by default, but as `1:34` if the `maxFieldCount` is set to two. The style automatically excludes more significant fields if their value is zero and they are not necessary for the format pattern, making room for less significant fields.
- maxPrecision: The precision at which the input is formatted. E.g. by default, two fractional digits are shown, making the maximum precision ten milliseconds. Setting the maximum precision to `.seconds(60)` would   only allow hours and minutes to be shown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/systemformatstyle/stopwatch/init(startingat:showshours:maxfieldcount:maxprecision:))*