# DockAccessory.TrackingState

**Framework**: DockKit  
**Kind**: struct

A representation of the active tracking session state.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
struct TrackingState
```

#### Overview

The active tracking session emits this state 10 times per second.

## Topics

### Instance Properties
- [var description: String](dockaccessory/trackingstate/description.md)
- [var time: Date](dockaccessory/trackingstate/time.md)
  The timestamp indicating when the dock captured the tracking state.
- [var trackedSubjects: [DockAccessory.TrackedSubjectType]](dockaccessory/trackingstate/trackedsubjects.md)
  A collection of actively tracked subjects.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/trackingstate)*