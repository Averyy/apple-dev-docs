# ARKitSession.Events.Iterator

**Framework**: ARKit  
**Kind**: struct  
**Role**: Structure

An iterator over a sequence of session events.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
struct Iterator
```

## Topics

### Type aliases
- [ARKitSession.Events.Element](./element.md)
  The type of element produced by this asynchronous sequence: ARKitSession.Event.
### Instance methods
- [func next() async -> ARKitSession.Events.Element?](./iterator/next%28%29.md)
  Asynchronously retrieve the next Event.

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../../../Swift/asynciteratorprotocol.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arkitsession/events-swift.struct/iterator)*