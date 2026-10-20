# PGResumeErrorCode

**Framework**: Paravirtualized Graphics  
**Kind**: enum  
**Role**: Enumeration

Error codes for suspend-resume actions.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
enum PGResumeErrorCode
```

```c
enum PGResumeErrorCode : NSUInteger;
```

## Topics

### Errors
- [PGResumeErrorCode.incompatibleDevice](./pgresumeerrorcode/incompatibledevice.md)
  The resume device is missing capabilities that the suspended device provided.
- [PGResumeErrorCode.internalFault](./pgresumeerrorcode/internalfault.md)
  An internal error occurred.
- [PGResumeErrorCode.invalidContent](./pgresumeerrorcode/invalidcontent.md)
  The content of the suspend state or the guest memory isn’t valid.
- [PGResumeErrorCode.invalidGuestVersion](./pgresumeerrorcode/invalidguestversion.md)
  The guest version is incompatible with this framework version.
- [PGResumeErrorCode.invalidSuspendStateVersion](./pgresumeerrorcode/invalidsuspendstateversion.md)
  The suspend state version is incompatible with this framework version.
### Enumeration Cases
- [PGResumeErrorCode.invalidDisplayPortCount](./pgresumeerrorcode/invaliddisplayportcount.md)
### Initializers
- [init?(rawValue: UInt)](./pgresumeerrorcode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Suspending and Resuming Graphics Processing
- [func willSuspend()](./pgdevice/willsuspend%28%29.md)
  Notifies the virtual graphics device to start suspending graphics activities.
- [func finishSuspend() -> Data?](./pgdevice/finishsuspend%28%29.md)
  Notifies the virtualized graphics device to finish suspending graphics activities.
- [func willResume(withSuspendState: Data, error: NSErrorPointer) -> Bool](./pgdevice/willresume%28withsuspendstate,error%29.md)
  Tells a new device object to load a previously saved device’s suspend state.
- [func didResume()](./pgdevice/didresume%28%29.md)
  Tells the device object to finish any remaining work to resume processing of a previously saved device’s suspend state.
- [let PGResumeErrorDomain: String](./pgresumeerrordomain.md)
  The error domain for suspend-resume actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgresumeerrorcode)*