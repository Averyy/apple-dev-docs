# endEncountered

**Framework**: Core Foundation  
**Kind**: property  
**Role**: Type Property

The end of the stream has been reached.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
static var endEncountered: CFStreamEventType { get }
```

```c
kCFStreamEventEndEncountered
```

## See Also

### Constants
- [static var openCompleted: CFStreamEventType](./opencompleted.md)
  The open has completed successfully.
- [static var hasBytesAvailable: CFStreamEventType](./hasbytesavailable.md)
  The stream has bytes to be read.
- [static var canAcceptBytes: CFStreamEventType](./canacceptbytes.md)
  The stream can accept bytes for writing.
- [static var errorOccurred: CFStreamEventType](./erroroccurred.md)
  An error has occurred on the stream.
- [kCFStreamEventNone](./kcfstreameventnone.md)
  No event has occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstreameventtype/endencountered)*