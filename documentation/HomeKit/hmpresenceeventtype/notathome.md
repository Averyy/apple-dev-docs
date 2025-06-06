# notAtHome

**Framework**: HomeKit  
**Kind**: property

Triggers the event when there are no users in the home.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
static var notAtHome: HMPresenceEventType { get }
```

#### Discussion

A convenience value for use in predicates on [`HMEventTrigger`](hmeventtrigger.md). Represents the presence of no users in the home.

## See Also

- [static var atHome: HMPresenceEventType](hmpresenceeventtype/athome.md)
  Triggers the event when at least one user is in the home.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmpresenceeventtype/notathome)*