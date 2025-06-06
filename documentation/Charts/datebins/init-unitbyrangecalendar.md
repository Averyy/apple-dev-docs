# init(unit:by:range:calendar:)

**Framework**: Swift Charts  
**Kind**: init

Creates uniform bins covering the given range.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
init(unit: Calendar.Component, by stride: Int = 1, range: ClosedRange<Date>, calendar: Calendar = .autoupdatingCurrent)
```

#### Return Value

The bins.

## Parameters

- `unit`: The size of the bins.
- `stride`: The number of components for each bin.
- `range`: The range of the data the bins cover.
- `calendar`: The calendar to use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/datebins/init(unit:by:range:calendar:))*