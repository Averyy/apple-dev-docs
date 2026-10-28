# eventStoreIdentifier

**Framework**: EventKit  
**Kind**: property  
**Role**: Instance Property

The unique identifier for the event store.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var eventStoreIdentifier: String { get }
```

```objc
@property (nonatomic, readonly) NSString * eventStoreIdentifier;
```

## Discussion

If the store is damaged, it’s recreated and given a new identifier. If this value is different from a fetched value, you should take the appropriate action.

## See Also

### Creating event stores
- [init()](./init%28%29.md)
  Creates a new event store.
- [init(sources: [EKSource])](./init%28sources%29.md)
  Creates an event store that contains data for the specified sources.
- [- initWithAccessToEntityTypes:](./initwithaccesstoentitytypes_.md)
  Initializes access to the event store with support for the given entity type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekeventstore/eventstoreidentifier)*