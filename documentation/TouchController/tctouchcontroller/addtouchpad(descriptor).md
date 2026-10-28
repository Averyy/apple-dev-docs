# addTouchpad(descriptor:)

**Framework**: Touch Controller  
**Kind**: method  
**Role**: Instance Method

Creates a new touchpad control with the provided descriptor, and adds it to the touch controller.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
func addTouchpad(descriptor: TCTouchpadDescriptor) -> TCTouchpad
```

```objc
- (TCTouchpad *) addTouchpadWithDescriptor:(TCTouchpadDescriptor *) descriptor;
```

## Return Value

A new `TCTouchpad` instance.

## Parameters

- `descriptor`: The `TCTouchpadDescriptor` containing the configuration for the touchpad.

## See Also

### Adding a touchpad control
- [class TCTouchpadDescriptor](../tctouchpaddescriptor.md)
  A descriptor for configuring a touchpad.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tctouchcontroller/addtouchpad(descriptor:))*