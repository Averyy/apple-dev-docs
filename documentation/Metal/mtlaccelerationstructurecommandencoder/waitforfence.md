# waitForFence(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command that instructs the GPU to pause before starting the acceleration structure commands until another pass updates a fence.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func waitForFence(_ fence: any MTLFence)
```

#### Discussion

Fences maintain order to prevent GPU data hazards as the GPU runs various passes within the same command queue. The encoded resource state commands wait for a pass to update `fence` before running.

The GPU driver evaluates the pass’s fences and the commands that depend on them when your app commits the enclosing [`MTLCommandBuffer`](mtlcommandbuffer.md).

## Parameters

- `fence`: The fence to wait for.

## See Also

- [func updateFence(any MTLFence)](mtlaccelerationstructurecommandencoder/updatefence(_:).md)
  Encodes a command that instructs the GPU to update a fence, which signals passes waiting on the fence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructurecommandencoder/waitforfence(_:))*