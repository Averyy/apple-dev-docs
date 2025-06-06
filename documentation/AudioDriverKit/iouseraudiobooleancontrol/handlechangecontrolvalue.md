# HandleChangeControlValue

**Framework**: AudioDriverKit  
**Kind**: method

Tells the Boolean control the value is changing.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t HandleChangeControlValue(bool in_control_value);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

The default implementation calls [`SetControlValue`](iouseraudiobooleancontrol/setcontrolvalue.md) and returns [`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess). Subclass and override this method to handle changes to the stream format and return [`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) upon success.

## Parameters

- `in_control_value`: The new Boolean value to set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiobooleancontrol/handlechangecontrolvalue)*