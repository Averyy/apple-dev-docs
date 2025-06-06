# NSFileAccessIntent

**Framework**: Foundation  
**Kind**: class

The details of a coordinated-read or coordinated-write operation.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSFileAccessIntent
```

#### Overview

Use this class when performing asynchronous operations with a file coordinator using the coordinator’s [`coordinate(with:queue:byAccessor:)`](nsfilecoordinator/coordinate(with:queue:byaccessor:).md) method.

## Topics

### Creating a File Access Intent
- [class func readingIntent(with: URL, options: NSFileCoordinator.ReadingOptions) -> Self](nsfileaccessintent/readingintent(with:options:).md)
  Returns a file access intent object for reading the given URL with the provided options.
- [class func writingIntent(with: URL, options: NSFileCoordinator.WritingOptions) -> Self](nsfileaccessintent/writingintent(with:options:).md)
  Returns a file access intent object for writing to the given URL with the provided options.
### Accessing the Current URL
- [var url: URL](nsfileaccessintent/url.md)
  The current URL for the item managed by the file access intent instance. (read-only)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol NSFilePresenter](nsfilepresenter.md)
  The interface a file coordinator uses to inform an object presenting a file about changes to that file made elsewhere in the system.
- [class NSFileCoordinator](nsfilecoordinator.md)
  An object that coordinates the reading and writing of files and directories among file presenters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfileaccessintent)*