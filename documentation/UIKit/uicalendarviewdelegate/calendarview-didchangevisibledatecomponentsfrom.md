# calendarView(_:didChangeVisibleDateComponentsFrom:)

**Framework**: UIKit  
**Kind**: method

**Availability**:
- iOS 16.2+
- iPadOS 16.2+
- Mac Catalyst 16.2+
- visionOS 1.0+

## Declaration

```swift
optional func calendarView(_ calendarView: UICalendarView, didChangeVisibleDateComponentsFrom previousDateComponents: DateComponents)
```

#### Discussion

Called when the visible date has changed from @c previousDateComponents from user interaction.

## Parameters

- `calendarView`: The @c UICalendarView
- `previousDateComponents`: The previous date components before the visible date components changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarviewdelegate/calendarview(_:didchangevisibledatecomponentsfrom:))*