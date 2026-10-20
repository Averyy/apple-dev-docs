# makeEvent()

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Creates a new event instance that you can use to synchronize commands and resources within the same GPU device.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func makeEvent() -> (any MTLEvent)?
```

```objc
- (id<MTLEvent>) newEvent;
```

## See Also

### Creating fences and events
- [func makeFence() -> (any MTLFence)?](./makefence%28%29.md)
  Creates a new memory fence instance.
- [func makeSharedEvent() -> (any MTLSharedEvent)?](./makesharedevent%28%29.md)
  Creates a new shared event instance that you can use to synchronize commands and resources across different GPU devices.
- [func makeSharedEvent(handle: MTLSharedEventHandle) -> (any MTLSharedEvent)?](./makesharedevent%28handle%29.md)
  Recreates a shared event from a handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makeevent())*