# logicalMinimum

**Framework**: Core HID  
**Kind**: property

The logical minimum for this element’s data.

**Availability**:
- macOS 15.0+

## Declaration

```swift
var logicalMinimum: Int64?
```

#### Discussion

The logical minimum is specified in the report descriptor for an element. It determines the minimum raw value that should be considered valid, anything below this value is invalid.

See the HID specification for more details: [`https://www.usb.org/hid`](https://developer.apple.comhttps://www.usb.org/hid).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hidelement/logicalminimum)*