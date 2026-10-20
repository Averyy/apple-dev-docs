# BADownload.State

**Framework**: Background Assets  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the state of a download.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
enum State
```

```c
enum BADownloadState : NSInteger;
```

## Topics

### Download states
- [BADownload.State.created](./state-swift.enum/created.md)
  A state that indicates a created download.
- [BADownload.State.waiting](./state-swift.enum/waiting.md)
  A state that indicates a download is waiting to execute.
- [BADownload.State.downloading](./state-swift.enum/downloading.md)
  A state that indicates a download is in progress.
- [BADownload.State.finished](./state-swift.enum/finished.md)
  A state that indicates a finished download.
- [BADownload.State.failed](./state-swift.enum/failed.md)
  A state that indicates a failed download.
### Initializers
- [init?(rawValue: Int)](./state-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the current state
- [var state: BADownload.State](./state-swift.property.md)
  The current state of the download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/badownload/state-swift.enum)*