# init(start:duration:)

**Framework**: Foundation  
**Kind**: init

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

- [init()](dateinterval/init.md)
  Initializes an interval with start and end dates set to the current date and the duration set to `0`.
- [init(start: Date, end: Date)](dateinterval/init(start:end:).md)
  Initializes an interval with the specified start and end date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dateinterval/init(start:duration:))*