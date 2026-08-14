# FSModuleIdentity

**Framework**: FSKit  
**Kind**: class

An installed file system module.

**Availability**:
- macOS 15.4+

## Declaration

```swift
class FSModuleIdentity
```

## Topics

### Accessing module properties
- [var bundleIdentifier: String](fsmoduleidentity/bundleidentifier.md)
  The module’s bundle identifier.
- [var url: URL](fsmoduleidentity/url.md)
  The module’s URL.
- [var isEnabled: Bool](fsmoduleidentity/isenabled.md)
  A Boolean value that indicates if the module is enabled.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [Copyable](../swift/copyable.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [Identifiable](../swift/identifiable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [func fetchInstalledExtensions(completionHandler: ([FSModuleIdentity]?, (any Error)?) -> Void)](fsclient/fetchinstalledextensions(completionhandler:).md)
  Asynchronously retrieves an list of installed file system modules.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsmoduleidentity)*