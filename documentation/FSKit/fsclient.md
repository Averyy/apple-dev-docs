# FSClient

**Framework**: FSKit  
**Kind**: class

An interface for apps and daemons to interact with FSKit.

**Availability**:
- macOS 15.4+

## Declaration

```swift
class FSClient
```

#### Overview

FSClient is the primary management interface for FSKit. Use this class to discover FSKit extensions installed on the system, including your own.

> ❗ **Important**: Don’t subclass `FSClient`.

## Topics

### Obtaining the shared instance
- [class var shared: FSClient](fsclient/shared.md)
  The shared instance of the FSKit client class.
### Discovering installed extensions
- [func fetchInstalledExtensions(completionHandler: ([FSModuleIdentity]?, (any Error)?) -> Void)](fsclient/fetchinstalledextensions(completionhandler:).md)
  Asynchronously retrieves an list of installed file system modules.
- [class FSModuleIdentity](fsmoduleidentity.md)
  An installed file system module.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsclient)*