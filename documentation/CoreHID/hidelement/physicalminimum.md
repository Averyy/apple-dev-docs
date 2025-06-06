# physicalMinimum

**Framework**: Core HID  
**Kind**: property

The physical minimum for this element’s data.

**Availability**:
- macOS 15.0+

## Declaration

```swift
var physicalMinimum: Int64?
```

#### Discussion

The physical minimum combines with the physical maximum to determine the shifting and scaling required to transform the raw report data into the actual value that has meaning for the device.

See the HID specification for more details: [`https://www.usb.org/hid`](https://developer.apple.comhttps://www.usb.org/hid).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hidelement/physicalminimum)*