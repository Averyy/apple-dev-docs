# NSFileAccessIntent

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface NSFileAccessIntent : NSObject
```

## Overview

Use this class when performing asynchronous operations with a file coordinator using the coordinator’s [`coordinate(with:queue:byAccessor:)`](./nsfilecoordinator/coordinate%28with,queue,byaccessor%29.md) method.

## Topics

### Creating a File Access Intent
- [class func readingIntent(with: URL, options: NSFileCoordinator.ReadingOptions) -> Self](./nsfileaccessintent/readingintent%28with,options%29.md)
  Returns a file access intent object for reading the given URL with the provided options.
- [class func writingIntent(with: URL, options: NSFileCoordinator.WritingOptions) -> Self](./nsfileaccessintent/writingintent%28with,options%29.md)
  Returns a file access intent object for writing to the given URL with the provided options.
### Accessing the Current URL
- [var url: URL](./nsfileaccessintent/url.md)
  The current URL for the item managed by the file access intent instance. (read-only)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Coordinated file access
- [protocol NSFilePresenter](./nsfilepresenter.md)
  The interface a file coordinator uses to inform an object presenting a file about changes to that file made elsewhere in the system.
- [class NSFileCoordinator](./nsfilecoordinator.md)
  An object that coordinates the reading and writing of files and directories among file presenters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfileaccessintent)*