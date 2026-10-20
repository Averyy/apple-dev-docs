# FSModuleIdentity

**Framework**: FSKit  
**Kind**: class  
**Role**: Class

An installed file system module.

**Availability**:
- macOS 15.4+

## Declaration

```swift
class FSModuleIdentity
```

```objc
@interface FSModuleIdentity : NSObject
```

## Topics

### Accessing module properties
- [var bundleIdentifier: String](./fsmoduleidentity/bundleidentifier.md)
  The module’s bundle identifier.
- [var url: URL](./fsmoduleidentity/url.md)
  The module’s URL.
- [var isEnabled: Bool](./fsmoduleidentity/isenabled.md)
  A Boolean value that indicates if the module is enabled.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [Identifiable](../Swift/identifiable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Discovering installed extensions
- [func fetchInstalledExtensions(completionHandler: ([FSModuleIdentity]?, (any Error)?) -> Void)](./fsclient/fetchinstalledextensions%28completionhandler%29.md)
  Asynchronously retrieves an list of installed file system modules.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsmoduleidentity)*