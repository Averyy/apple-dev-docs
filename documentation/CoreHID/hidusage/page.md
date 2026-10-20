# page

**Framework**: Core HID  
**Kind**: property  
**Role**: Instance Property

The usage page value.

**Availability**:
- macOS 15.0+

## Declaration

```swift
var page: UInt16 { get }
```

#### Discussion

This value determines the broader category of the functionality. This must always be specified, as a usage doesn’t have meaning without a page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hidusage/page)*