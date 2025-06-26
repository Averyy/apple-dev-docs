# throttle(with:)

**Framework**: Touch Controller  
**Kind**: method

Creates a new throttle control with the provided descriptor.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func throttle(with descriptor: TCThrottleDescriptor) -> TCThrottle
```

#### Return Value

A new `TCThrottle` instance.

## Parameters

- `descriptor`: The   containing the configuration for the throttle.

## See Also

- [func button(with: TCButtonDescriptor) -> TCButton](tctouchcontroller/button(with:).md)
  Creates a new button control with the provided descriptor.
- [func thumbstick(with: TCThumbstickDescriptor) -> TCThumbstick](tctouchcontroller/thumbstick(with:).md)
  Creates a new thumbstick control with the provided descriptor.
- [func touchpad(with: TCTouchpadDescriptor) -> TCTouchpad](tctouchcontroller/touchpad(with:).md)
  Creates a new touchpad control with the provided descriptor.
- [func directionPad(with: TCDirectionPadDescriptor) -> TCDirectionPad](tctouchcontroller/directionpad(with:).md)
  Creates a new direction pad control with the provided descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tctouchcontroller/throttle(with:))*