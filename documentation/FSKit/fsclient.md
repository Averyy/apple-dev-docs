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
### Performing single-volume mounting
- [func mountSingleVolume(resource: FSResource, bundleID: String, options: [String], completionHandler: (URL?, (any Error)?) -> Void)](fsclient/mountsinglevolume(resource:bundleid:options:completionhandler:).md)
  Asynchronously mounts a single volume file system with a given resource.
- [class FSResource](fsresource.md)
  An abstract resource a file system uses to provide data for a volume.
### Accessing file system extension settings
- [func openFileSystemExtensionsSettings() -> Bool](fsclient/openfilesystemextensionssettings.md)
  Opens the File System Extensions settings in System Settings.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsclient)*