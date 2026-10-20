# FSTaskOptions

**Framework**: FSKit  
**Kind**: class  
**Role**: Class

A class that passes command options to a task, optionally providing security-scoped URLs.

**Availability**:
- macOS 15.4+

## Declaration

```swift
class FSTaskOptions
```

```objc
@interface FSTaskOptions : NSObject
```

## Topics

### Retrieving task options
- [var taskOptions: [String]](./fstaskoptions/taskoptions.md)
  An array of strings that represent command-line options for the task.
### Retrieving task option URLs
- [func url(forOption: String) -> URL?](./fstaskoptions/url%28foroption%29.md)
  Retrieves a URL for a given option.

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

## See Also

### Tasks
- [class FSTask](./fstask.md)
  A class that enables a file system module to pass log messages and completion notifications to clients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fstaskoptions)*