# loadResource(resource:options:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Requests that the file system load a resource and present it as a volume.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func loadResource(resource: FSResource, options: FSTaskOptions) async throws -> FSVolume
```

#### Discussion

Implement this method by inspecting the provided resource and verifying it uses a supported format. If the resource does use a supported format, create a subclass of `FSVolume`, clear the container error state, and invoke the `reply` callback, passing your volume as a parameter. If loading can’t proceed, invoke `reply` and send an appropriate error as the second parameter.

## Parameters

- `resource`: An   to load.
- `options`: An   object specifying options to apply when loading the resource. An   supports two options:   for “force” and   for read-only. The file system must remember if the read-only option is present.
- `reply`: A block or closure that your implementation invokes when it finishes setting up or encounters an error. Pass a subclass of   as the first parameter if loading succeeds. If loading fails, pass an error as the second parameter.

## See Also

- [func unloadResource(resource: FSResource, options: FSTaskOptions, replyHandler: ((any Error)?) -> Void)](fsunaryfilesystemoperations/unloadresource(resource:options:replyhandler:).md)
  Requests that the file system unload the specified resource.
- [func didFinishLoading()](fsunaryfilesystemoperations/didfinishloading.md)
  Notifies you that the system finished loading your file system extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsunaryfilesystemoperations/loadresource(resource:options:replyhandler:))*