# signaledValue

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The current signal value for the shareable event.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
var signaledValue: UInt64 { get set }
```

```objc
@property (readwrite) uint64_t signaledValue;
```

## Mentions

- [Synchronizing events between a GPU and the CPU](../synchronizing-events-between-a-gpu-and-the-cpu.md)

#### Discussion

When you set the value of a shared event, its value is changed only if you provide a larger value than the value currently stored in the event. Setting this property signals the event. Commands waiting on the event are allowed to run if the new value is equal to or greater than the value for which they are waiting. Similarly, setting the event’s value triggers notifications if the value is equal to or greater than the value for which they are waiting.

## See Also

### Synchronizing a shareable event
- [func notify(MTLSharedEventListener, atValue: UInt64, block: MTLSharedEventNotificationBlock)](./notify%28_,atvalue,block%29.md)
  Schedules a notification handler to be called after the shareable event’s signal value equals or exceeds a given value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlsharedevent/signaledvalue)*