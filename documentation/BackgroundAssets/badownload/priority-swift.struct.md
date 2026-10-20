# BADownload.Priority

**Framework**: Background Assets  
**Kind**: struct  
**Role**: Structure

A type that determines the execution priority of a scheduled asset download.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
struct Priority
```

```c
typedef NSInteger BADownloaderPriority;
```

#### Overview

Use [`BADownload.Priority`](./priority-swift.struct.md) to assign an app-specific priority to a download or group of downloads. The system processes downloads with a higher priority before those with a lower priority, no matter what order you schedule them in.

## Topics

### Creating a priority
- [init(Int)](./priority-swift.struct/init%28_%29.md)
  Creates a priority using the specified integer value.
- [init(rawValue: Int)](./priority-swift.struct/init%28rawvalue%29.md)
  Creates a priority using the specified raw value.
### Getting system priorities
- [static let `default`: BADownload.Priority](./priority-swift.struct/default.md)
  The default execution priority.
- [static let min: BADownload.Priority](./priority-swift.struct/min.md)
  The lowest execution priority.
- [static let max: BADownload.Priority](./priority-swift.struct/max.md)
  The highest execution priority.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Determining the priority
- [var isEssential: Bool](./isessential.md)
- [var priority: BADownload.Priority](./priority-swift.property.md)
  The download’s execution priority.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/badownload/priority-swift.struct)*