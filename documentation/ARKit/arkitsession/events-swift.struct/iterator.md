# ARKitSession.Events.Iterator

**Framework**: ARKit  
**Kind**: struct  
**Role**: Structure

A type that provides a sequence’s iteration interface and encapsulates its iteration state.

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
  A type representing a sequence’s elements.
### Instance methods
- [func next() async -> ARKitSession.Events.Element?](./iterator/next%28%29.md)
  Returns the next element in a sequence.

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../../../Swift/asynciteratorprotocol.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arkitsession/events-swift.struct/iterator)*