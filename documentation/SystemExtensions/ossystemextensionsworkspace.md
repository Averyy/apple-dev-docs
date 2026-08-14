# OSSystemExtensionsWorkspace

**Framework**: System Extensions  
**Kind**: class

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.1+

## Declaration

```swift
class OSSystemExtensionsWorkspace
```

#### Overview

> **Note**: Using the workspace API requires the system extension entitlement

## Topics

### Instance Methods
- [func addObserver(any OSSystemExtensionsWorkspaceObserver) throws](ossystemextensionsworkspace/addobserver(_:).md)
- [func removeObserver(any OSSystemExtensionsWorkspaceObserver)](ossystemextensionsworkspace/removeobserver(_:).md)
- [func systemExtensions(forApplicationWithBundleID: String) throws -> Set<OSSystemExtensionProperties>](ossystemextensionsworkspace/systemextensions(forapplicationwithbundleid:).md)
### Type Properties
- [class var shared: OSSystemExtensionsWorkspace](ossystemextensionsworkspace/shared.md)

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
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemextensions/ossystemextensionsworkspace)*