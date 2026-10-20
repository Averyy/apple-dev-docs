# hasBytesAvailable

**Framework**: Core Foundation  
**Kind**: property  
**Role**: Type Property

The stream has bytes to be read.

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
static var hasBytesAvailable: CFStreamEventType { get }
```

```c
kCFStreamEventHasBytesAvailable
```

## See Also

### Constants
- [static var openCompleted: CFStreamEventType](./opencompleted.md)
  The open has completed successfully.
- [static var canAcceptBytes: CFStreamEventType](./canacceptbytes.md)
  The stream can accept bytes for writing.
- [static var errorOccurred: CFStreamEventType](./erroroccurred.md)
  An error has occurred on the stream.
- [static var endEncountered: CFStreamEventType](./endencountered.md)
  The end of the stream has been reached.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstreameventtype/hasbytesavailable)*