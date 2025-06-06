# updateFence(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command that instructs the GPU to update a fence, which signals passes waiting on the fence.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func updateFence(_ fence: any MTLFence)
```

#### Discussion

Fences maintain order to prevent GPU data hazards as the GPU runs various passes within the same command queue. The acceleration structure encoder notifies any passes waiting for `fence`.

The GPU driver evaluates the pass’s fences and the commands that depend on them when your app commits the enclosing [`MTLCommandBuffer`](mtlcommandbuffer.md).

## Parameters

- `fence`: An   instance to update.

## See Also

- [func waitForFence(any MTLFence)](mtlaccelerationstructurecommandencoder/waitforfence(_:).md)
  Encodes a command that instructs the GPU to pause before starting the acceleration structure commands until another pass updates a fence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructurecommandencoder/updatefence(_:))*