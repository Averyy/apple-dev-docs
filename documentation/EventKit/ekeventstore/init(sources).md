# init(sources:)

**Framework**: EventKit  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithSources:(NSArray<EKSource *> *) sources;
```

#### Return Value

An event store that contains data for a specific collection of event sources.

## Parameters

- `sources`: An array of sources the event store should contain. This array may include delegate sources.

## See Also

### Creating event stores
- [init()](./init%28%29.md)
  Creates a new event store.
- [var eventStoreIdentifier: String](./eventstoreidentifier.md)
  The unique identifier for the event store.
- [- initWithAccessToEntityTypes:](./initwithaccesstoentitytypes_.md)
  Initializes access to the event store with support for the given entity type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekeventstore/init(sources:))*