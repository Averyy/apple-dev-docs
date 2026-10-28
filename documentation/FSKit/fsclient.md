# FSClient

**Framework**: FSKit  
**Kind**: class  
**Role**: Class

An interface for apps and daemons to interact with FSKit.

**Availability**:
- macOS 15.4+

## Declaration

```swift
class FSClient
```

```objc
@interface FSClient : NSObject
```

## Overview

FSClient is the primary management interface for FSKit. Use this class to discover FSKit extensions installed on the system, including your own.

> ❗ **Important**: Don’t subclass `FSClient`.

## Topics

### Obtaining the shared instance
- [class var shared: FSClient](./fsclient/shared.md)
  The shared instance of the FSKit client class.
### Discovering installed extensions
- [func fetchInstalledExtensions(completionHandler: ([FSModuleIdentity]?, (any Error)?) -> Void)](./fsclient/fetchinstalledextensions%28completionhandler%29.md)
  Asynchronously retrieves an list of installed file system modules.
- [class FSModuleIdentity](./fsmoduleidentity.md)
  An installed file system module.
### Performing single-volume mounting
- [func mountSingleVolume(resource: FSResource, bundleID: String, options: [String], completionHandler: (URL?, (any Error)?) -> Void)](./fsclient/mountsinglevolume%28resource,bundleid,options,completionhandler%29.md)
  Asynchronously mounts a single volume file system with a given resource.
- [class FSResource](./fsresource.md)
  An abstract resource a file system uses to provide data for a volume.
### Accessing file system extension settings
- [func openFileSystemExtensionsSettings() -> Bool](./fsclient/openfilesystemextensionssettings%28%29.md)
  Opens the File System Extensions settings in System Settings.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsclient)*