# touchpad(with:)

**Framework**: Touch Controller  
**Kind**: method

Creates a new touchpad control with the provided descriptor.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func touchpad(with descriptor: TCTouchpadDescriptor) -> TCTouchpad
```

#### Return Value

A new `TCTouchpad` instance.

## Parameters

- `descriptor`: The   containing the configuration for the touchpad.

## See Also

- [func button(with: TCButtonDescriptor) -> TCButton](tctouchcontroller/button(with:).md)
  Creates a new button control with the provided descriptor.
- [func throttle(with: TCThrottleDescriptor) -> TCThrottle](tctouchcontroller/throttle(with:).md)
  Creates a new throttle control with the provided descriptor.
- [func thumbstick(with: TCThumbstickDescriptor) -> TCThumbstick](tctouchcontroller/thumbstick(with:).md)
  Creates a new thumbstick control with the provided descriptor.
- [func directionPad(with: TCDirectionPadDescriptor) -> TCDirectionPad](tctouchcontroller/directionpad(with:).md)
  Creates a new direction pad control with the provided descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tctouchcontroller/touchpad(with:))*