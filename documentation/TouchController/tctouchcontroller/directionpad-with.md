# directionPad(with:)

**Framework**: Touch Controller  
**Kind**: method

Creates a new direction pad control with the provided descriptor.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func directionPad(with descriptor: TCDirectionPadDescriptor) -> TCDirectionPad
```

#### Return Value

A new `TCDirectionPad` instance.

## Parameters

- `descriptor`: The   containing the configuration for the direction pad.

## See Also

- [func button(with: TCButtonDescriptor) -> TCButton](tctouchcontroller/button(with:).md)
  Creates a new button control with the provided descriptor.
- [func throttle(with: TCThrottleDescriptor) -> TCThrottle](tctouchcontroller/throttle(with:).md)
  Creates a new throttle control with the provided descriptor.
- [func thumbstick(with: TCThumbstickDescriptor) -> TCThumbstick](tctouchcontroller/thumbstick(with:).md)
  Creates a new thumbstick control with the provided descriptor.
- [func touchpad(with: TCTouchpadDescriptor) -> TCTouchpad](tctouchcontroller/touchpad(with:).md)
  Creates a new touchpad control with the provided descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tctouchcontroller/directionpad(with:))*