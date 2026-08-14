# BADownload.Priority

**Framework**: Background Assets  
**Kind**: struct

A type that determines the execution priority of a scheduled asset download.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct Priority
```

#### Overview

Use [`BADownload.Priority`](badownload/priority-swift.struct.md) to assign an app-specific priority to a download or group of downloads. The system processes downloads with a higher priority before those with a lower priority, no matter what order you schedule them in.

## Topics

### Creating a priority
- [init(Int)](badownload/priority-swift.struct/init(_:).md)
  Creates a priority using the specified integer value.
- [init(rawValue: Int)](badownload/priority-swift.struct/init(rawvalue:).md)
  Creates a priority using the specified raw value.
### Getting system priorities
- [static let `default`: BADownload.Priority](badownload/priority-swift.struct/default.md)
  The default execution priority.
- [static let min: BADownload.Priority](badownload/priority-swift.struct/min.md)
  The lowest execution priority.
- [static let max: BADownload.Priority](badownload/priority-swift.struct/max.md)
  The highest execution priority.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var isEssential: Bool](badownload/isessential.md)
- [var priority: BADownload.Priority](badownload/priority-swift.property.md)
  The download’s execution priority.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/badownload/priority-swift.struct)*