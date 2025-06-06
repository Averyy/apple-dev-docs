# init(timeInterval:range:)

**Framework**: Swift Charts  
**Kind**: init

Creates uniform bins covering the given range. The first bin starts at the lower bound of the range.

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
init(timeInterval: TimeInterval, range: ClosedRange<Date>)
```

#### Return Value

The bins.

## Parameters

- `timeInterval`: The size of the bins.
- `range`: The range of the data the bins cover.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/datebins/init(timeinterval:range:))*