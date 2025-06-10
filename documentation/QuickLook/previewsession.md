# PreviewSession

**Framework**: Quick Look  
**Kind**: struct

A structure with which you can control an existing session and receive events for the current preview application.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct PreviewSession
```

## Topics

### Instance Properties
- [var events: some AsyncSequence<PreviewSession.Event, Never>](previewsession/events.md)
  An async sequence of preview session events.
### Instance Methods
- [func close() async throws](previewsession/close.md)
  Closes the preview session.
### Enumerations
- [PreviewSession.Event](previewsession/event.md)
  An event from the preview session’s events stream.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/previewsession)*