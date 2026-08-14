# FSTaskOptions

**Framework**: FSKit  
**Kind**: class

A class that passes command options to a task, optionally providing security-scoped URLs.

**Availability**:
- macOS 15.4+

## Declaration

```swift
class FSTaskOptions
```

## Topics

### Retrieving task options
- [var taskOptions: [String]](fstaskoptions/taskoptions.md)
  An array of strings that represent command-line options for the task.
### Retrieving task option URLs
- [func url(forOption: String) -> URL?](fstaskoptions/url(foroption:).md)
  Retrieves a URL for a given option.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class FSTask](fstask.md)
  A class that enables a file system module to pass log messages and completion notifications to clients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fstaskoptions)*