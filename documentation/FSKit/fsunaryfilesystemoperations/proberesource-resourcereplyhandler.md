# probeResource(resource:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Requests that the file system probe the specified resource.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func probeResource(resource: FSResource) async throws -> FSProbeResult
```

#### Discussion

Implement this method to indicate whether the resource is recognizable and usable.

## Parameters

- `resource`: The   to probe.
- `reply`: A block or closure that your implementation invokes when it finishes the probe or encounters an error. Pass an instance of   with probe results as the first parameter if your probe operation succeeds. If probing fails, pass an error as the second parameter.

## See Also

- [class FSProbeResult](fsproberesult.md)
  An object that represents the results of a specific probe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsunaryfilesystemoperations/proberesource(resource:replyhandler:))*