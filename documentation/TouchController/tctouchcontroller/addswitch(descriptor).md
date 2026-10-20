# addSwitch(descriptor:)

**Framework**: Touch Controller  
**Kind**: method  
**Role**: Instance Method

Creates a new switch control with the provided descriptor, and adds it to the touch controller.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
func addSwitch(descriptor: TCSwitchDescriptor) -> TCSwitch
```

```objc
- (TCSwitch *) addSwitchWithDescriptor:(TCSwitchDescriptor *) descriptor;
```

#### Return Value

A new `TCSwitch` instance.

## Parameters

- `descriptor`: The `TCSwitchDescriptor` containing the configuration for the switch.

## See Also

### Adding a switch control
- [class TCSwitchDescriptor](../tcswitchdescriptor.md)
  A descriptor for configuring a switch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tctouchcontroller/addswitch(descriptor:))*