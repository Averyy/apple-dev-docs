# didFinishLoading()

**Framework**: FSKit  
**Kind**: method

Notifies you that the system finished loading your file system extension.

**Availability**:
- macOS 15.4+

## Declaration

```swift
optional func didFinishLoading()
```

#### Discussion

The system performs this callback after the main run loop starts and before receiving the first message from the FSKit daemon.

Implement this method if you want to perform any setup prior to receiving FSKit callbacks.

## See Also

- [func loadResource(resource: FSResource, options: FSTaskOptions, replyHandler: (FSVolume?, (any Error)?) -> Void)](fsunaryfilesystemoperations/loadresource(resource:options:replyhandler:).md)
  Requests that the file system load a resource and present it as a volume.
- [func unloadResource(resource: FSResource, options: FSTaskOptions, replyHandler: ((any Error)?) -> Void)](fsunaryfilesystemoperations/unloadresource(resource:options:replyhandler:).md)
  Requests that the file system unload the specified resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsunaryfilesystemoperations/didfinishloading())*