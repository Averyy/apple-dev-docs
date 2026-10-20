# unloadResource(resource:options:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Requests that the file system unload the specified resource.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func unloadResource(resource: FSResource, options: FSTaskOptions, replyHandler reply: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func unloadResource(resource: FSResource, options: FSTaskOptions) async throws
```

```objc
- (void) unloadResource:(FSResource *) resource options:(FSTaskOptions *) options replyHandler:(void (^)(NSError *err)) reply;
```

## Parameters

- `resource`: An [`FSResource`](../fsresource.md) to unload.
- `options`: An [`FSTaskOptions`](../fstaskoptions.md) object specifying options to apply when unloading the resource.
- `reply`: A block or closure that your implementation invokes when it finishes unloading or encounters an error. If unloading fails, pass an error as the parameter to describe the problem. Otherwise, pass `nil`.

## See Also

### Loading and unloading resources
- [func loadResource(resource: FSResource, options: FSTaskOptions, replyHandler: (FSVolume?, (any Error)?) -> Void)](./loadresource%28resource,options,replyhandler%29.md)
  Requests that the file system load a resource and present it as a volume.
- [func didFinishLoading()](./didfinishloading%28%29.md)
  Notifies you that the system finished loading your file system extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsunaryfilesystemoperations/unloadresource(resource:options:replyhandler:))*