# CAClockMessage

**Framework**: Audio Toolbox  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- macOS

## Declaration

```swift
enum CAClockMessage
```

```c
enum CAClockMessage : UInt32;
```

## Topics

### Constants
- [CAClockMessage.armed](./caclockmessage/armed.md)
- [CAClockMessage.disarmed](./caclockmessage/disarmed.md)
- [CAClockMessage.propertyChanged](./caclockmessage/propertychanged.md)
- [CAClockMessage.startTimeSet](./caclockmessage/starttimeset.md)
- [CAClockMessage.started](./caclockmessage/started.md)
- [CAClockMessage.stopped](./caclockmessage/stopped.md)
- [CAClockMessage.wrongSMPTEFormat](./caclockmessage/wrongsmpteformat.md)
### Initializers
- [init?(rawValue: UInt32)](./caclockmessage/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Adding and Removing Listeners
- [func CAClockAddListener(CAClockRef, CAClockListenerProc, UnsafeMutableRawPointer) -> OSStatus](./caclockaddlistener%28_,_,_%29.md)
- [func CAClockRemoveListener(CAClockRef, CAClockListenerProc, UnsafeMutableRawPointer) -> OSStatus](./caclockremovelistener%28_,_,_%29.md)
- [typealias CAClockListenerProc](./caclocklistenerproc.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/caclockmessage)*