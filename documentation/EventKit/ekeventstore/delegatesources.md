# delegateSources

**Framework**: EventKit  
**Kind**: property  
**Role**: Instance Property

The event sources delegated to the person using your app.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var delegateSources: [EKSource] { get }
```

```objc
@property (nonatomic, readonly) NSArray<EKSource *> * delegateSources;
```

#### Discussion

By default, delegate event sources aren’t included in an event store’s [`sources`](./sources.md). To access events and reminders in a delegate source:

1. Use [`init()`](./init%28%29.md) to initialize an [`EKEventStore`](../ekeventstore.md).
2. Use [`requestAccess(to:completion:)`](./requestaccess%28to,completion%29.md) to request access to the desired entity types.
3. Get the delegate sources from the event store using [`delegateSources`](./delegatesources.md).
4. After the request is granted, initialize another [`EKEventStore`](../ekeventstore.md) using [`init(sources:)`](./init%28sources%29.md), passing the delegate stores.

## See Also

### Accessing account sources
- [var sources: [EKSource]](./sources.md)
  An unordered array of objects that represent accounts that contain calendars.
- [func source(withIdentifier: String) -> EKSource?](./source%28withidentifier%29.md)
  Locates an event source with the specified identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekeventstore/delegatesources)*