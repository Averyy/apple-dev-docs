# init(origin:itemCount:totalItemCount:metrics:)

**Framework**: Create ML Components  
**Kind**: init

Creates an event.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
init(origin: String, itemCount: Int, totalItemCount: Int? = nil, metrics: [MetricsKey : any Sendable])
```

## Parameters

- `origin`: A description of the event’s origin.
- `itemCount`: The number of items processed so far.
- `totalItemCount`: The total number of items being processed.
- `metrics`: A dictionary of custom metrics values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/event/init(origin:itemcount:totalitemcount:metrics:))*