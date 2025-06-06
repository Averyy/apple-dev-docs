# unloadResource(resource:options:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Requests that the file system unload the specified resource.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func unloadResource(resource: FSResource, options: FSTaskOptions) async throws
```

## Parameters

- `resource`: An   to unload.
- `options`: An   object specifying options to apply when unloading the resource.
- `reply`: A block or closure that your implementation invokes when it finishes unloading or encounters an error. If unloading fails, pass an error as the parameter to describe the problem. Otherwise, pass  .

## See Also

- [func loadResource(resource: FSResource, options: FSTaskOptions, replyHandler: (FSVolume?, (any Error)?) -> Void)](fsunaryfilesystemoperations/loadresource(resource:options:replyhandler:).md)
  Requests that the file system load a resource and present it as a volume.
- [func didFinishLoading()](fsunaryfilesystemoperations/didfinishloading.md)
  Notifies you that the system finished loading your file system extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsunaryfilesystemoperations/unloadresource(resource:options:replyhandler:))*