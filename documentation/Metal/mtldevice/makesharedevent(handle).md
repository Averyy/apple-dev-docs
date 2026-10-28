# makeSharedEvent(handle:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Recreates a shared event from a handle.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func makeSharedEvent(handle sharedEventHandle: MTLSharedEventHandle) -> (any MTLSharedEvent)?
```

```objc
- (id<MTLSharedEvent>) newSharedEventWithHandle:(MTLSharedEventHandle *) sharedEventHandle;
```

## Return Value

A new [`MTLSharedEvent`](../mtlsharedevent.md) instance if the method completed successfully; otherwise nil.

## Parameters

- `sharedEventHandle`: An [`MTLSharedEventHandle`](../mtlsharedeventhandle.md) instance from another GPU device or process.

## See Also

### Creating fences and events
- [func makeFence() -> (any MTLFence)?](./makefence%28%29.md)
  Creates a new memory fence instance.
- [func makeEvent() -> (any MTLEvent)?](./makeevent%28%29.md)
  Creates a new event instance that you can use to synchronize commands and resources within the same GPU device.
- [func makeSharedEvent() -> (any MTLSharedEvent)?](./makesharedevent%28%29.md)
  Creates a new shared event instance that you can use to synchronize commands and resources across different GPU devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makesharedevent(handle:))*