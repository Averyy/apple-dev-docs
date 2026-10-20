# probeResource(resource:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Requests that the file system probe the specified resource.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func probeResource(resource: FSResource, replyHandler reply: @escaping @Sendable (FSProbeResult?, (any Error)?) -> Void)
```

```swift
func probeResource(resource: FSResource) async throws -> FSProbeResult
```

```objc
- (void) probeResource:(FSResource *) resource replyHandler:(void (^)(FSProbeResult *result, NSError *error)) reply;
```

#### Discussion

Implement this method to indicate whether the resource is recognizable and usable.

## Parameters

- `resource`: The [`FSResource`](../fsresource.md) to probe.
- `reply`: A block or closure that your implementation invokes when it finishes the probe or encounters an error. Pass an instance of [`FSProbeResult`](../fsproberesult.md) with probe results as the first parameter if your probe operation succeeds. If probing fails, pass an error as the second parameter.

## See Also

### Probing resources
- [class FSProbeResult](../fsproberesult.md)
  An object that represents the results of a specific probe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsunaryfilesystemoperations/proberesource(resource:replyhandler:))*