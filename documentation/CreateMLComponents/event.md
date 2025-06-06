# Event

**Framework**: Create ML Components  
**Kind**: struct

Maintains the status of the pipeline.

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
struct Event
```

## Topics

### Creating the event
- [init(origin: String, itemCount: Int, totalItemCount: Int?, metrics: [MetricsKey : any Sendable])](event/init(origin:itemcount:totalitemcount:metrics:).md)
  Creates an event.
### Getting the properties
- [var itemCount: Int](event/itemcount.md)
  The number of items processed so far.
- [var metrics: [MetricsKey : any Sendable]](event/metrics.md)
  A dictionary of custom metrics values.
- [var origin: String](event/origin.md)
  A description of the event’s origin.
- [var totalItemCount: Int?](event/totalitemcount.md)
  The total number of items being processed.
### Default Implementations
- [CustomDebugStringConvertible Implementations](event/customdebugstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [typealias EventHandler](eventhandler.md)
  A closure to handle processing events.
- [struct MetricsKey](metricskey.md)
  A key that uniquely identifies a metric.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/event)*