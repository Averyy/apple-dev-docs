# init(range:desiredCount:calendar:)

**Framework**: Swift Charts  
**Kind**: init

Automatically determine the bins from a range of data.

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
init(range: ClosedRange<Date>, desiredCount: Int = 10, calendar: Calendar = .autoupdatingCurrent)
```

#### Return Value

The inferred bins.

## Parameters

- `range`: The range the bins should cover.
- `desiredCount`: The desired number of bins for the given data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/datebins/init(range:desiredcount:calendar:))*