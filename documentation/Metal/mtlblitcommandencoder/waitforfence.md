# waitForFence(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command that instructs the GPU to wait until a pass updates a fence.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func waitForFence(_ fence: any MTLFence)
```

#### Discussion

Fences maintain order to prevent GPU data hazards as the GPU runs various passes within the same command queue. The GPU driver evaluates the fences and the commands that depend on them when your app commits the enclosing [`MTLCommandBuffer`](mtlcommandbuffer.md).

> ❗ **Important**:  For a blit pass that updates and waits for the same fence, you can only call [`waitForFence(_:)`](mtlblitcommandencoder/waitforfence(_:).md) before you call [`updateFence(_:)`](mtlblitcommandencoder/updatefence(_:).md). Updating a fence before waiting on it within the same encoder can cause GPU deadlock.

The GPU driver evaluates the pass’s fences and the commands that depend on them when your app commits the enclosing [`MTLCommandBuffer`](mtlcommandbuffer.md).

## Parameters

- `fence`: An   instance the GPU waits for before running this blit pass.

## See Also

- [func updateFence(any MTLFence)](mtlblitcommandencoder/updatefence(_:).md)
  Encodes a command that instructs the GPU to update a fence, which signals passes waiting on the fence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/waitforfence(_:))*