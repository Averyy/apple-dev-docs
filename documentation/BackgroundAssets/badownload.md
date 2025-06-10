# BADownload

**Framework**: Background Assets  
**Kind**: class

An object that represents an in-progress or concluded asset download.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 18.4+
- visionOS 2.4+

## Declaration

```swift
class BADownload
```

#### Overview

> **Note**:  You don’t create instances of this object directly. Instead, use an object that inherits from [`BADownload`](badownload.md), such as [`BAURLDownload`](baurldownload.md).

## Topics

### Getting the identity
- [var identifier: String](badownload/identifier.md)
  The app-specific string that uniquely identifies the downloadable asset.
- [var uniqueIdentifier: String](badownload/uniqueidentifier.md)
  The system-provided string that uniquely identifies the download object.
### Determining the priority
- [var isEssential: Bool](badownload/isessential.md)
- [var priority: BADownload.Priority](badownload/priority-swift.property.md)
  The download’s execution priority.
- [BADownload.Priority](badownload/priority-swift.struct.md)
  A type that determines the execution priority of a scheduled asset download.
### Getting the current state
- [var state: BADownload.State](badownload/state-swift.property.md)
  The current state of the download.
- [BADownload.State](badownload/state-swift.enum.md)
  Constants that indicate the state of a download.
### Downloading nonessential assets
- [func removingEssential() -> Self](badownload/removingessential.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [BAURLDownload](baurldownload.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class BAURLDownload](baurldownload.md)
  An object that represents a remote asset to download.
- [BADownload.Priority](badownload/priority-swift.struct.md)
  A type that determines the execution priority of a scheduled asset download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/badownload)*