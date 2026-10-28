# FSUnaryFileSystemOperations

**Framework**: FSKit  
**Kind**: protocol  
**Role**: Protocol

Operations performed by a unary file system.

**Availability**:
- macOS 15.4+

## Declaration

```swift
protocol FSUnaryFileSystemOperations : NSObjectProtocol
```

```objc
@protocol FSUnaryFileSystemOperations <NSObject>
```

## Overview

Make sure your subclass of [`FSUnaryFileSystem`](./fsunaryfilesystem.md) conforms to this protocol.

## Topics

### Loading and unloading resources
- [func loadResource(resource: FSResource, options: FSTaskOptions, replyHandler: (FSVolume?, (any Error)?) -> Void)](./fsunaryfilesystemoperations/loadresource%28resource,options,replyhandler%29.md)
  Requests that the file system load a resource and present it as a volume.
- [func unloadResource(resource: FSResource, options: FSTaskOptions, replyHandler: ((any Error)?) -> Void)](./fsunaryfilesystemoperations/unloadresource%28resource,options,replyhandler%29.md)
  Requests that the file system unload the specified resource.
- [func didFinishLoading()](./fsunaryfilesystemoperations/didfinishloading%28%29.md)
  Notifies you that the system finished loading your file system extension.
### Probing resources
- [func probeResource(resource: FSResource, replyHandler: (FSProbeResult?, (any Error)?) -> Void)](./fsunaryfilesystemoperations/proberesource%28resource,replyhandler%29.md)
  Requests that the file system probe the specified resource.
- [class FSProbeResult](./fsproberesult.md)
  An object that represents the results of a specific probe.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsunaryfilesystemoperations)*