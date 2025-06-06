# logicalMaximum

**Framework**: Core HID  
**Kind**: property

The logical maximum for this element’s data.

**Availability**:
- macOS 15.0+

## Declaration

```swift
var logicalMaximum: Int64?
```

#### Discussion

The logical maximum is specified in the report descriptor for an element. It determines the maximum raw value that should be considered valid, anything above this value is invalid.

See the HID specification for more details: [`https://www.usb.org/hid`](https://developer.apple.comhttps://www.usb.org/hid).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hidelement/logicalmaximum)*