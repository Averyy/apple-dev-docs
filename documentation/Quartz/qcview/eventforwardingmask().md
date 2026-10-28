# eventForwardingMask()

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Retrieves the mask used to filter which types of events are forwarded from the view to the composition during rendering.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func eventForwardingMask() -> Int
```

```objc
- (NSUInteger) eventForwardingMask;
```

## Return Value

The event filtering mask.

## See Also

### Setting and Getting Event Masks
- [func setEventForwardingMask(Int)](./seteventforwardingmask%28_%29.md)
  Sets the mask used to filter which types of events are forwarded from the view to the composition during rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcview/eventforwardingmask())*