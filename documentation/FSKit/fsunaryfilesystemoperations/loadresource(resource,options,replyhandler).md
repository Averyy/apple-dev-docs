# loadResource(resource:options:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Requests that the file system load a resource and present it as a volume.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func loadResource(resource: FSResource, options: FSTaskOptions, replyHandler reply: @escaping @Sendable (FSVolume?, (any Error)?) -> Void)
```

```swift
func loadResource(resource: FSResource, options: FSTaskOptions) async throws -> FSVolume
```

```objc
- (void) loadResource:(FSResource *) resource options:(FSTaskOptions *) options replyHandler:(void (^)(FSVolume *volume, NSError *err)) reply;
```

#### Discussion

Implement this method by inspecting the provided resource and verifying it uses a supported format. If the resource does use a supported format, create a subclass of `FSVolume`, clear the container error state, and invoke the `reply` callback, passing your volume as a parameter. If loading can’t proceed, invoke `reply` and send an appropriate error as the second parameter.

## Parameters

- `resource`: An [`FSResource`](../fsresource.md) to load.
- `options`: An [`FSTaskOptions`](../fstaskoptions.md) object specifying options to apply when loading the resource. An [`FSUnaryFileSystem`](../fsunaryfilesystem.md) supports two options: `-f` for “force” and `--rdonly` for read-only. The file system must remember if the read-only option is present.
- `reply`: A block or closure that your implementation invokes when it finishes setting up or encounters an error. Pass a subclass of `FSVolume` as the first parameter if loading succeeds. If loading fails, pass an error as the second parameter.

## See Also

### Loading and unloading resources
- [func unloadResource(resource: FSResource, options: FSTaskOptions, replyHandler: ((any Error)?) -> Void)](./unloadresource%28resource,options,replyhandler%29.md)
  Requests that the file system unload the specified resource.
- [func didFinishLoading()](./didfinishloading%28%29.md)
  Notifies you that the system finished loading your file system extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsunaryfilesystemoperations/loadresource(resource:options:replyhandler:))*