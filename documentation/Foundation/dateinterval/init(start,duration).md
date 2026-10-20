# init(start:duration:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes an interval with the specified start date and duration.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
init(start: Date, duration: TimeInterval)
```

#### Discussion

Precondition: `duration >= 0`

## See Also

### Creating a Date Interval
- [init()](./init%28%29.md)
  Initializes an interval with start and end dates set to the current date and the duration set to `0`.
- [init(start: Date, end: Date)](./init%28start,end%29.md)
  Initializes an interval with the specified start and end date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dateinterval/init(start:duration:))*