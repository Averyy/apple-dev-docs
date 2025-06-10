# updateFence(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command that instructs the GPU to update a fence, which signals passes waiting on the fence.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func updateFence(_ fence: any MTLFence)
```

#### Discussion

Fences maintain order to prevent GPU data hazards as the GPU runs various passes within the same command queue. Metal evaluates fences and the commands that depend on them when your app commits the enclosing [`MTLCommandBuffer`](mtlcommandbuffer.md).

> ❗ **Important**:  For a pass that updates and waits for the same fence, call [`waitForFence(_:)`](mtlblitcommandencoder/waitforfence(_:).md) before you call [`updateFence(_:)`](mtlblitcommandencoder/updatefence(_:).md). Updating a fence before waiting on it within the same encoder can cause GPU deadlock.

## Parameters

- `fence`: An   instance to update.

## See Also

- [func waitForFence(any MTLFence)](mtlblitcommandencoder/waitforfence(_:).md)
  Encodes a command that instructs the GPU to wait until a pass updates a fence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/updatefence(_:))*