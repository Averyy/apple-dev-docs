# addThrottle(descriptor:)

**Framework**: Touch Controller  
**Kind**: method  
**Role**: Instance Method

Creates a new throttle control with the provided descriptor, and adds it to the touch controller.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
func addThrottle(descriptor: TCThrottleDescriptor) -> TCThrottle
```

```objc
- (TCThrottle *) addThrottleWithDescriptor:(TCThrottleDescriptor *) descriptor;
```

#### Return Value

A new `TCThrottle` instance.

## Parameters

- `descriptor`: The `TCThrottleDescriptor` containing the configuration for the throttle.

## See Also

### Adding a throttle control
- [class TCThrottleDescriptor](../tcthrottledescriptor.md)
  A descriptor for configuring a throttle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tctouchcontroller/addthrottle(descriptor:))*