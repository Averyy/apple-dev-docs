# update(_:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Encodes a command that instructs the GPU to update a fence, which signals passes waiting on the fence.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
func update(_ fence: any MTLFence)
```

*Mac Catalyst, macOS*

```swift
optional func update(_ fence: any MTLFence)
```

```objc
- (void) updateFence:(id<MTLFence>) fence;
```

#### Discussion

Fences maintain order to prevent GPU data hazards as the GPU runs various passes within the same command queue. This encoded command notifies any passes waiting for `fence`.

The GPU driver evaluates the fences that apply to the pass and the commands that depend on those fences when your app commits the enclosing [`MTLCommandBuffer`](../mtlcommandbuffer.md).

## Parameters

- `fence`: An [`MTLFence`](../mtlfence.md) instance to update.

## See Also

### Performing fence operations
- [func wait(for: any MTLFence)](./wait%28for%29.md)
  Encodes a command that instructs the GPU to pause before starting the resource state commands until another pass updates a fence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresourcestatecommandencoder/update(_:))*