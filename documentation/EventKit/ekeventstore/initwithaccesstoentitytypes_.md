# initWithAccessToEntityTypes:

**Framework**: EventKit  
**Kind**: method  
**Role**: Instance Method

Initializes access to the event store with support for the given entity type.

**Availability**:
- macOS 10.8+ - Deprecated in 10.9

> **Deprecated**: Use [`init()`](./init%28%29.md) instead.

## Declaration

```objc
- (id) initWithAccessToEntityTypes:(EKEntityMask) entityTypes;
```

#### Return Value

The event store.

## Parameters

- `entityTypes`: The event or reminder entity mask.

## See Also

### Creating event stores
- [init()](./init%28%29.md)
  Creates a new event store.
- [init(sources: [EKSource])](./init%28sources%29.md)
  Creates an event store that contains data for the specified sources.
- [var eventStoreIdentifier: String](./eventstoreidentifier.md)
  The unique identifier for the event store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekeventstore/initwithaccesstoentitytypes:)*