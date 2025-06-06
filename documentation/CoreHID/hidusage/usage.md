# usage

**Framework**: Core HID  
**Kind**: property

The usage value.

**Availability**:
- macOS 15.0+

## Declaration

```swift
var usage: UInt16? { get }
```

#### Discussion

The usage combines with the page to determine specific functionality. This may not be specified, in which case the `HIDUsage` refers to the overall page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hidusage/usage)*