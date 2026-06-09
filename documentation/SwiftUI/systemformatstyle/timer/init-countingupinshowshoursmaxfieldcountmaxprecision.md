# init(countingUpIn:showsHours:maxFieldCount:maxPrecision:)

**Framework**: SwiftUI  
**Kind**: init

Creates a timer format style that counts up within the interval you provide.

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
init(countingUpIn interval: Range<Date>, showsHours: Bool = true, maxFieldCount: Int = 3, maxPrecision: Duration = .seconds(1))
```

#### Discussion

The timer displays the elapsed time, starting from zero and increasing toward the total interval duration.

## Parameters

- `interval`: The time interval during which the timer counts up.
- `showsHours`: If `true`, hours appear as a separate element when the elapsed time reaches one hour. If `false`, minutes accumulate beyond 60.
- `maxFieldCount`: The maximum number of fields shown at once. With the default of 3, output includes hours, minutes, and seconds. With 2, it shows hours and minutes once the time reaches hours.
- `maxPrecision`: The smallest time interval between display updates. Defaults to 1 second.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/systemformatstyle/timer/init(countingupin:showshours:maxfieldcount:maxprecision:))*