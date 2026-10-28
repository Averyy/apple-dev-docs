# OSSystemExtensionsWorkspace

**Framework**: System Extensions  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.1+

## Declaration

```swift
class OSSystemExtensionsWorkspace
```

```objc
@interface OSSystemExtensionsWorkspace : NSObject
```

## Overview

> **Note**: Using the workspace API requires the system extension entitlement

## Topics

### Instance Methods
- [func addObserver(any OSSystemExtensionsWorkspaceObserver) throws](./ossystemextensionsworkspace/addobserver%28_%29.md)
- [func removeObserver(any OSSystemExtensionsWorkspaceObserver)](./ossystemextensionsworkspace/removeobserver%28_%29.md)
- [func systemExtensions(forApplicationWithBundleID: String) throws -> Set<OSSystemExtensionProperties>](./ossystemextensionsworkspace/systemextensions%28forapplicationwithbundleid%29.md)
### Type Properties
- [class var shared: OSSystemExtensionsWorkspace](./ossystemextensionsworkspace/shared.md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemextensions/ossystemextensionsworkspace)*