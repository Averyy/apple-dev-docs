# makeFence()

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Creates a new memory fence instance.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func makeFence() -> (any MTLFence)?
```

```objc
- (id<MTLFence>) newFence;
```

## Mentions

- [Synchronizing passes with a fence](../synchronizing-passes-with-a-fence.md)

## See Also

### Creating fences and events
- [func makeEvent() -> (any MTLEvent)?](./makeevent%28%29.md)
  Creates a new event instance that you can use to synchronize commands and resources within the same GPU device.
- [func makeSharedEvent() -> (any MTLSharedEvent)?](./makesharedevent%28%29.md)
  Creates a new shared event instance that you can use to synchronize commands and resources across different GPU devices.
- [func makeSharedEvent(handle: MTLSharedEventHandle) -> (any MTLSharedEvent)?](./makesharedevent%28handle%29.md)
  Recreates a shared event from a handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makefence())*