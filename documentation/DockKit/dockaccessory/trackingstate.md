# DockAccessory.TrackingState

**Framework**: DockKit  
**Kind**: struct  
**Role**: Structure

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
- [var description: String](./trackingstate/description.md)
- [var time: Date](./trackingstate/time.md)
  The timestamp indicating when the dock captured the tracking state.
- [var trackedSubjects: [DockAccessory.TrackedSubjectType]](./trackingstate/trackedsubjects.md)
  A collection of actively tracked subjects.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/trackingstate)*