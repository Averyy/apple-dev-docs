# makeFence()

**Framework**: Metal  
**Kind**: method  
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

## See Also

- [func makeEvent() -> (any MTLEvent)?](mtldevice/makeevent.md)
  Creates a new event instance that you can use to synchronize commands and resources within the same GPU device.
- [func makeSharedEvent() -> (any MTLSharedEvent)?](mtldevice/makesharedevent.md)
  Creates a new shared event instance that you can use to synchronize commands and resources across different GPU devices.
- [func makeSharedEvent(handle: MTLSharedEventHandle) -> (any MTLSharedEvent)?](mtldevice/makesharedevent(handle:).md)
  Recreates a shared event from a handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makefence())*