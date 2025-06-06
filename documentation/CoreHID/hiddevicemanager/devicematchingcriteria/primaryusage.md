# primaryUsage

**Framework**: Core HID  
**Kind**: property

The HID specification compliant usage for the device.

**Availability**:
- macOS 15.0+

## Declaration

```swift
var primaryUsage: HIDUsage?
```

#### Discussion

This is the main usage for the device, pulled from the top level collection of the report descriptor, specifying the general device type.

For more details, see [`HIDUsage`](hidusage.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hiddevicemanager/devicematchingcriteria/primaryusage)*