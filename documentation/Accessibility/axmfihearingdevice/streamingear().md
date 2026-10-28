# streamingEar()

**Framework**: Accessibility  
**Kind**: method  
**Role**: Type Method

Returns which ears enable streaming.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static func streamingEar() -> AXMFiHearingDevice.Ear
```

```c
extern AXHearingDeviceEar AXMFiHearingDeviceStreamingEar();
```

## Return Value

An [`AXMFiHearingDevice.Ear`](./ear.md) constant that represents which ears enable streaming.

## See Also

### Streaming status
- [AXMFiHearingDevice.Ear](./ear.md)
  Constants that represent a hearing device ear.
- [static let streamingEarDidChangeNotification: NSNotification.Name](./streamingeardidchangenotification.md)
  A notification that the system posts when there’s a change to which ears enable streaming.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axmfihearingdevice/streamingear())*