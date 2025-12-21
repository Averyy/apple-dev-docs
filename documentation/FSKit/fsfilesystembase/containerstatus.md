# containerStatus

**Framework**: FSKit  
**Kind**: property  
**Required**: Yes

The status of the file system container, indicating its readiness and activity.

**Availability**:
- macOS 15.4+

## Declaration

```swift
@NSCopying
var containerStatus: FSContainerStatus { get set }
```

#### Discussion

A file system container starts in the [`FSContainerState.notReady`](fscontainerstate/notready.md) state, and then transitions to the other values of the [`FSContainerState`](fscontainerstate.md) enumeration. The following diagram illustrates the possible state transitions.

![A flow diagram of four possible container states. The initial state, notReady, can transition to ready or blocked. The ready state can transition back to not ready, or to blocked or active. The blocked state can transition to ready or not ready. The active state can transition back to ready or to not ready.](https://docs-assets.developer.apple.com/published/bddcc0fab660562eaf070e9608aa415e/fs-file-system-base%402x.png)

Your file system implementation updates this property as it changes state. Many events and operations may trigger a state transition, and some transitions depend on a specific file system’s design.

When using [`FSBlockDeviceResource`](fsblockdeviceresource.md), implement the following common state transitions:

- Calling `loadResource` transitions the state out of [`FSContainerState.notReady`](fscontainerstate/notready.md). For all block device file systems, this operation changes the state to either [`FSContainerState.ready`](fscontainerstate/ready.md) or [`FSContainerState.blocked`](fscontainerstate/blocked.md).
- Calling `unloadResource` transitions to the [`FSContainerState.notReady`](fscontainerstate/notready.md) state, as does device termination.
- Transitioning from [`FSContainerState.blocked`](fscontainerstate/blocked.md) to [`FSContainerState.ready`](fscontainerstate/ready.md) occurs as a result of resolving the underlying block favorably.
- Transitioning from [`FSContainerState.ready`](fscontainerstate/ready.md) to [`FSContainerState.blocked`](fscontainerstate/blocked.md) is unusal, but valid.
- Transitioning between [`FSContainerState.ready`](fscontainerstate/ready.md) and [`FSContainerState.active`](fscontainerstate/active.md) can result from maintenance operations such as [`startCheck(task:options:)`](fsmanageableresourcemaintenanceoperations/startcheck(task:options:).md). For a [`FSUnaryFileSystem`](fsunaryfilesystem.md), this transition can also occur when activating or deactivating the container’s single volume.

## See Also

- [func wipe(FSBlockDeviceResource, completionHandler: ((any Error)?) -> Void)](fsfilesystembase/wipe(_:completionhandler:).md)
  Wipes existing file systems on the specified resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsfilesystembase/containerstatus)*