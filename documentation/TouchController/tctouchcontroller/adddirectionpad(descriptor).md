# addDirectionPad(descriptor:)

**Framework**: Touch Controller  
**Kind**: method  
**Role**: Instance Method

Creates a new direction pad control with the provided descriptor, and adds it to the touch controller.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
func addDirectionPad(descriptor: TCDirectionPadDescriptor) -> TCDirectionPad
```

```objc
- (TCDirectionPad *) addDirectionPadWithDescriptor:(TCDirectionPadDescriptor *) descriptor;
```

## Return Value

A new `TCDirectionPad` instance.

## Parameters

- `descriptor`: The `TCDirectionPadDescriptor` containing the configuration for the direction pad.

## See Also

### Adding a directional pad control
- [class TCDirectionPadDescriptor](../tcdirectionpaddescriptor.md)
  A descriptor for configuring a directional pad.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tctouchcontroller/adddirectionpad(descriptor:))*