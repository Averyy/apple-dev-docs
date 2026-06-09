# taskIDToken

**Framework**: Foveated Streaming  
**Kind**: property  
**Required**: Yes

A token to be used for billing large buffer allocations to the host app.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
var taskIDToken: task_id_token_t { get }
```

#### Discussion

Use this token to ensure large allocations are billed to the calling app instead of your extension:

- When you create an [`IOSurface`](https://developer.apple.com/documentation/IOSurface/IOSurface) in this process, use [`IOSurfaceSetOwnershipIdentity(_:_:_:_:)`](https://developer.apple.com/documentation/IOSurface/IOSurfaceSetOwnershipIdentity(_:_:_:_:)) with this token to attribute the memory.
- When you create an [`MTLResource`](https://developer.apple.com/documentation/Metal/MTLResource) in this process (such as an `MTLBuffer` or `MTLTexture`), use [`setOwnerWithIdentity:`](https://developer.apple.com/documentation/Metal/MTLResource/setOwnerWithIdentity:) with this token to attribute the memory.

> ⚠️ **Warning**: Failure to properly attribute large buffers can result in process termination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingprovidercontext/taskidtoken)*