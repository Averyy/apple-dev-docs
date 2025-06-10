# ActivityState

**Framework**: ActivityKit  
**Kind**: enum

The enum that describes the state of a Live Activity in its life cycle.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+

## Declaration

```swift
enum ActivityState
```

## Mentions

- [Displaying live data with Live Activities](displaying-live-data-with-live-activities.md)

## Topics

### Live Activity states
- [ActivityState.active](activitystate/active.md)
  The Live Activity is active, visible, and can receive content updates.
- [ActivityState.dismissed](activitystate/dismissed.md)
  The Live Activity ended and is no longer visible because a person or the system removed it.
- [ActivityState.pending](activitystate/pending.md)
  The Live Activity is scheduled to start at a specified date but hasn’t started yet.
- [ActivityState.stale](activitystate/stale.md)
  The Live Activity content is out of date and needs an update.
- [ActivityState.ended](activitystate/ended.md)
  The Live Activity is visible, but a person, the app, or the system ended it, and it won’t update its content anymore.
### Operators
- [static func == (ActivityState, ActivityState) -> Bool](activitystate/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(from: any Decoder) throws](activitystate/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [var hashValue: Int](activitystate/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](activitystate/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](activitystate/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](activitystate/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var activityState: ActivityState](activity/activitystate.md)
  The current state of a Live Activity in its life cycle.
- [var activityStateUpdates: Activity<Attributes>.ActivityStateUpdates](activity/activitystateupdates-swift.property.md)
  An asynchronous sequence you use to observe activity state changes.
- [Activity.ActivityStateUpdates](activity/activitystateupdates-swift.struct.md)
  A structure that offers functionality to observe state changes of a Live Activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activitystate)*