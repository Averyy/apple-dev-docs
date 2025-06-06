# handlerQueue

**Framework**: Game Controller  
**Kind**: property  
**Required**: Yes

The dispatch queue that the framework uses to call element value change handlers.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var handlerQueue: dispatch_queue_t { get set }
```

## Mentions

- [Handling input events](handling-input-events.md)

#### Discussion

The default queue is the main queue. Set this property to another queue to asynchronously call value change handlers (see [`GCControllerAxisInput`](gccontrolleraxisinput.md), [`GCControllerButtonInput`](gccontrollerbuttoninput.md), [`GCControllerDirectionPad`](gccontrollerdirectionpad.md), and [`GCMotion`](gcmotion.md)). For example, if you handle input on another queue, set this property when you first access the input device.

## See Also

- [var physicalInputProfile: GCPhysicalInputProfile](gcdevice/physicalinputprofile.md)
  The device’s physical input profile, such as a controller’s extended gamepad.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdevice/handlerqueue)*