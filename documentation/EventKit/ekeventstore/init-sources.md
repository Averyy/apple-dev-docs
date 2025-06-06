# init(sources:)

**Framework**: EventKit  
**Kind**: init

Creates an event store that contains data for the specified sources.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 10.11+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init(sources: [EKSource])
```

#### Return Value

An event store that contains data for a specific collection of event sources.

## Parameters

- `sources`: An array of sources the event store should contain. This array may include delegate sources.

## See Also

- [init()](ekeventstore/init.md)
  Creates a new event store.
- [var eventStoreIdentifier: String](ekeventstore/eventstoreidentifier.md)
  The unique identifier for the event store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekeventstore/init(sources:))*