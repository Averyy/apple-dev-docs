# HandleChangeControlValue

**Framework**: AudioDriverKit  
**Kind**: method

Tells the stereo pan control the value is changing.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
virtual kern_return_t HandleChangeControlValue(float in_control_value);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/driverkit/kioreturnsuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/driverkit/error-codes).

#### Discussion

The default implementation calls [`SetControlValue`](iouseraudiostereopancontrol/setcontrolvalue.md) and returns [`kIOReturnSuccess`](https://developer.apple.com/documentation/driverkit/kioreturnsuccess). Subclass and override this method to handle changes to the stream format and return [`kIOReturnSuccess`](https://developer.apple.com/documentation/driverkit/kioreturnsuccess) upon success.

## Parameters

- `in_control_value`: The new floating-point stereo pan value to set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiostereopancontrol/handlechangecontrolvalue)*