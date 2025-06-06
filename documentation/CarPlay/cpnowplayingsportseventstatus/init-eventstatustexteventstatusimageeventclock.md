# init(eventStatusText:eventStatusImage:eventClock:)

**Framework**: CarPlay  
**Kind**: init

Initialize an event status with optional event status text, an optional event status image, and an optional event clock.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
init(eventStatusText: [String]?, eventStatusImage: UIImage?, eventClock: CPNowPlayingSportsClock?)
```

#### Discussion

The first string should always be used to show the play period (quarter, inning, period) using as few characters as possible; e.g. “2nd” for the 2nd quarter.

The second and third strings can be used to display additional information, like “1st & 10” and “SF 15” for an American football game.

All three strings should be kept as brief as possible to ensure they display well on car screens of various sizes.

## Parameters

- `eventStatusText`: Up to three separate strings for event status may be displayed.
- `eventStatusImage`: An optional event status image for this event, if it applies to this event. For example,   a baseball game could display a representation of the bases and outs, indicating   how many bases are loaded and the number of outs in the current inning.
- `eventClock`: The event timer, if it applies to this event. See @c CPNowPlayingSportsClock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingsportseventstatus/init(eventstatustext:eventstatusimage:eventclock:))*