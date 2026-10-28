# atHome

**Framework**: HomeKit  
**Kind**: property  
**Role**: Type Property

Triggers the event when at least one user is in the home.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
static var atHome: HMPresenceEventType { get }
```

```c
HMPresenceEventTypeAtHome
```

## Discussion

A convenience value for use in predicates on [`HMEventTrigger`](../hmeventtrigger.md). Represents the presence of at least one user in the home.

## See Also

### Using presence as a predicate
- [static var notAtHome: HMPresenceEventType](./notathome.md)
  Triggers the event when there are no users in the home.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmpresenceeventtype/athome)*